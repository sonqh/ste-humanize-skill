#!/usr/bin/env python3
"""One command for both linters: the AI tells and the structural STE rules.

Usage:
    lint.py FILE [FILE ...]
    echo "text" | lint.py [--json]
    lint.py --baseline 5 FILE
    lint.py --only tells FILE
    lint.py --disable dash,semicolon FILE

Each finding prints as file:line:col rule [level] match.
Exit 1 when hard findings exceed the baseline (default 0).
Advisory findings never fail the run.
Exit 2 on a usage error or empty input.
"""
import argparse
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


tells = _load("tells_lint", "tells-lint.py")
ste = _load("ste_lint", "ste-lint.py")


def _non_negative_int(value):
    try:
        n = int(value)
    except ValueError:
        n = -1
    if n < 0:
        raise argparse.ArgumentTypeError(f"expected a non-negative integer, got {value!r}")
    return n


def _column(text_lines, line, match):
    """Return the 1-based column of a match on its line, or 1 if not found."""
    if not match or not 1 <= line <= len(text_lines):
        return 1
    first = str(match).split("\n")[0]
    idx = text_lines[line - 1].find(first)
    return idx + 1 if idx >= 0 else 1


# REQ-LINT-001
def lint_text(text, name, only=None, disabled=frozenset()):
    """Return the findings of both rule sets for one text, in one shape."""
    lines = text.splitlines()
    out = []
    if only in (None, "tells"):
        for f in tells.lint(text, disabled & set(tells.RULES)):
            out.append({"rule": f["rule"], "level": f["level"], "line": f["line"],
                        "col": _column(lines, f["line"], f["match"]),
                        "match": str(f["match"]), "source": "tells"})
    if only in (None, "ste"):
        found, _ = ste.lint(text, filename=name)
        for f in found:
            if f["rule"] in disabled:
                continue
            level = "hard" if f["level"] == "advisory-free" else "advisory"
            out.append({"rule": f["rule"], "level": level, "line": f["line"],
                        "col": f["col"], "match": str(f["match"]), "source": "ste"})
    out.sort(key=lambda f: (f["line"], f["col"], f["rule"]))
    return out


# REQ-LINT-001 REQ-LINT-002
def main(argv):
    ap = argparse.ArgumentParser(
        prog="lint.py", allow_abbrev=False,
        description="Check files for AI tells and structural STE rules.")
    ap.add_argument("files", nargs="*", metavar="FILE",
                    help="Files to check. Read stdin if none.")
    ap.add_argument("--baseline", type=_non_negative_int, default=0, metavar="N",
                    help="Allow N hard findings. Default 0.")
    ap.add_argument("--disable", default="", metavar="RULES",
                    help="Turn off rules. Give names with commas.")
    ap.add_argument("--only", choices=("tells", "ste"),
                    help="Run one rule set only.")
    ap.add_argument("--json", action="store_true", help="Print the findings as JSON.")
    a = ap.parse_intermixed_args(argv)

    disabled = {d.strip() for d in a.disable.split(",") if d.strip()}
    unknown = disabled - set(tells.RULES) - set(ste.RULE_IDS)
    if unknown:
        print(f"unknown rule(s): {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    sources = []
    if a.files:
        for p in a.files:
            try:
                with open(p, encoding="utf-8") as fh:
                    sources.append((p, fh.read()))
            except OSError as e:
                print(f"cannot read {p}: {e.strerror}", file=sys.stderr)
                return 2
    else:
        data = sys.stdin.read()
        if not data.strip():
            print("no input", file=sys.stderr)
            return 2
        sources.append(("<stdin>", data))

    report, hard = [], 0
    for name, text in sources:
        fs = lint_text(text, name, a.only, frozenset(disabled))
        hard += sum(1 for f in fs if f["level"] == "hard")
        report.append({"file": name, "findings": fs})

    if a.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for entry in sorted(report, key=lambda e: e["file"]):
            for f in entry["findings"]:
                match = " ".join(f["match"].split())
                print(f"{entry['file']}:{f['line']}:{f['col']} {f['rule']} [{f['level']}] {match}")
        print(f"{hard} hard finding(s), baseline {a.baseline}", file=sys.stderr)
    return 1 if hard > a.baseline else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
