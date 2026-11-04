# Known issues (Grok Bot)
Built 2026-11-04 only from data we already had: data/posts.jsonl, kb/changelog.md, kb/features.md, kb/people/. Nothing invented; (?) = unclear/unconfirmed.
**Maintenance:** daily-scan appends new bugs/fixes here (new items only, next KI id; update a status only when a source says so). Used by the bug-or-me skill.
Status: open / fixed in vX.Y.Z / unclear (?).

| id | area | symptom (user words) | status | workaround | source | date |
|---|---|---|---|---|---|---|
| KI-001 | iOS app | "the iOS app freezes on the first screen at launch" | unclear (?) — root cause known and a fix was in progress on 2026-08-18; no changelog line confirms a fix | turn off the Apple accessibility setting "show borders" | https://x.com/lingxi/status/2089591569146138850 | 2026-08-18 |
| KI-002 | Voice | "voice mode is gone / disabled" | unclear (?) — temporarily disabled for everyone to fix an issue, re-enable promised "pretty soon"; no post confirming re-enable in kb | wait; use text chat or voice notes | https://x.com/lingxi/status/2107554521346101325 | 2026-10-06 |
| KI-003 | Sign-in / access | "can't get access with my Cursor/SuperGrok subscription" | unclear (?) — team "sprinting to fix auth issues"; no fix line found | report to @egavrilenko11 or in-app Send Feedback | https://x.com/egavrilenko11/status/2094877365419889055 | 2026-09-01 |
| KI-004 | Chat / languages | "right-to-left text (Arabic, Hebrew) looks broken" | fixed in v0.26.0 (right-to-left typing), poteto: "much less broken now" | update the app | https://x.com/poteto/status/2092700749730140284 · https://x.ai/changelog/bot | 2026-08-25/26 |
| KI-005 | Composer | "typing / pops up the skills menu" | fixed in v0.68.1 | update the app | https://x.ai/changelog/bot (v0.68.1) | 2026-10-07 |
| KI-006 | Vault / payments | "does a saved Vault card charge without asking me?" | open — docs/vault says a saved card fills in without per-use approval; changelog v0.77.0 says "you still approve every purchase" (re-checked 2026-11-04) (?) | don't tick "Securely save" for the card; choose "Allow once" | https://docs.x.ai/bot/vault · https://x.ai/changelog/bot (v0.77.0) | 2026-11-04 |
| KI-007 | Access / plans | "is there a free trial or not?" | unclear (?) — @bot 2026-08-21: limited free trial; Elon 2026-10-15: "no free tier"; docs/faq: 7-day trial credit | check Usage & Billing in the app | https://x.com/bot/status/2090852881373311369 · https://x.com/elonmusk/status/2110866513955868924 | 2026-10-15 |
| KI-008 | Bot settings | "I can't find a settings page for my bot's description" | unclear (?) — guide 101 shows Name/Title/Description fields, docs say personal bots change behavior in chat | tell the bot "remember…" in chat | https://x.ai/bot/guides/grok-bot-101 (kb/features.md) | — |
| KI-009 | Skills | "skills don't get invoked" | unclear (?) — users reported it; Eric asked for details; no fix known | name the skill explicitly in the message; send feedback | https://x.com/ericzakariasson/status/2115872535569150111 | 2026-10-29 |
| KI-010 | Desktop app speed | "slow to reconnect after flaky Wi-Fi / slow after laptop wake" | fixed (53 perf fixes: reconnect 60s→0.7s, wake 23s→1s); version not stated (?) | update the desktop app | https://x.com/poteto/status/2102504221648339170 | 2026-09-22 |
| KI-011 | Gmail connector | "Gmail stopped working and nobody told me" | fixed in v0.77.0 — primary Bot now tells you when Gmail signs you out and offers to reconnect | reconnect Gmail when asked | https://x.ai/changelog/bot (v0.77.0) | 2026-10-26 |

How to report a new bug: in-app Send Feedback (poteto: add "poteto poteto poteto"), or ask your bot to send feedback — https://x.com/poteto/status/2096089814672314420
