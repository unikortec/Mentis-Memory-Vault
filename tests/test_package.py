"""Dependency-free, static quality checks for a public, platform-neutral memory skill."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ALL_MD = list(ROOT.rglob("*.md"))
REQUIRED = [
    "SKILL.md", "README.md", "LICENSE",
    "references/INSTALLATION.md", "references/STORAGE.md",
    "references/MEMORY_POLICY.md", "references/HISTORY_AUDIT.md",
    "references/SCHEDULING.md", "references/VALIDATION.md",
    "references/SECURITY.md", "references/PLATFORM_COMPATIBILITY.md",
    "references/RECOVERY_AND_OPERATIONS.md", "references/THREAT_MODEL.md",
    "templates/PERSISTENT_INSTRUCTIONS.md", "templates/INSTALL_REPORT.md",
]
# Identifiers below are *synthetic patterns*. Actual private tokens must never
# be embedded in this repository or its test fixtures.
SUSPECT_PATTERNS = [
    re.compile(r"(?i)\b(sk-proj|sb_secret|ghp|github_pat)_[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"(?i)(?:service_role|access_token|secret_key)\s*[:=]\s*['\"][A-Za-z0-9_-]{25,}"),
    re.compile(r"(?i)(?:postgres(?:ql)?://)[^\s]+:[^\s@]+@"),
]


class PublicSkillTests(unittest.TestCase):
    def test_required_files(self):
        for name in REQUIRED:
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file(), name)

    def test_skill_metadata(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertRegex(skill, r"(?m)^name:\s*mentis-memory-vault\s*$")
        self.assertRegex(skill, r"(?m)^description:\s*\S")
        self.assertIn("Category → Subject/Project → Specific memory", skill)

    def test_relative_markdown_links(self):
        link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for md in ALL_MD:
            for target in link.findall(md.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                clean = target.split("#", 1)[0].split("?", 1)[0]
                if clean:
                    with self.subTest(source=md.relative_to(ROOT), target=clean):
                        self.assertTrue((md.parent / clean).exists())

    def test_security_controls_present(self):
        joined = "\n".join(p.read_text(encoding="utf-8") for p in ALL_MD)
        for keyword in ("RLS", "approval", "read-back", "scheduler", "checkpoint", "Codex"):
            with self.subTest(keyword=keyword):
                self.assertIn(keyword.lower(), joined.lower())

    def test_no_obvious_secrets(self):
        for item in ROOT.rglob("*"):
            if not item.is_file() or ".git" in item.parts or item.suffix not in {".md", ".yml", ".yaml", ".json", ".py", ".txt"}:
                continue
            content = item.read_text(encoding="utf-8")
            for pattern in SUSPECT_PATTERNS:
                with self.subTest(file=str(item.relative_to(ROOT)), pattern=pattern.pattern):
                    self.assertIsNone(pattern.search(content))

    def test_not_shipping_sql_dumps(self):
        self.assertFalse(list(ROOT.rglob("*.sql")))


if __name__ == "__main__":
    unittest.main()
