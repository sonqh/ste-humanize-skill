import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "SKILL.md")
DOC_SHAPES = os.path.join(ROOT, "references", "doc-shapes.md")
PAGE_GUIDES = os.path.join(ROOT, "references", "page-guides.md")


HUMAN = os.path.join(ROOT, "references", "human.md")
TERMS = os.path.join(ROOT, "references", "terms.md")


def section(name, path=SKILL):
    with open(path, encoding="utf-8") as fh:
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
        for want in ("Kept as-is:", "Cut candidates:", "Reader:", "nothing else"):
            self.assertIn(want, body)
        # SCN-SKILL-003-2
        self.assertIn("only when the request does not name the reader", body)
        self.assertIn("add no `Reader:` line", section("Reader first"))

    def test_word_cap(self):
        """SCN-SKILL-004-1"""
        # Covers: REQ-SKILL-004
        with open(SKILL, encoding="utf-8") as fh:
            self.assertLess(len(fh.read().split()), 1900)

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
        for bad in ("openspec", "tests", ".ctx", ".claude", "evals"):
            self.assertFalse(any(n == bad or n.startswith(bad + "/") for n in names), bad)


class AudienceFitTest(unittest.TestCase):
    # Covers: REQ-SKILL-006

    def test_reader_first(self):
        # Covers: SCN-SKILL-006-1
        sec = section("Audience fit", HUMAN)
        self.assertIn("Human mode only", sec)
        self.assertIn("already know", sec)
        self.assertIn("complete a task", sec)

    def test_appendices(self):
        # Covers: SCN-SKILL-006-2
        sec = section("Audience fit", HUMAN)
        self.assertIn("appendices", sec)
        self.assertIn("collapsed sections", sec)

    def test_source_and_links(self):
        # Covers: SCN-SKILL-006-3
        sec = section("Audience fit", HUMAN)
        self.assertIn("against the source code", sec)
        self.assertIn("link text", sec)

    def test_conditions_survive_identifiers_exact(self):
        # Covers: SCN-SKILL-006-4
        item1 = re.search(r"^1\.\s+Meaning\..*$", section("Order of precedence when rules conflict"), re.M).group(0)
        self.assertIn("condition", item1)
        self.assertIn("exception", item1)
        terms = section("Technical terms and other languages", TERMS)
        self.assertIn("Audience fit", terms)
        self.assertIn("Strict mode", terms)

    def test_one_event_per_bullet(self):
        # Covers: SCN-SKILL-006-5
        sec = section("Shape: fit the content")
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

    def _section(self, title, path=SKILL):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        start = text.index(title)
        end = text.find("\n## ", start + 1)
        return text[start:end if end > 0 else None]

    def test_section_and_order(self):
        # Covers: SCN-SKILL-005-1
        sec = self._section("## A page for a newcomer", DOC_SHAPES)
        items = [l for l in sec.splitlines() if l[:2] in ("1.", "2.", "3.", "4.", "5.")]
        self.assertEqual(len(items), 5)
        self.assertIn("base thing", items[0])
        self.assertIn("try it", items[4])

    def test_caption_rule(self):
        # Covers: SCN-SKILL-005-2
        sec = self._section("## A page for a newcomer", DOC_SHAPES)
        self.assertIn("what the reader sees", sec)
        self.assertIn("does not repeat the command", sec)
        self.assertIn("references/doc-shapes.md", self._section("## Reader first"))

    def test_numbers_need_scale(self):
        # Covers: SCN-SKILL-005-3
        self.assertIn("scale the reader has", self._section("## Boundaries"))


def precedence_item_1():
    return re.search(r"^1\.\s+Meaning\..*$",
                     section("Order of precedence when rules conflict"), re.M).group(0)


class TwoTasksTest(unittest.TestCase):
    # Covers: REQ-SKILL-008

    def test_header_and_names(self):
        # Covers: SCN-SKILL-008-1
        labels = re.findall(r"^\*\*([A-Za-z]+)\.\*\*", section("Two tasks"), re.M)
        self.assertEqual(labels, ["Rewrite", "Write"])

    def test_rewrite_keeps_source(self):
        # Covers: SCN-SKILL-008-2
        sec = section("Two tasks")
        self.assertIn("Cut candidates:", sec)
        self.assertIn("source is the truth", sec)

    def test_limits_of_a_write(self):
        # Covers: SCN-SKILL-008-3
        sec = section("Two tasks")
        self.assertIn("safety condition", sec)
        self.assertIn("exception", sec)
        self.assertIn("Write task", precedence_item_1())


class ReaderFirstTest(unittest.TestCase):
    # Covers: REQ-SKILL-009

    def test_brief_of_three_questions(self):
        # Covers: SCN-SKILL-009-1
        sec = section("Reader first")
        self.assertEqual(re.findall(r"^(\d+)\.\s", sec, re.M), ["1", "2", "3"])
        self.assertIn("reader brief", sec)

    def test_answer_first_and_stop_rule(self):
        # Covers: SCN-SKILL-009-2
        sec = section("Reader first")
        self.assertIn("Answer first", sec)
        self.assertIn("reader can act", sec)

    def test_act_first(self):
        # Covers: SCN-SKILL-009-5
        with open(DOC_SHAPES, encoding="utf-8") as fh:
            self.assertIn("The first task comes before the reference", fh.read())

    def test_kinds_of_page(self):
        # Covers: SCN-SKILL-009-3
        self.assertIn("references/doc-shapes.md", section("Reader first"))
        with open(DOC_SHAPES, encoding="utf-8") as fh:
            rows = [l.split("|")[1].strip() for l in fh if l.startswith("|")]
        for page in ("README", "How-to guide", "Reference page", "Design note",
                     "PR description", "Runbook"):
            self.assertIn(page, rows)

    def test_process_names_the_brief(self):
        # Covers: SCN-SKILL-009-4
        step1 = re.search(r"^1\.\s.*$", section("Process"), re.M).group(0)
        self.assertIn("reader brief", step1)
        self.assertIn("task", step1)


