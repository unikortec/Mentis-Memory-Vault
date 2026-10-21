# Platform capability contract

Do not infer tool access from model names, plan names or app logos. Each capability must be probed and marked **verified / available but untested / manual-only / unsupported**.

| Capability | ChatGPT chat | ChatGPT Work/Codex | Claude chat | Claude Code |
|---|---|---|---|---|
| Read a public GitHub repository | Depends on tools/web | Depends on connectors/browser | Depends on web/connector access | Depends on sandbox/network |
| Install native persistent skill | Depends on account features | Depends on workspace configuration | Depends on current skills UI | Usually project/user skills when writable |
| Persist user-wide instructions | Often user-managed settings | Depends on workspace/project | Often user-managed settings | Project/user configuration files with authorization |
| Access complete historical chats | Not implied | Not implied | Not implied | Not implied |
| Read coding-agent local logs | Not implied | Only with authorized workspace/files | Not implied | Only with authorized filesystem |
| Create actual scheduled job | Native scheduler only if available | Scheduler/cron if authorized | Platform-dependent | OS/CI/hosted scheduler if configured |
| Run continuously without hosted service | No | No | No | No |

This is a **capability matrix, not a representation of platform entitlements**. Verify the platform's up-to-date user documentation and runtime permissions.

## Full automation truth test

1. Does the agent have programmatic permission to write its selected store?
2. Are persistent instructions actually installed and re-read in a new supported context?
3. Can a fresh conversation trigger capture without manually pasting the skill again?
4. Does a real scheduled execution have usable credentials, storage reachability, user identity and durable checkpoints?
5. Is the user informed and able to pause/revoke?
6. Is access to private conversations explicitly supported by the provider, or only to exported/uploaded files?

If **any** requirement fails, report the corresponding feature as `MANUAL_REQUIRED` or `PARTIAL`. Never claim “automatic in every conversation” on the basis of a text instruction alone.
