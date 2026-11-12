"""One pin of the spec engine and one list of markdown globs."""
# Covers: REQ-SKILL-013
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


def toml_markdown():
    text = read("spec-ctx.toml")
    m = re.search(r"^\[gate\]\s*$(.*?)(?=^\[|\Z)", text, re.M | re.S)
    assert m, "spec-ctx.toml has no [gate] section"
    line = re.search(r"^markdown\s*=\s*\[(.*?)\]", m.group(1), re.M | re.S)
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


if __name__ == "__main__":
    unittest.main()
