#!/usr/bin/env python3
"""Score what an agent wrote with the skill. No model call, no network.

Usage:
    eval.py list
    eval.py prompt ID --skill DIR      # print the prompt for a runner
    eval.py score OUTPUTS_DIR [--json] # read OUTPUTS_DIR/<id>.md for each fixture

A fixture is one JSON file in evals/fixtures/. A runner (an agent, or a person)
writes one output file per fixture. The scorer applies the checks of the
fixture to that file. The same output always gets the same score.

Exit 0 when every check of every fixture passes. Exit 1 when a check fails or
an output file is missing. Exit 2 on a usage error or a bad fixture.
"""
import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FIXTURES = os.path.join(HERE, "fixtures")

# REQ-EVAL-001
REQUIRED_KEYS = ("id", "mode", "task", "request", "input", "checks")
MODES = ("Strict", "Human")
TASKS = ("Rewrite", "Write")
SHAPES = ("bullets", "numbered", "prose", "any")
CHECK_KEYS = {"must_contain", "must_not_contain", "first_sentence", "max_words",
              "shape", "trailers"}
TRAILERS = ("Kept as-is:", "Cut candidates:", "Reader:")
PREAMBLE = re.compile(
    r"^(?:here(?:'s| is| are)|sure\b|certainly\b|of course\b|below is|i have |i've |okay\b)",
    re.I)
BULLET = re.compile(r"^\s*[-*+]\s+\S", re.M)
NUMBERED = re.compile(r"^\s*\d+[.)]\s+\S", re.M)
FENCE = re.compile(r"^\s*(```|~~~)")


