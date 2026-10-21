# End-to-end verification, recovery and delivery gates

## Install quality gates
- Source repo trusted and skill fully read, no suspicious instructions from unrelated files.
- Requested storage connected with **actual** scopes/permissions.
- Test user identity and tenant isolation, including denied unauthorized read/write.
- Upsert one synthetic fixture, read it, link it, search it, update/version it, export it; then archive/delete fixture with user authorization or safe test cleanup.
- Verify folder/index or DB constraints, metadata, cross-links, hashes and latest change receipts.
- Test idempotency (re-running import does not duplicate).
- In dual mode, mutate a test value on one side, sync, read back, and simulate conflicting edits to ensure neither is silently lost.
- Perform safe backup and sample restore to isolated test scope.
- Verify persistent instructions installed in correct platform scope. If only copy-ready instructions, label `manual_pending`.
- If scheduling chosen, obtain task ID/read-back and validate connector context; else label `not_configured`.
- Perform history audit dry run with source inventory and coverage ledger.
- Check secret scanning and no private content in public repository.
- Preserve preexisting records, backup and migration history.

## Recoverable phases
`PRECHECK → CONSENT → STORAGE → INSTRUCTIONS → HISTORY → SCHEDULE → VERIFY → COMPLETE`. Checkpoint per phase. Resume safely; don't duplicate. If a step fails, mark partial, provide rollback/resume instructions.

## Status classification
- `COMPLETE`: all requested capabilities verified end-to-end.
- `PARTIAL`: core setup works, optional or requested integration incomplete.
- `MANUAL_REQUIRED`: platform lacks write capability or owner action still needed.
- `BLOCKED`: security/authorization prevents safe continuation.

Never fake success. A single read/write in one account does not prove multi-user RLS. Do not test production by indiscriminate deletion.
