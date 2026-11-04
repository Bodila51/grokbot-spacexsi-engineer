# Dean Rie (@dean_rie)
- Role / team: Cursor forum staff (flair CursorStaff, admin/moderator), SpaceXSI x Cursor; answers Grok Bot questions ([source](https://forum.cursor.com/u/deanrie))
- Links: [X](https://x.com/dean_rie), [forum](https://forum.cursor.com/u/deanrie)
- Confidence: high
## Key ideas
- Never paste passwords or credentials into the chat; use the masked secret request — [forum thread](https://forum.cursor.com/t/confused-over-grok-bot/171745.md?page=2) (2026-10-13)
- For payments choose "Allow once", not "Always allow" — same thread (2026-10-13)
- Windows: run `agent update` then `agent worker start` (crash fixed in Cursor Agent CLI 2026.10.16+; needs Git for Windows, no WSL); "My Machines" is closest to local execution — same thread (2026-10-19)
- Grok Bot is for tasks outside the editor and hands coding to Cursor cloud agents — [forum thread](https://forum.cursor.com/t/confused-over-grok-bot/171745.md)
- Security docs: bots act as the signed-in member, secrets are masked, approvals are Allow once / Always / Deny, Auto Review exists, "Never allow" recommended for local execution — [docs](https://cursor.com/docs/grok-bot/security)
- Get-started docs: state lasting preferences in the first message; save a stable process as a skill or routine — [docs](https://cursor.com/docs/grok-bot/get-started)
## Bots, skills, plugins
- No bots or repos; guidance only (docs above).
## Copy this in Grok Bot
1. Enter secrets only through the masked secret request, never in chat.
2. Use "Allow once" for payments and consider "Never allow" for local execution.
3. Put lasting preferences in your first message to a new bot; save stable processes as skills or routines.
4. On Windows, if local runs crash, update the Cursor agent CLI with `agent update`, then `agent worker start`.
## Sources
- https://x.com/dean_rie
- https://forum.cursor.com/u/deanrie
- https://forum.cursor.com/t/confused-over-grok-bot/171745
- https://cursor.com/docs/grok-bot/security
- https://cursor.com/docs/grok-bot/get-started
