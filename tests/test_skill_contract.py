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
            self.assertLess(len(fh.read().split()), 2400)

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


class AudienceFitTest(unittest.TestCase):
    # Covers: REQ-SKILL-006

    def test_reader_first(self):
        # Covers: SCN-SKILL-006-1
        sec = section("Audience fit")
        self.assertIn("Human mode only", sec)
        self.assertIn("already know", sec)
        self.assertIn("complete a task", sec)

    def test_appendices(self):
        # Covers: SCN-SKILL-006-2
        sec = section("Audience fit")
        self.assertIn("appendices", sec)
        self.assertIn("collapsed sections", sec)

    def test_source_and_links(self):
        # Covers: SCN-SKILL-006-3
        sec = section("Audience fit")
        self.assertIn("against the source code", sec)
        self.assertIn("link text", sec)

    def test_conditions_survive_identifiers_exact(self):
        # Covers: SCN-SKILL-006-4
        item1 = re.search(r"^1\.\s+Meaning\..*$", section("Order of precedence when rules conflict"), re.M).group(0)
        self.assertIn("condition", item1)
        self.assertIn("exception", item1)
        terms = section("Technical terms and other languages")
        self.assertIn("Audience fit", terms)
        self.assertIn("Strict mode", terms)

    def test_one_event_per_bullet(self):
        # Covers: SCN-SKILL-006-5
        sec = section("Shape: bullets first")
        self.assertIn("one event", sec)
        self.assertIn("Independent rules", sec)


class PluginMarketplaceTest(unittest.TestCase):
    # Covers: REQ-SKILL-007

    def _json(self, name):
        import json
        with open(os.path.join(ROOT, ".claude-plugin", name), encoding="utf-8") as fh:
            return json.load(fh)

    def _front(self, key):
        with open(SKILL, encoding="utf-8") as fh:
            head = fh.read().split("---", 2)[1]
        return re.search(r"^" + key + r":\s*(\S+)\s*$", head, re.M).group(1)

    def test_names_match(self):
        # Covers: SCN-SKILL-007-1
        plugin = self._json("plugin.json")
        entries = self._json("marketplace.json")["plugins"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(plugin["name"], self._front("name"))
        self.assertEqual(entries[0]["name"], plugin["name"])
        self.assertEqual(entries[0]["source"], "./")

    def test_versions_match(self):
        # Covers: SCN-SKILL-007-2
        version = self._json("plugin.json")["version"]
        self.assertEqual(version, self._front("version"))
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def test_validate_passes(self):
        # Covers: SCN-SKILL-007-3
        import shutil
        if shutil.which("claude") is None:
            self.skipTest("claude CLI not on the path")
        r = subprocess.run(["claude", "plugin", "validate", "--strict", "."], cwd=ROOT,
                           capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()


class NewcomerShapeTest(unittest.TestCase):
    # Covers: REQ-SKILL-005

    def _section(self, title):
        with open(SKILL, encoding="utf-8") as fh:
            text = fh.read()
        start = text.index(title)
        end = text.find("\n## ", start + 1)
        return text[start:end if end > 0 else None]

    def test_section_and_order(self):
        # Covers: SCN-SKILL-005-1
        sec = self._section("## Shape: a page for a newcomer")
        items = [l for l in sec.splitlines() if l[:2] in ("1.", "2.", "3.", "4.", "5.")]
        self.assertEqual(len(items), 5)
        self.assertIn("base thing", items[0])
        self.assertIn("try it", items[4])

    def test_caption_rule(self):
        # Covers: SCN-SKILL-005-2
        sec = self._section("## Shape: a page for a newcomer")
        self.assertIn("what the reader sees", sec)
        self.assertIn("does not repeat the command", sec)

    def test_numbers_need_scale(self):
        # Covers: SCN-SKILL-005-3
        self.assertIn("scale the reader has", self._section("## Boundaries"))

