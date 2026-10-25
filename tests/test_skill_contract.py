import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "SKILL.md")


def section(name):
    with open(SKILL, encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(r"^## " + re.escape(name) + r"\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    assert m, f"missing section: {name}"
    return m.group(1)


class SkillContractTests(unittest.TestCase):
    def test_two_modes(self):
        """SCN-SKILL-001-1"""
        # Covers: REQ-SKILL-001
        body = section("Two modes")
        labels = re.findall(r"^\*\*([A-Za-z]+)\.\*\*", body, re.M)
        self.assertEqual(labels, ["Strict", "Human"])

    def test_precedence_order(self):
        """SCN-SKILL-002-1"""
        # Covers: REQ-SKILL-002
        body = section("Order of precedence when rules conflict")
        items = re.findall(r"^\d+\.\s+(\w+)", body, re.M)
        self.assertEqual(items, ["Meaning", "Structure", "Voice", "Shape", "Brevity"])

    def test_output_format(self):
        """SCN-SKILL-003-1"""
        # Covers: REQ-SKILL-003
        body = section("Output format")
        self.assertIn("Kept as-is:", body)
        self.assertIn("nothing else", body)

    def test_word_cap(self):
        """SCN-SKILL-004-1"""
        # Covers: REQ-SKILL-004
        with open(SKILL, encoding="utf-8") as fh:
            self.assertLess(len(fh.read().split()), 1800)

    def test_readme_lints_clean(self):
        """SCN-SKILL-004-2"""
        # Covers: REQ-SKILL-004
        r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "lint.py"),
                            os.path.join(ROOT, "README.md")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertNotIn("\n## Develop", text)
        self.assertTrue(os.path.exists(os.path.join(ROOT, "examples", "before-after.md")))

    def test_clean_archive(self):
        """SCN-SKILL-004-3"""
        # Covers: REQ-SKILL-004
        # --worktree-attributes reads .gitattributes from disk, so the test
        # passes before the file is committed.
        try:
            r = subprocess.run(["git", "archive", "--worktree-attributes", "HEAD"],
                               cwd=ROOT, capture_output=True)
        except OSError:
            self.skipTest("git not available")
        if r.returncode != 0:
            self.skipTest("not a git checkout")
        import io
        import tarfile
        names = tarfile.open(fileobj=io.BytesIO(r.stdout)).getnames()
        for want in ("SKILL.md", "references", "scripts", "examples"):
            self.assertTrue(any(n == want or n.startswith(want + "/") for n in names), want)
        for bad in ("openspec", "tests", ".ctx", ".claude"):
            self.assertFalse(any(n == bad or n.startswith(bad + "/") for n in names), bad)


if __name__ == "__main__":
    unittest.main()
