import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "scripts", "tells-lint.py")

spec = importlib.util.spec_from_file_location("tells_lint", SCRIPT)
tells = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tells)

HARD = {"dash", "not-x-but-y", "not-x-its-y", "chat-residue", "run-up",
        "deep-saying", "stock-word", "bold-label", "emoji-heading"}
ADVISORY = {"sales-word", "title-case-heading", "stacked-qualifier",
            "serves-as", "closer", "repeated-closer"}


def run(args, text=None):
    return subprocess.run([sys.executable, SCRIPT] + args, input=text,
                          capture_output=True, text=True)


def run_file(text, args=()):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "doc.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return run(list(args) + [path])


class TellsLintTests(unittest.TestCase):
    def test_hard_table(self):
        """SCN-TELLS-001-1"""
        # Covers: REQ-TELLS-001
        got = {n for n, (lvl, _) in tells.RULES.items() if lvl == "hard"}
        self.assertEqual(got, HARD)

    def test_bold_label_colon_inside(self):
        """SCN-TELLS-001-2"""
        # Covers: REQ-TELLS-001
        hits = [f for f in tells.lint("- **Speed:** fast\n") if f["rule"] == "bold-label"]
        self.assertEqual(len(hits), 1)

    def test_dash_as_glue(self):
        """SCN-TELLS-001-3"""
        # Covers: REQ-TELLS-001
        text = "The tool — fast and small.\n"
        self.assertIn("dash", {f["rule"] for f in tells.lint(text)})
        self.assertEqual(run_file(text).returncode, 1)

    def test_advisory_table(self):
        """SCN-TELLS-002-1"""
        # Covers: REQ-TELLS-002
        got = {n for n, (lvl, _) in tells.RULES.items() if lvl == "advisory"}
        self.assertEqual(got, ADVISORY)

    def test_advisory_does_not_fail(self):
        """SCN-TELLS-002-2"""
        # Covers: REQ-TELLS-002
        r = run_file("Run the build.\n\nRead that again.\n")
        self.assertEqual(r.returncode, 0)
        self.assertIn("closer", r.stdout)

    def test_baseline(self):
        """SCN-TELLS-003-1"""
        # Covers: REQ-TELLS-003
        text = "A — b.\n\nC — d.\n\nE — f.\n"
        self.assertEqual(run_file(text).returncode, 1)
        self.assertEqual(run_file(text, ["--baseline", "3"]).returncode, 0)

    def test_json_shape(self):
        """SCN-TELLS-003-2"""
        # Covers: REQ-TELLS-003
        r = run_file("The tool — fast.\n", ["--json"])
        data = json.loads(r.stdout)
        self.assertIsInstance(data, list)
        entry = data[0]
        self.assertIn("file", entry)
        self.assertEqual(len(entry["findings"]), 1)
        for key in ("line", "rule", "level", "match"):
            self.assertIn(key, entry["findings"][0])

    def test_unknown_rule(self):
        """SCN-TELLS-003-3"""
        # Covers: REQ-TELLS-003
        r = run(["--disable", "not-a-rule"], text="Hello.\n")
        self.assertEqual(r.returncode, 2)
        self.assertIn("not-a-rule", r.stderr + r.stdout)


if __name__ == "__main__":
    unittest.main()
