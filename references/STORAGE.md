# Storage architecture specification (no bundled SQL)

## Minimal canonical model
Every memory must have:
- Stable opaque `id`
- `category`: person, company, project, decision, preference, context, reference, idea, system; extensible
- `subject`: durable project/entity grouping
- `title`, `summary`, `body`
- `status`: candidate, permanent, temporary, archived, rejected
- `fact_kind`: confirmed, user-reported, decision, plan, hypothesis, estimate, historical
- `confidence`: evidence confidence on 0..1, **separate** from review priority 0..100
- `source`: kind, locator, timestamp, access scope, immutable evidence pointer when available
- `created_at`, `updated_at`, `reviewed_at`
- `owner_scope` or tenant identity enforced server-side
- `version`, `tags`, `links`
- `storage_provider`, `external_file_id`, `content_hash` (as appropriate)

## Recommended tables (agent should generate)
`memories`, `memory_versions`, `entities`, `memory_links`, `capture_candidates`, `audit_runs`, `audit_sources`, `sync_state`, `jobs` or `schedule_receipts`. Avoid tables not required by chosen features. JSON metadata should not be a replacement for ownership, indexes, foreign keys and RLS.

### Supabase security
- Prefer isolated new project for unrelated users rather than putting public user memory into one shared developer project.
- Every user-scoped row requires ownership policy enforced by PostgreSQL RLS, not frontend-only filtering.
- No anonymous write or public bucket for personal memory.
- Storage objects private and user-scoped.
- Schema migrations transactionally and versioned with dry-run when supported; incremental rollout and rollback path.
- Confirm RLS on every exposed table and run negative cross-user access tests.
- Detect project configuration and table conflicts before mutation.

### Drive-only security
- Private root; check sharing and ACLs.
- Markdown frontmatter (id/category/subject/source/status/version) + content sections.
- `index.json` / `manifest.json` mapping IDs, filenames, checksums; `audit-log.ndjson` and backups.
- Link by canonical IDs, not only filenames; resolve broken links on rename.
- Since Drive updates are not transactional, use staged writes and a commit manifest/checkpoint; resume after partial failure.

### Dual syncing
- Never mark synced until both sides confirm read-back and hashes.
- Explicit primary preference and conflict policy. Retain both versions for conflicting edits.
- Idempotency keys for imports; no blind overwrite.

### Backups and retention
User chooses retention and restore location. Backup before migration; test restoration with non-sensitive fixtures. Allow deletion/export; propagate deletions across configured stores after explicit confirmation. An export is personal/private even if this skill is public.

**No ready-made SQL in the package.** The installer agent generates suitable migrations from this contract within the authorized selected Supabase project.