class ShapeFitsContentTest(unittest.TestCase):
    # Covers: REQ-SKILL-010

    def test_table_of_shapes(self):
        # Covers: SCN-SKILL-010-1
        cells = [l.split("|")[2].strip() for l in section("Shape: fit the content").splitlines()
                 if l.startswith("|")]
        for shape in ("Bullets", "Numbered list", "Table"):
            self.assertIn(shape, cells)
        self.assertTrue(any(c.startswith("Prose") for c in cells), cells)

    def test_signs(self):
        # Covers: SCN-SKILL-010-2
        sec = section("Shape: fit the content")
        self.assertIn("more than 6 sentences", sec)
        self.assertIn("5 or more items", sec)

    def test_reasoning_stays_prose(self):
        # Covers: SCN-SKILL-010-3
        self.assertIn("Do not cut reasoning into bullets", section("Shape: fit the content"))
        with open(SKILL, encoding="utf-8") as fh:
            headers = re.findall(r"^## (.*)$", fh.read(), re.M)
        self.assertNotIn("Shape: bullets first", headers)


class RouterTest(unittest.TestCase):
    # Covers: REQ-SKILL-011

    def _skill(self):
        with open(SKILL, encoding="utf-8") as fh:
            return fh.read()

    def test_every_reference_is_routed(self):
        # Covers: SCN-SKILL-011-1
        table = [l for l in section("What to read").splitlines() if l.startswith("|")]
        self.assertGreaterEqual(len(table), 4)
        routed = set(re.findall(r"`references/([\w-]+\.md)`", "\n".join(table)))
        on_disk = set(os.listdir(os.path.join(ROOT, "references")))
        self.assertEqual(routed, on_disk)

    def test_no_dead_reference(self):
        # Covers: SCN-SKILL-011-2
        files = [SKILL] + [os.path.join(ROOT, "references", n)
                           for n in os.listdir(os.path.join(ROOT, "references"))]
        for path in files:
            with open(path, encoding="utf-8") as fh:
                for name in re.findall(r"`((?:references|scripts)/[\w./-]+)`", fh.read()):
                    self.assertTrue(os.path.exists(os.path.join(ROOT, name)), f"{path}: {name}")

    def test_reference_says_when_to_read_it(self):
        # Covers: SCN-SKILL-011-3
        for name in ("human.md", "terms.md", "doc-shapes.md", "page-guides.md"):
            with open(os.path.join(ROOT, "references", name), encoding="utf-8") as fh:
                head = "".join(fh.readlines()[:4])
            self.assertIn("Read this file when", head, name)

    def test_moved_sections_live_in_one_place(self):
        # Covers: SCN-SKILL-011-4
        headers = re.findall(r"^## (.*)$", self._skill(), re.M)
        for moved in ("Voice", "Audience fit", "Humanizer patterns",
                      "Technical terms and other languages"):
            self.assertNotIn(moved, headers)
        self.assertEqual(len(headers), len(set(headers)))
        step1 = re.search(r"^1\.\s.*$", section("Process"), re.M).group(0)
        self.assertIn("What to read", step1)


class PageGuidesTest(unittest.TestCase):
    # Covers: REQ-SKILL-012

    def _doc(self, name):
        path = DOC_SHAPES if name == "Reader questions" else PAGE_GUIDES
        return section(name, path)

    def test_reader_questions(self):
        # Covers: SCN-SKILL-012-1
        sec = self._doc("Reader questions")
        self.assertEqual(len(re.findall(r"^\d+\.\s", sec, re.M)), 6)
        self.assertIn("cut candidate", sec)
        self.assertIn("first paragraph, and the headings", sec)

    def test_three_guides(self):
        # Covers: SCN-SKILL-012-2
        for name in ("README", "ADR", "Technical proposal"):
            sec = self._doc(name)
            self.assertIn("Readers:", sec, name)
            self.assertGreaterEqual(len(re.findall(r"^\d+\.\s", sec, re.M)), 6, name)
            self.assertIn("\nTest: ", sec, name)

    def test_table_rows_and_template_rule(self):
        # Covers: SCN-SKILL-012-3
        with open(DOC_SHAPES, encoding="utf-8") as fh:
            text = fh.read()
        rows = [l.split("|")[1].strip() for l in text.splitlines() if l.startswith("|")]
        self.assertIn("ADR", rows)
        self.assertIn("Technical proposal", rows)
        self.assertIn("keep its headings and their order", text)

    def test_skill_names_the_questions(self):
        # Covers: SCN-SKILL-012-4
        self.assertIn("questions the reader brings", section("Reader first"))
        tasks = section("Two tasks")
        self.assertIn("A Rewrite may move a part", tasks)
        self.assertIn("removes none", tasks)
        routes = section("What to read")
        self.assertIn("Rewrite of a whole page", routes)
        self.assertIn("a README, an ADR, or a technical proposal", routes)

