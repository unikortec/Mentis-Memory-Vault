# Mentis Memory Vault — Universal AI Memory Skill

**Version 3.0** · Universal, privacy-first, user-controlled memory for ChatGPT, Claude, Codex, Claude Code and compatible AI agents.

This is a portable **agent skill**, not a hosted database or a tool that can secretly read all conversations. It provides an assisted installer and a verifiable operating protocol.

## One-prompt installation

Copy and paste this message into your preferred AI assistant:

> Install the complete **Mentis Memory Vault** skill from https://github.com/unikortec/Mentis-Memory-Vault . Read the root **SKILL.md**, follow all referenced instructions, and guide the installation using your available tools. First check capabilities and existing installations. Ask me only for essential choices and authorizations. Offer **Supabase only, Google Drive only, or both**, and configure the desired persistent memory instructions, consent-based automatic capture, accessible conversation / coding-agent history audit, and verified optional daily/weekly/monthly schedules. Do not include third-party or developer information in my memory. Do not assert access to histories, background scheduling, successful writes or fully completed installation without proof. Produce a final installation and validation report. If you cannot access this GitHub repository or install native Skills, explain the limitation and request that I upload the repository ZIP.

**The AI needs web/GitHub access** to retrieve the skill; text alone does not bypass platform restrictions. If your environment has no repository access, [download this repository as ZIP](https://github.com/unikortec/Mentis-Memory-Vault/archive/refs/heads/main.zip), attach it, and reuse the prompt.

## Options

- **Supabase:** structured, relational memory; generates instance-specific schema/migrations during installation (no prepackaged SQL).
- **Google Drive:** private Markdown files, index and manifest; no Supabase required.
- **Both:** cross-store mapping, verified read-backs and conflict reconciliation.

Persistent instructions are installed only where the platform supports them and where the user has authorized writes. Scheduled jobs are created and verified **only if the environment exposes a compatible scheduling facility**.

## Start here

- [SKILL.md](SKILL.md) — authoritative instructions for AI agents
- [Installation](references/INSTALLATION.md)
- [Storage architecture (without bundled SQL)](references/STORAGE.md)
- [Privacy and security](references/SECURITY.md)
- [Memory classification and auto-capture](references/MEMORY_POLICY.md)
- [History and coding-agent audit](references/HISTORY_AUDIT.md)
- [Scheduling](references/SCHEDULING.md)
- [Validation and rollback](references/VALIDATION.md)
- [Persistent-instructions template](templates/PERSISTENT_INSTRUCTIONS.md)
- [Installation-report template](templates/INSTALL_REPORT.md)

## Non-negotiable safeguards

No personal data, account IDs, secrets or private vault dumps belong in this public repository. Do not automatically ingest inaccessible ChatGPT/Claude/Codex histories or treat Git commits as full conversation transcripts. Auto-save must respect explicit consent boundaries; sensitive and uncertain information requires review. Production writes require least privilege, backups and verification. Never claim autonomous background processing without a verified scheduler.

License: [MIT](LICENSE).

## Professional QA and go-live status

- [Platform capability matrix](references/PLATFORM_COMPATIBILITY.md)
- [Recovery, idempotency and operations](references/RECOVERY_AND_OPERATIONS.md)
- [Threat model and public distribution gates](references/THREAT_MODEL.md)
- [Static test suite](tests/test_package.py) · [GitHub Actions workflow](.github/workflows/skill-quality.yml)

**Status:** source package published; real fresh-account ChatGPT/Claude installation, two-principal Supabase RLS, Google Drive ACL, dual-store conflict and scheduled-job execution **not yet certified**. Passing GitHub CI validates repository structure only. No claim of universal zero-touch setup.
