import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "scripts", "ste-lint.py")
RULES_JSON = os.path.join(ROOT, "tests", "ste_rules.json")

spec = importlib.util.spec_from_file_location("ste_lint", SCRIPT)
ste = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ste)

WORDS_26 = " ".join(f"w{i}" for i in range(26)) + ".\n"


def run(args, text=None):
    return subprocess.run([sys.executable, SCRIPT] + args, input=text,
                          capture_output=True, text=True)


def run_file(text, args=()):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "doc.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return run(list(args) + [path])


class SteLintTests(unittest.TestCase):
    def test_table_matches_record(self):
        """SCN-STE-001-1"""
        # Covers: REQ-STE-001
        with open(RULES_JSON, encoding="utf-8") as fh:
            recorded = [(r["id"], r["level"]) for r in json.load(fh)]
        actual = [(r[0], r[1]) for r in ste.RULES]
        self.assertEqual(actual, recorded)
        for _, level in actual:
            self.assertIn(level, ("advisory-free", "advisory"))

    def test_messages_bounded(self):
        """SCN-STE-001-2"""
        # Covers: REQ-STE-001
        for rule_id, _, _, message in ste.RULES:
            self.assertTrue(message, rule_id)
            self.assertLess(len(message), 160, rule_id)

    def test_long_sentence(self):
        """SCN-STE-002-1"""
        # Covers: REQ-STE-002
        findings, _ = ste.lint(WORDS_26)
        hits = [f for f in findings if f["rule"] == "long-sentence"]
        self.assertEqual(len(hits), 1)
        self.assertIn("26", hits[0]["message"])

    def test_hedge_protected(self):
        """SCN-STE-002-2"""
        # Covers: REQ-STE-002
        findings, _ = ste.lint("The request may have failed.\n")
        self.assertEqual(findings, [])

    def test_code_skipped(self):
        """SCN-STE-002-3"""
        # Covers: REQ-STE-002
        text = "Run this.\n\n```\nx = 1;\n```\n"
        findings, _ = ste.lint(text)
        self.assertNotIn("semicolon", {f["rule"] for f in findings})
        findings, _ = ste.lint("Run this; then stop.\n")
        self.assertIn("semicolon", {f["rule"] for f in findings})

    def test_disable(self):
        """SCN-STE-003-1"""
        # Covers: REQ-STE-003
        text = "Check the file. Verify the file.\n"
        self.assertEqual(run_file(text).returncode, 1)
        self.assertEqual(run_file(text, ["--disable", "synonym-rotation"]).returncode, 0)

    def test_summary_line(self):
        """SCN-STE-003-2"""
        # Covers: REQ-STE-003
        lines = run_file("Run the build.\n").stdout.rstrip("\n").splitlines()
        self.assertRegex(lines[-2], r"\d+ violations \(\d+ hard, baseline \d+\)")
        self.assertIn("Hedges/modality", lines[-1])

    def test_json_shape(self):
        """SCN-STE-003-3"""
        # Covers: REQ-STE-003
        data = json.loads(run_file("Run the build.\n", ["--json"]).stdout)
        self.assertIsInstance(data, dict)
        self.assertEqual(set(data), {"violations", "count", "hard_count",
                                     "baseline", "words", "per_100_words"})

    def test_unknown_rule_and_selftest(self):
        """SCN-STE-003-3 CLI exits"""
        # Covers: REQ-STE-003
        r = run(["--disable", "not-a-rule"], text="Hello.\n")
        self.assertEqual(r.returncode, 2)
        self.assertIn("not-a-rule", r.stderr)
        self.assertIn("semicolon", r.stderr)
        r = run(["--selftest"])
        self.assertEqual(r.returncode, 0)
        self.assertIn("selftest OK", r.stdout)


if __name__ == "__main__":
    unittest.main()
