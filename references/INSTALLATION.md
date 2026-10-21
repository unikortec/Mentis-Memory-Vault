# Guided installation — precise workflow

## A. Capability preflight (no questions yet)
Probe available connectors, authenticated accounts, workspace/files access, project-listing permissions, code workspace, history export access, scheduled tasks / automation facilities, and current persistent-instructions location. Record each as **confirmed**, **not connected**, **permission denied**, or **unsupported**.

If a Supabase project is already available, inspect schema, RLS, permissions, migrations, and existing memory-related objects before creating anything. For Drive, list the intended parent, check write access and name collisions. If existing installation is detected, reconcile; never overwrite by default.

## B. Minimal decisions
Ask just for the necessary choices in normal conversation:
- Where to store: Supabase, Drive or both (or set up later)?
- Can the assistant automatically save **low-risk durable facts** from authorized current conversations, with explicit approval for ambiguous/sensitive material; or should it request approval for every permanent entry?
- If requesting historical analysis, may it use already-connected records and selected coding-agent logs/exports? Honor account/source restrictions.
- Only if scheduled reviews are wanted: daily, weekly, both, custom, none; local time/timezone (discover if available).

Never require a user to reveal a password, token, API key, phone number, address, private identity or other secret for setup.

## C. Account and storage setup
### Supabase route
If project exists, request selection from actual list. If not, offer to create a new private project through authorized connector when supported, or walk the user through creating one in the Supabase dashboard. Explain region/cost/backup/pausing behavior based on currently verified plan terms. Only ask for region/project name when creation requires them and no sensible choice is available.

Generate minimal, idempotent, versioned schema migration **based on the live instance** as specified in STORAGE.md. Review planned tables, RLS, service credentials and costs. Apply through supported migration tools with authorization; verify constraints and tenant isolation using separate test identities or policy tests. Never paste secret keys or ask the user to send them in chat.

### Drive route
Ask for folder only if it can't be discovered/created with permission. Create a private root such as `Memory Vault` and category index Markdown files. Use stable file IDs and a manifest; storage is viable without any database. Never assume Google Drive supports full-text, relational queries or atomic transactions like Postgres.

### Dual route
Set the selected primary source explicitly. Store `storage_provider`, `external_file_id`, `content_hash`, `revision`, and `last_verified_at` metadata. Reconcile conflicts; never silently choose latest timestamps over deliberate decisions.

## D. Persistent agent setup
Detect first-party instructions/skills/project settings or writable agent config. Present change summary. Install template with least privilege, linking to storage and consent settings, then verify across a fresh authorized execution/context if possible.

In ChatGPT: use supported user-managed Custom Instructions, project instructions, installed Skills or other officially supported persistence where available. In Claude: use native Skills/project instructions or CLAUDE.md for coding environments. In Codex: use supported Skills/AGENTS.md in the intended scope. Do not assume chat instructions modify permanent global behavior.

## E. Finalization
Perform dry-run classification and dedupe; authorized write/read test; link integrity; index search; backup/recovery; schedule verification if requested. Issue manifest/report. Install success = confirmed persistence + authorized storage read/write + reporting.

Do not call this "one click" or "100% automatic" if platform capabilities are missing.
