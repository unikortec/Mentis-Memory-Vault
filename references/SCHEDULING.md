# Scheduling — create only when actually requested

At setup offer: **none, daily, weekly, both, monthly deep, custom**. Ask for timezone and preferred local time only if not resolved from user context / scheduler. Display exact times, avoid inventing times the user did not specify, and distinguish flexible from exact.

## Job recipes
### Daily memory health
“Check authorized Vault storage availability, indexes, backups and pending sync; examine newly accessible authorized sources since the last successful checkpoint, generate candidate suggestions under the configured policy, auto-promote only explicitly permitted low-risk facts, and report failures or actionable changes. Do not expose secrets or raw personal logs.”

### Weekly review
“Review accessible authorized chat and coding-agent history since the previous checkpoint, identify missing/stale/contradictory memories, dedupe and rank candidate updates, request approval when needed, verify configured storage read-backs and send a concise audit report, including coverage limitations.”

### Monthly deep audit (optional)
“Re-run historical coverage inventory across all authorized accessible sources, review permissions, reconcile memory versions, test recovery, and report omissions with evidence. Never assume unavailable histories were scanned.”

## Platform instructions
1. Detect if platform provides an actual scheduled-task API, native automation, OS scheduler, cron, CI or authorized hosted worker.
2. Favor the platform's native scheduler for user-facing updates. Create job **only** with user's approval.
3. In prompt-only or skill-only environments, **do not** say job created. Offer exact copy-paste configuration and instructions for the platform.
4. Bind scheduled tasks to the **same user-approved connectors / identity**, least-privilege read/write scopes, and durable checkpoints. Scheduling a reminder to run without storage access is not an automatic audit.
5. Verify creation using returned task ID and schedule read-back; test a run where supported, log `last_successful_run`, and explicitly report missing connector scope.
6. Always provide pause/disable/delete steps or actions. Respect task quota/frequency limits and local timezone/daylight changes.
7. For periodic user notifications with no change, use the user's selected verbosity/delivery preference.
8. If background execution requires subscription, account, authentication or a hosted runtime, describe this before promising full automation.

## Setup receipt
Record scheduler provider, job ID, time zone, cadence, next expected run (when provider supplies it), capability list and test result. Do not fabricate job IDs or runs.
