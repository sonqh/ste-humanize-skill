import importlib.util
import json
import os
import re
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
            "serves-as", "closer", "repeated-closer", "false-balance",
            "actorless-decision", "empty-mitigation", "unmeasured-quality",
            "support-cliche", "vague-date", "blame-phrase", "negative-contraction",
            "particle-repeat"}


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

    def test_contrast_across_dash(self):
        """SCN-TELLS-001-4"""
        # Covers: REQ-TELLS-001
        hits = [f for f in tells.lint("It's not just a linter \u2014 it's a gate.\n")
                if f["rule"] == "not-x-its-y"]
        self.assertEqual(len(hits), 1)
        for sep in (",", ".", ":", ";", " -", "\u2013"):
            text = f"It's not a tool{sep} it's a mirror.\n"
            self.assertIn("not-x-its-y", {f["rule"] for f in tells.lint(text)}, sep)
        self.assertNotIn("not-x-its-y", {f["rule"] for f in tells.lint("It's not here. The tool works.\n")})

    def test_inflected_stock_word(self):
        """SCN-TELLS-001-5"""
        # Covers: REQ-TELLS-001
        hits = [f for f in tells.lint("The team leverages the cache.\n") if f["rule"] == "stock-word"]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["match"], "leverages")
        for w in ("leveraged", "leveraging", "delves", "tapestries", "deep dives", "aligned with"):
            self.assertIn("stock-word", {f["rule"] for f in tells.lint(f"We saw {w} here.\n")}, w)
        self.assertNotIn("stock-word", {f["rule"] for f in tells.lint("Use a lever.\n")})

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

    def test_help_strings(self):
        """SCN-TELLS-003-4"""
        # Covers: REQ-TELLS-003
        out = run(["--help"]).stdout.split("\n")
        start = next(i for i, l in enumerate(out) if l.startswith("positional arguments"))
        entries, cur = [], None
        for l in out[start:]:
            if l.startswith("  ") and l.strip():
                if l[2] != " ":
                    cur = [l.strip()]
                    entries.append(cur)
                elif cur is not None:
                    cur.append(l.strip())
        self.assertGreaterEqual(len(entries), 6)
        for e in entries:
            self.assertTrue(len(e) > 1 or re.search(r"\S\s{2,}\S", e[0]), e)

    def test_empty_input(self):
        """SCN-TELLS-003-5"""
        # Covers: REQ-TELLS-003
        r = run([], text="")
        self.assertEqual(r.returncode, 2)
        self.assertIn("no input", r.stderr + r.stdout)


class DecisionTellTests(unittest.TestCase):
    # Covers: REQ-TELLS-004

    def _rules(self, text):
        return [f["rule"] for f in tells.lint(text + "\n")]

    def test_false_balance(self):
        """SCN-TELLS-004-1"""
        # Covers: REQ-TELLS-004
        self.assertEqual(self._rules("Both options have their merits.").count("false-balance"), 1)

    def test_actorless_decision(self):
        """SCN-TELLS-004-2"""
        # Covers: REQ-TELLS-004
        self.assertEqual(self._rules("It was decided that the team uses pg-boss.").count("actorless-decision"), 1)
        self.assertEqual(self._rules("The team decided to use pg-boss."), [])

    def test_empty_mitigation(self):
        """SCN-TELLS-004-3"""
        # Covers: REQ-TELLS-004
        self.assertEqual(self._rules("Mitigation: we will monitor closely.").count("empty-mitigation"), 1)

    def test_unmeasured_quality(self):
        """SCN-TELLS-004-4"""
        # Covers: REQ-TELLS-004
        self.assertEqual(self._rules("Option B is more scalable.").count("unmeasured-quality"), 1)
        self.assertEqual(self._rules("Option B scales to 350 jobs per second."), [])

    def test_decision_tells_are_advisory(self):
        """SCN-TELLS-004-5"""
        # Covers: REQ-TELLS-004
        text = ("Both options have their merits.\n\nIt was decided that we use A.\n\n"
                "Mitigation: we will monitor closely.\n\nOption B is more scalable.\n")
        r = run_file(text)
        self.assertEqual(r.returncode, 0)
        for rule in ("false-balance", "actorless-decision", "empty-mitigation", "unmeasured-quality"):
            self.assertEqual(r.stdout.count(rule), 1, rule)


class MessageTellTests(unittest.TestCase):
    # Covers: REQ-TELLS-005

    def _rules(self, text):
        return [f["rule"] for f in tells.lint(text + "\n")]

    def test_support_cliche(self):
        """SCN-TELLS-005-1"""
        # Covers: REQ-TELLS-005
        rules = self._rules("We apologize for any inconvenience.\nMong quý khách thông cảm.")
        self.assertEqual(rules.count("support-cliche"), 2)

    def test_vague_date(self):
        """SCN-TELLS-005-2"""
        # Covers: REQ-TELLS-005
        self.assertIn("vague-date", self._rules("We will fix it soon."))
        self.assertIn("vague-date", self._rules("Bên em sẽ xử lý trong thời gian sớm nhất."))
        self.assertNotIn("vague-date", self._rules("We will fix it on 3 March."))

    def test_blame_and_contraction(self):
        """SCN-TELLS-005-3"""
        # Covers: REQ-TELLS-005
        rules = self._rules("You forgot to save, so we can't restore it.")
        self.assertEqual(rules.count("blame-phrase"), 1)
        self.assertEqual(rules.count("negative-contraction"), 1)

    def test_particle_once_per_file(self):
        """SCN-TELLS-005-4"""
        # Covers: REQ-TELLS-005
        rules = self._rules("Dạ, em gửi anh bảng giá ạ.\n\nAnh xem giúp em ạ.")
        self.assertEqual(rules.count("particle-repeat"), 1)
        self.assertNotIn("particle-repeat", self._rules("Em gửi anh bảng giá ạ."))

    def test_vietnamese_contrast(self):
        """SCN-TELLS-001-6"""
        # Covers: REQ-TELLS-001
        rules = self._rules("Không phải lỗi hệ thống mà là do cấu hình.")
        self.assertEqual(rules.count("not-x-but-y"), 1)


if __name__ == "__main__":
    unittest.main()
