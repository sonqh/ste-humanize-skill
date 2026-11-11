import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "evals", "eval.py")

spec = importlib.util.spec_from_file_location("skill_eval", SCRIPT)
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)

FIXTURE = {
    "id": "t", "mode": "Human", "task": "Rewrite", "request": "r", "input": "i",
    "checks": {"first_sentence": "delete", "must_contain": ["6 rows"],
               "must_not_contain": ["Kafka"], "max_words": 30, "shape": "bullets",
               "trailers": ["Cut candidates:"]},
}
GOOD = ("Delete the 6 rows, then run the migration again.\n\n"
        "- Finance may need the rows for the audit.\n"
        "- In that case, archive them.\n\n"
        "Cut candidates: the history of the column.\n")
BAD = ("Here is the rewrite. Kafka holds the rows; we have received them.\n\n"
       "Reader: a reviewer.\n")


def run(args):
    return subprocess.run([sys.executable, SCRIPT] + args, capture_output=True, text=True)


def failed(text):
    results, _ = ev.score_output(FIXTURE, text)
    return {name for name, ok, _ in results if not ok}


class FixtureTests(unittest.TestCase):
    # Covers: REQ-EVAL-001

    def test_fixtures_load_and_cover(self):
        """SCN-EVAL-001-1"""
        # Covers: REQ-EVAL-001
        fixtures = ev.load_fixtures()
        self.assertGreaterEqual(len(fixtures), 6)
        self.assertEqual({f["mode"] for f in fixtures}, {"Strict", "Human"})
        self.assertEqual({f["task"] for f in fixtures}, {"Rewrite", "Write"})
        shapes = {f["checks"].get("shape") for f in fixtures}
        self.assertIn("bullets", shapes)
        self.assertIn("prose", shapes)

    def test_long_fixtures(self):
        """SCN-EVAL-001-3"""
        # Covers: REQ-EVAL-001
        long = [f for f in ev.load_fixtures()
                if len(f["input"].split()) >= ev.LONG_INPUT_WORDS]
        self.assertGreaterEqual(len(long), 3)
        self.assertEqual({f["mode"] for f in long}, {"Strict", "Human"})
        self.assertEqual({f["task"] for f in long}, {"Rewrite", "Write"})
        for f in long:
            self.assertGreaterEqual(len(f["checks"]["must_contain"]), 15, f["id"])

    def test_bad_fixture_rejected(self):
        """SCN-EVAL-001-2"""
        # Covers: REQ-EVAL-001
        with tempfile.TemporaryDirectory() as d:
            for name, change in (("t.json", {"checks": {"no_such_check": 1}}),
                                 ("t.json", {"mode": "Loud"}),
                                 ("other.json", {})):
                path = os.path.join(d, name)
                with open(path, "w", encoding="utf-8") as fh:
                    json.dump({**FIXTURE, **change}, fh)
                with self.assertRaises(ev.FixtureError):
                    ev.load_fixture(path)
                os.remove(path)


class ScorerTests(unittest.TestCase):
    # Covers: REQ-EVAL-002

    def test_good_output_passes(self):
        """SCN-EVAL-002-1"""
        # Covers: REQ-EVAL-002
        self.assertEqual(failed(GOOD), set())

    def test_bad_output_fails_each_check(self):
        """SCN-EVAL-002-2"""
        # Covers: REQ-EVAL-002
        self.assertEqual(failed(BAD), {
            "no-preamble", "contains:6 rows", "omits:Kafka", "answer-first",
            "shape:bullets", "lint-hard", "trailers"})
        self.assertIn("max-words", failed(GOOD + "\n" + "More words here. " * 20))
        self.assertIn("no-long-paragraph", failed("Delete the 6 rows. " * 7))

    def test_same_output_same_score(self):
        """SCN-EVAL-002-3"""
        # Covers: REQ-EVAL-002
        self.assertEqual(ev.score_output(FIXTURE, GOOD), ev.score_output(FIXTURE, GOOD))

    def test_cli(self):
        """SCN-EVAL-002-4"""
        # Covers: REQ-EVAL-002
        r = run(["list"])
        self.assertEqual(r.returncode, 0)
        first = r.stdout.split("\t")[0]
        r = run(["prompt", first, "--skill", "/tmp/skill"])
        self.assertEqual(r.returncode, 0)
        self.assertIn("/tmp/skill/SKILL.md", r.stdout)
        self.assertNotIn("must_contain", r.stdout)
        self.assertEqual(run(["prompt", "no-such", "--skill", "x"]).returncode, 2)
        self.assertEqual(run(["score", "/no/such/folder"]).returncode, 2)
        with tempfile.TemporaryDirectory() as d:
            r = run(["score", d])
            self.assertEqual(r.returncode, 1)
            self.assertIn("missing output", r.stdout)

    def test_several_runs(self):
        """SCN-EVAL-002-5"""
        # Covers: REQ-EVAL-002
        fx = ev.load_fixtures()[0]["id"]
        with tempfile.TemporaryDirectory() as d:
            for name, text in (("run1", "Delete it.\n"), ("run2", "Here is the text.\n")):
                os.mkdir(os.path.join(d, name))
                with open(os.path.join(d, name, fx + ".md"), "w", encoding="utf-8") as fh:
                    fh.write(text)
            runs = [os.path.join(d, "run1"), os.path.join(d, "run2")]
            r = run(["score"] + runs + ["--only", fx])
            self.assertEqual(r.returncode, 1)
            self.assertIn("in 2 runs", r.stdout)
            self.assertIn("fail no-preamble in 1 of 2 runs", r.stdout)
            self.assertNotIn("missing output", r.stdout)
            data = json.loads(run(["score"] + runs + ["--only", fx, "--json"]).stdout)
            self.assertEqual(len(data["runs"]), 2)
            self.assertEqual(run(["score", runs[0], "--only", "no-such"]).returncode, 2)


if __name__ == "__main__":
    unittest.main()
