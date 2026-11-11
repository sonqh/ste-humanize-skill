#!/usr/bin/env python3
"""Score what an agent wrote with the skill. No model call, no network.

Usage:
    eval.py list
    eval.py prompt ID --skill DIR      # print the prompt for a runner
    eval.py score DIR [DIR ...] [--only IDS] [--json]
                                       # one DIR for each run, with DIR/<id>.md

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
LONG_INPUT_WORDS = 600
REQUIRED_KEYS = ("id", "mode", "task", "request", "input", "checks")
MODES = ("Strict", "Human")
TASKS = ("Rewrite", "Write")
SHAPES = ("bullets", "numbered", "prose", "any")
CHECK_KEYS = {"must_contain", "must_not_contain", "first_sentence", "max_words",
              "shape", "trailers", "early"}
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
    # REQ-EVAL-003
    for item in checks.get("early", []):
        if (not isinstance(item, dict) or set(item) != {"pattern", "within_words"}
                or not isinstance(item["within_words"], int) or item["within_words"] < 1):
            raise FixtureError(f"{name}: an early check needs pattern and within_words")
        try:
            re.compile(item["pattern"])
        except re.error as e:
            raise FixtureError(f"{name}: bad pattern {item['pattern']!r}: {e}")
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
    # REQ-EVAL-003 the reader can act near the top: the pattern starts in the first N words
    for item in checks.get("early", []):
        m = re.search(item["pattern"], body, re.I)
        at = len(body[:m.start()].split()) if m else None
        add(f"early:{item['pattern']}", at is not None and at < item["within_words"],
            "absent" if at is None else f"at word {at}, limit {item['within_words']}")
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


def score_run(outputs, fixtures):
    """Score one folder of outputs. Return a list with one entry per fixture."""
    report = []
    for fx in fixtures:
        path = os.path.join(outputs, fx["id"] + ".md")
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            report.append({"id": fx["id"], "missing": True, "checks": [], "words": 0})
            continue
        results, words = score_output(fx, text)
        report.append({"id": fx["id"], "missing": False, "words": words,
                       "checks": [{"name": n, "pass": ok, "detail": d} for n, ok, d in results]})
    return report


# REQ-EVAL-002
def cmd_score(folders, as_json, fixtures):
    """Score one folder for each run. Report each check as passes out of runs."""
    runs = [{"dir": d, "fixtures": score_run(d, fixtures)} for d in folders]
    n = len(runs)
    total = sum(len(r["checks"]) for run in runs for r in run["fixtures"])
    passed = sum(1 for run in runs for r in run["fixtures"] for c in r["checks"] if c["pass"])
    missing = sum(1 for run in runs for r in run["fixtures"] if r["missing"])
    if as_json:
        print(json.dumps({"runs": runs, "passed": passed, "total": total}, indent=2))
        return 1 if missing or passed < total else 0
    for index, fx in enumerate(fixtures):
        entries = [run["fixtures"][index] for run in runs]
        present = [e for e in entries if not e["missing"]]
        if len(present) < n:
            where = "" if n == 1 else f" in {n - len(present)} of {n} runs"
            print(f"{fx['id']}: missing output{where}")
        if not present:
            continue
        ok = sum(1 for e in present for c in e["checks"] if c["pass"])
        count = sum(len(e["checks"]) for e in present)
        words = round(sum(e["words"] for e in present) / len(present))
        if n == 1:
            print(f"{fx['id']}: {ok}/{count} checks, {words} words")
        else:
            print(f"{fx['id']}: {ok}/{count} checks in {len(present)} runs, mean {words} words")
        fails = {}
        for e in present:
            for c in e["checks"]:
                if not c["pass"]:
                    fails.setdefault(c["name"], []).append(c["detail"])
        for name, details in fails.items():
            detail = next((d for d in details if d), "")
            times = "" if n == 1 else f" in {len(details)} of {len(present)} runs"
            print(f"  fail {name}{times}" + (f" [{detail}]" if detail else ""))
    print(f"{passed}/{total} checks passed" + ("" if n == 1 else f" in {n} runs"))
    return 1 if missing or passed < total else 0


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
    s.add_argument("outputs", metavar="OUTPUTS_DIR", nargs="+",
                   help="One folder for each run.")
    s.add_argument("--only", default="", metavar="IDS",
                   help="Score these fixtures only. Give ids with commas.")
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
    for folder in a.outputs:
        if not os.path.isdir(folder):
            print(f"not a folder: {folder}", file=sys.stderr)
            return 2
    only = [i.strip() for i in a.only.split(",") if i.strip()]
    unknown = set(only) - {fx["id"] for fx in fixtures}
    if unknown:
        print(f"unknown fixture(s): {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2
    if only:
        fixtures = [fx for fx in fixtures if fx["id"] in only]
    return cmd_score(a.outputs, a.json, fixtures)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
