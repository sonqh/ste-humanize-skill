"""One pin of the spec engine, one pin of OpenSpec, and one list of markdown globs."""
# Covers: REQ-SKILL-013, REQ-SKILL-014
import os
import re
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = "scripts/specctx.sh"
CALLERS = [".githooks/pre-commit", ".githooks/pre-push", "scripts/ci-local.sh", ".github/workflows/ci.yml"]
HISTORY = ("openspec/changes/archive/", ".ctx/evidence/", "docs/verification/", "docs/releases/", "evals/runs/")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def tracked():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8").split("\0") if p]


def gate_section():
    m = re.search(r"^\[gate\]\s*$(.*?)(?=^\[|\Z)", read("spec-ctx.toml"), re.M | re.S)
    assert m, "spec-ctx.toml has no [gate] section"
    return m.group(1)


def toml_markdown():
    line = re.search(r"^markdown\s*=\s*\[(.*?)\]", gate_section(), re.M | re.S)
    assert line, "[gate] has no markdown key"
    return re.findall(r'"([^"]*)"', line.group(1))


class EnginePinTests(unittest.TestCase):
    def test_one_pin(self):
        """SCN-SKILL-013-1"""
        # Covers: SCN-SKILL-013-1
        text = read(PIN)
        pins = re.findall(r"^SPECCTX_VERSION=(\S+)$", text, re.M)
        self.assertEqual(len(pins), 1, pins)
        self.assertRegex(pins[0], r"^\d+\.\d+\.\d+$")
        self.assertRegex(text, r'(?m)^exec npx -y "spec-ctx@\$SPECCTX_VERSION" "\$@"$')

    def test_no_second_pin(self):
        """SCN-SKILL-013-2"""
        # Covers: SCN-SKILL-013-2
        offenders = []
        for rel in tracked():
            if rel == PIN or rel.startswith(HISTORY):
                continue
            try:
                text = read(rel)
            except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
                continue
            if re.search(r"spec-ctx@\d|SPECCTX_VERSION=\d", text):
                offenders.append(rel)
        self.assertEqual(offenders, [])
        for rel in CALLERS:
            text = read(rel)
            self.assertNotRegex(text, r"npx[^\n]*spec-ctx", rel)
        for rel in [".githooks/pre-commit", "scripts/ci-local.sh", ".github/workflows/ci.yml"]:
            self.assertIn("scripts/specctx.sh", read(rel), rel)

    def test_one_markdown_list(self):
        """SCN-SKILL-013-3"""
        # Covers: SCN-SKILL-013-3
        want = toml_markdown()
        self.assertTrue(want)
        lists = {
            ".githooks/pre-commit": re.search(r'--markdown "([^"]*)"', read(".githooks/pre-commit")),
            "scripts/ci-local.sh": re.search(r'--markdown "([^"]*)"', read("scripts/ci-local.sh")),
            ".github/workflows/ci.yml": re.search(r'specctx: bash scripts/specctx\.sh[\s\S]*?markdown: "([^"]*)"',
                                                  read(".github/workflows/ci.yml")),
        }
        for rel, m in lists.items():
            self.assertIsNotNone(m, rel)
            self.assertEqual(m.group(1).split(), want, rel)


OPENSPEC_PIN = "scripts/openspec.sh"
SPECCTX_SKILLS = (".claude/skills/specctx-", ".agents/skills/specctx-")


class OpenSpecPinTests(unittest.TestCase):
    def test_one_openspec_pin(self):
        """SCN-SKILL-014-1"""
        # Covers: SCN-SKILL-014-1
        text = read(OPENSPEC_PIN)
        pins = re.findall(r"^OPENSPEC_VERSION=(\S+)$", text, re.M)
        self.assertEqual(len(pins), 1, pins)
        self.assertRegex(pins[0], r"^\d+\.\d+\.\d+$")
        self.assertRegex(text, r'(?m)^exec npx -y "@fission-ai/openspec@\$OPENSPEC_VERSION" "\$@"$')
        line = re.search(r'^openspec\s*=\s*"([^"]*)"', gate_section(), re.M)
        self.assertIsNotNone(line, "[gate] has no openspec key")
        self.assertEqual(line.group(1), "bash scripts/openspec.sh")

    def test_no_second_openspec_pin(self):
        """SCN-SKILL-014-2"""
        # Covers: SCN-SKILL-014-2
        offenders = []
        for rel in tracked():
            if rel.startswith(HISTORY) or rel.startswith(SPECCTX_SKILLS):
                continue
            try:
                text = read(rel)
            except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
                continue
            if re.search(r"@fission-ai/openspec@(\d|latest)", text):
                offenders.append(rel)
        self.assertEqual(offenders, [])

    def test_stock_schema(self):
        """SCN-SKILL-014-3"""
        # Covers: SCN-SKILL-014-3
        self.assertRegex(read("openspec/config.yaml"), r"(?m)^schema: spec-driven$")
        files = tracked()
        self.assertEqual([p for p in files if p.startswith("openspec/schemas/")], [])
        for name in ("spec.md", "tasks.md"):
            self.assertIn("openspec/templates/spec-driven-ids/" + name, files)


def openspec_skills(base):
    folder = os.path.join(ROOT, base)
    return sorted(n for n in os.listdir(folder) if n.startswith("openspec-"))


class OpenSpecSkillTests(unittest.TestCase):
    def test_skills_match_pin(self):
        """SCN-SKILL-015-1"""
        # Covers: REQ-SKILL-015, SCN-SKILL-015-1
        pin = re.search(r"^OPENSPEC_VERSION=(\S+)$", read(OPENSPEC_PIN), re.M).group(1)
        names = openspec_skills(".agents/skills")
        self.assertTrue(names)
        for name in names:
            m = re.search(r'^\s*generatedBy:\s*"([^"]+)"', read(".agents/skills/%s/SKILL.md" % name), re.M)
            self.assertIsNotNone(m, name)
            self.assertEqual(m.group(1), pin, name)

    def test_one_copy_of_each_skill(self):
        """SCN-SKILL-015-2"""
        # Covers: SCN-SKILL-015-2
        links = openspec_skills(".claude/skills")
        self.assertEqual(links, openspec_skills(".agents/skills"))
        for name in links:
            path = os.path.join(ROOT, ".claude/skills", name)
            self.assertTrue(os.path.islink(path), name)
            self.assertEqual(os.readlink(path), "../../.agents/skills/" + name)

    def test_no_opsx_commands(self):
        """SCN-SKILL-015-3"""
        # Covers: SCN-SKILL-015-3
        self.assertEqual([p for p in tracked() if p.startswith(".claude/commands/opsx/")], [])


if __name__ == "__main__":
    unittest.main()