def _load_lint():
    spec = importlib.util.spec_from_file_location(
        "lint", os.path.join(ROOT, "scripts", "lint.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lint = _load_lint()


class FixtureError(Exception):
    pass


# REQ-EVAL-001
def load_fixture(path):
    """Read one fixture and reject a shape the scorer does not know."""
    try:
        with open(path, encoding="utf-8") as fh:
            fx = json.load(fh)
    except (OSError, ValueError) as e:
        raise FixtureError(f"{path}: {e}")
    name = os.path.basename(path)
    for key in REQUIRED_KEYS:
        if key not in fx:
            raise FixtureError(f"{name}: missing key {key}")
    if fx["id"] + ".json" != name:
        raise FixtureError(f"{name}: id {fx['id']!r} does not match the file name")
    if fx["mode"] not in MODES or fx["task"] not in TASKS:
        raise FixtureError(f"{name}: bad mode or task")
    checks = fx["checks"]
    unknown = set(checks) - CHECK_KEYS
    if unknown:
        raise FixtureError(f"{name}: unknown check(s): {', '.join(sorted(unknown))}")
    if checks.get("shape", "any") not in SHAPES:
        raise FixtureError(f"{name}: bad shape")
    for key in ("must_contain", "must_not_contain"):
        for pattern in checks.get(key, []):
            try:
                re.compile(pattern)
            except re.error as e:
                raise FixtureError(f"{name}: bad pattern {pattern!r}: {e}")
    return fx


def load_fixtures(directory=FIXTURES):
    names = sorted(n for n in os.listdir(directory) if n.endswith(".json"))
    return [load_fixture(os.path.join(directory, n)) for n in names]


def split_output(text):
    """Return (body, trailers). Trailers are the permitted lines after the text."""
    lines = text.strip().splitlines()
    trailers = []
    while lines and (not lines[-1].strip() or lines[-1].lstrip().startswith(TRAILERS)):
        line = lines.pop().strip()
        if line:
            trailers.insert(0, line.split(":", 1)[0] + ":")
    return "\n".join(lines).strip(), trailers


def _prose(body):
    """The body with no code block, heading, list marker, or quote mark."""
    out, in_fence = [], False
    for line in body.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or line.lstrip().startswith("#"):
            continue
        line = re.sub(r"^\s*(?:>\s?)+", "", line)
        out.append(re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line))
    return "\n".join(out)


def first_sentence(body):
    prose = " ".join(_prose(body).split())
    m = re.search(r"(?<=[.!?:])\s", prose)
    return prose[:m.start()] if m else prose


# REQ-EVAL-002
def score_output(fx, text):
    """Apply the checks of one fixture. Return a list of (name, passed, detail)."""
    checks = fx["checks"]
    body, trailers = split_output(text)
    results = []

    def add(name, passed, detail=""):
        results.append((name, bool(passed), detail))

    add("not-empty", bool(body))
    first_line = next((l for l in body.splitlines() if l.strip()), "")
    add("no-preamble", not PREAMBLE.match(first_line.strip()), first_line[:60])
    for pattern in checks.get("must_contain", []):
        add(f"contains:{pattern}", re.search(pattern, body, re.I))
    for pattern in checks.get("must_not_contain", []):
        m = re.search(pattern, body, re.I)
        add(f"omits:{pattern}", not m, m.group(0) if m else "")
    if "first_sentence" in checks:
        sentence = first_sentence(body)
        add("answer-first", re.search(checks["first_sentence"], sentence, re.I), sentence[:80])
    words = len(_prose(body).split())
    if "max_words" in checks:
        add("max-words", words <= checks["max_words"], f"{words} of {checks['max_words']}")
    shape = checks.get("shape", "any")
    has_bullets, has_numbers = bool(BULLET.search(body)), bool(NUMBERED.search(body))
    if shape == "bullets":
        add("shape:bullets", has_bullets)
    elif shape == "numbered":
        add("shape:numbered", has_numbers)
    elif shape == "prose":
        add("shape:prose", not has_bullets and not has_numbers)
    findings = lint.lint_text(body, fx["id"])
    hard = [f for f in findings if f["level"] == "hard"]
    add("lint-hard", not hard, ", ".join(sorted({f["rule"] for f in hard})))
    long_paragraphs = [f for f in findings if f["rule"] == "long-paragraph"]
    add("no-long-paragraph", not long_paragraphs)
    allowed = set(checks.get("trailers", []))
    extra = [t for t in trailers if t not in allowed]
    add("trailers", not extra, ", ".join(extra))
    return results, words


def build_prompt(fx, skill_dir):
    """The prompt a runner gives to an agent. It names no check."""
    return (
        f"Use the skill in {skill_dir}. Read {os.path.join(skill_dir, 'SKILL.md')} first, "
        "then every file that it tells you to read for this task. Follow the skill exactly.\n\n"
        f"Request from the user:\n{fx['request']}\n\n"
        f"Material:\n<<<\n{fx['input']}\n>>>\n\n"
        "You cannot ask the user a question. Reply with the output of the skill and nothing else."
    )


def cmd_score(outputs, as_json):
    report, failed = [], 0
    for fx in load_fixtures():
        path = os.path.join(outputs, fx["id"] + ".md")
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            report.append({"id": fx["id"], "missing": True, "checks": [], "words": 0})
            failed += 1
            continue
        results, words = score_output(fx, text)
        failed += sum(1 for _, ok, _ in results if not ok)
        report.append({"id": fx["id"], "missing": False, "words": words,
                       "checks": [{"name": n, "pass": ok, "detail": d} for n, ok, d in results]})
    total = sum(len(r["checks"]) for r in report)
    passed = sum(1 for r in report for c in r["checks"] if c["pass"])
    if as_json:
        print(json.dumps({"fixtures": report, "passed": passed, "total": total}, indent=2))
    else:
        for r in report:
            if r["missing"]:
                print(f"{r['id']}: missing output")
                continue
            ok = sum(1 for c in r["checks"] if c["pass"])
            print(f"{r['id']}: {ok}/{len(r['checks'])} checks, {r['words']} words")
            for c in r["checks"]:
                if not c["pass"]:
                    print(f"  fail {c['name']}" + (f" [{c['detail']}]" if c["detail"] else ""))
        print(f"{passed}/{total} checks passed")
    return 1 if failed else 0


# REQ-EVAL-002
def main(argv):
    ap = argparse.ArgumentParser(prog="eval.py", allow_abbrev=False,
                                 description="Score outputs written with the skill.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="Print the fixture ids.")
    p = sub.add_parser("prompt", help="Print the runner prompt of one fixture.")
    p.add_argument("id")
    p.add_argument("--skill", required=True, metavar="DIR", help="Folder that holds SKILL.md.")
    s = sub.add_parser("score", help="Score one output file per fixture.")
    s.add_argument("outputs", metavar="OUTPUTS_DIR")
    s.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        fixtures = load_fixtures()
    except FixtureError as e:
        print(e, file=sys.stderr)
        return 2
    if a.cmd == "list":
        for fx in fixtures:
            print(f"{fx['id']}\t{fx['mode']}\t{fx['task']}")
        return 0
    if a.cmd == "prompt":
        for fx in fixtures:
            if fx["id"] == a.id:
                print(build_prompt(fx, a.skill))
                return 0
        print(f"unknown fixture: {a.id}", file=sys.stderr)
        return 2
    if not os.path.isdir(a.outputs):
        print(f"not a folder: {a.outputs}", file=sys.stderr)
        return 2
    return cmd_score(a.outputs, a.json)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
