import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "scripts", "lint.py")

# One stock-word tell on line 1, one semicolon STE finding on line 2.
BOTH = "The team leverages the cache.\nRun it first; then stop.\n"


def run(args, text=None):
    return subprocess.run([sys.executable, SCRIPT] + args, input=text,
                          capture_output=True, text=True)


def run_file(text, args=()):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "doc.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        r = run(list(args) + [path])
    return r


class LintCliTests(unittest.TestCase):
    def test_both_sources(self):
        """SCN-LINT-001-1"""
        # Covers: REQ-LINT-001
        r = run_file(BOTH)
        lines = r.stdout.splitlines()
        self.assertEqual(len(lines), 2, r.stdout)
        self.assertRegex(lines[0], r"doc\.md:1:\d+ stock-word \[hard\] leverages$")
        self.assertRegex(lines[1], r"doc\.md:2:\d+ semicolon \[hard\] ;$")
        self.assertEqual(r.returncode, 1)

    def test_only_one_source(self):
        """SCN-LINT-001-2"""
        # Covers: REQ-LINT-001
        r = run_file(BOTH, ["--only", "ste"])
        lines = r.stdout.splitlines()
        self.assertEqual(len(lines), 1, r.stdout)
        self.assertIn("semicolon", lines[0])
        self.assertNotIn("stock-word", r.stdout)

    def test_empty_input(self):
        """SCN-LINT-001-3"""
        # Covers: REQ-LINT-001
        r = run([], text="")
        self.assertEqual(r.returncode, 2)
        self.assertIn("no input", r.stderr + r.stdout)

    def test_json_shape(self):
        """SCN-LINT-002-1"""
        # Covers: REQ-LINT-002
        r = run_file(BOTH, ["--json"])
        data = json.loads(r.stdout)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertIn("file", data[0])
        findings = data[0]["findings"]
        self.assertEqual(len(findings), 2)
        for f in findings:
            self.assertEqual(set(f), {"rule", "level", "line", "col", "match", "source"})
        self.assertEqual({f["source"] for f in findings}, {"tells", "ste"})

    def test_baseline_and_advisory(self):
        """Exit codes: baseline and advisory findings."""
        # Covers: REQ-LINT-001
        self.assertEqual(run_file(BOTH, ["--baseline", "2"]).returncode, 0)
        self.assertEqual(run_file("Run the build.\n\nRead that again.\n").returncode, 0)

    def test_disable_and_unknown_rule(self):
        """--disable filters both sources and rejects unknown names."""
        # Covers: REQ-LINT-001
        r = run_file(BOTH, ["--disable", "stock-word,semicolon"])
        self.assertEqual(r.stdout.strip(), "")
        self.assertEqual(r.returncode, 0)
        r = run(["--disable", "not-a-rule"], text="Hello.\n")
        self.assertEqual(r.returncode, 2)
        self.assertIn("not-a-rule", r.stderr)

    def test_hook_id(self):
        """SCN-LINT-003-1"""
        # Covers: REQ-LINT-003
        with open(os.path.join(ROOT, ".pre-commit-hooks.yaml"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertEqual(len(re.findall(r"^- id:", text, re.M)), 1)
        self.assertRegex(text, r"(?m)^- id: ste-humanize-lint\s*$")
        self.assertRegex(text, r"(?m)^\s+entry: .*scripts/lint\.py")

    def test_action_inputs(self):
        """SCN-LINT-003-2"""
        # Covers: REQ-LINT-003
        with open(os.path.join(ROOT, "action.yml"), encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        inputs, block = set(), None
        for line in lines:
            if re.match(r"^\S", line):
                block = line.split(":")[0]
            elif block == "inputs":
                m = re.match(r"^  (\w+):\s*$", line)
                if m:
                    inputs.add(m.group(1))
        self.assertTrue({"files", "baseline"} <= inputs, inputs)
        self.assertIn("  using: composite", lines)
        with open(os.path.join(ROOT, ".github", "workflows", "ci.yml"), encoding="utf-8") as fh:
            ci = fh.read()
        self.assertIn("uses: ./", ci)


if __name__ == "__main__":
    unittest.main()
