# Recipe: a team of bots (multi-bot)

## Engineers' approaches side by side
| Who | Approach | Source |
|---|---|---|
| Eric Zakariasson | A "Projects Manager" bot that never does the work itself. One project = one channel = one set of bots = one Notion board. It reuses existing bots first, proposes at most 5 besides the PM (at most 6 per channel), and creates new bots only with approval. A stuck task gets marked Blocked, with a ping. | [guide](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots), [bot](https://x.ai/bot/marketplace/bots/projects-manager) |
| Lingxi Li | One domain per bot (5 engineer bots), each with its own memory and specs. A shared Notion board that the bots check every 30 min. An ops bot, "Jenny", writes no code: at 5 a.m. it holds a 1:1 with every bot, runs postmortems after mistakes, updates the playbook and onboards new bots. | [article](https://x.com/lingxi/status/2094493172516966781), [guide](https://x.ai/bot/guides/grok-bot-for-engineering) |
| Lauren Tan | An eng-lead bot, "Matcha", splits projects into tasks for the other bots and does none of the work. New bots go through "dr eggbot": one job, one voice, explicit anti-jobs (what the bot must not do), no leftover tools. Bots work side by side in Slack. | [creatoreconomy](https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan), [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2), [post](https://x.com/poteto/status/2114071326411690209) |
| Kiara Polychroniadi | A "bot-maker" bot ("Professor Oak") that holds the rules for all the other bots. Every new bot goes through it first. | [post](https://x.com/kiaraplds/status/2117705575014547661) |
| Maxime Prades | Named specialist bots with a lead bot ("Zidane"). Each has its own skills, personality, memory and routines. | [post](https://x.com/prades_maxime/status/2089217862745698447) |
| n2parko / Kevin Niparko (?) | Core team: chief of staff, EM, 5 engineers, data analyst, PM. An hourly list of what needs attention. Agents should over-communicate. | [post](https://x.com/n2parko/status/2087251704744235298), [guide for PMs](https://x.ai/bot/guides/grok-bot-for-pms) |
| Peng Zheng | Narrow bots: one clear responsibility per bot. | [How I AI](https://www.lennysnewsletter.com/p/how-i-ai-how-two-spacexai-designers) |
| Nick Miller | A proactive chief of staff that posts on its own (for example, before a meeting). | [post](https://x.com/nickwm/status/2107291948360839536) |

## Steps in Grok Bot
1. **Make the primary bot (★) your chief of staff.** It coordinates the others and offers work proactively (v0.66.0).
2. **Create or redesign bots through one "maker" bot.** Add [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2), or make your own like Kiara's. Have it keep the shared rules in a file such as `/workspace/team/RULES.md`. Every bot gets one job, a list of what it must NOT do, and only the tools it needs.
3. **Shared work board.** Use a Notion database or a Page with columns Backlog / Working / Ready for Review / Blocked. A routine every 30 min checks the board (Lingxi's pattern). 30 min is far above the 5-minute minimum.
4. **Manager without the work** (Eric's pattern). The manager splits the work and assigns it to specialists, and creates a new bot only after your approval.
5. **An ops bot for discipline** (Lingxi's pattern). Once a day it runs a short check-in with each bot. After a mistake: root cause, a playbook change, an announcement to the team.
6. **Group chats** only for coordination. Approvals, secrets and drafts don't appear in groups, so keep those in 1:1 chats.

## Limits to keep in mind
- 2–6 bots per group.
- Every bot reply counts toward usage, and messages between bots are asynchronous.
- All bots share **one computer**, so logins and files are visible to every bot.
- A personal user has no switch to stop bots messaging each other.
- Sources: kb/features.md §5–6.

## Related ready-made bots
Projects Manager, dr eggbot, Lingxi's Engineer Bot, Executive Assistant (Natasha Kuo). See kb/marketplace.md.

## Added from posts merge (2026-11-04)
- Token Officer bot watches fleet token burn (kiaraplds); she also runs a CFO routine on spend — https://x.com/kiaraplds/status/2097753767579984281
- Release + QA: sandcastle (release manager) + engineer bot in a Slack channel (poteto) — https://x.com/poteto/status/2107527180263829827
- Growth pod: PM / engineer / data-scientist bots in one channel (egavrilenko11) — https://x.com/egavrilenko11/status/2093409119302791170
- Field marketing: six bots, one per step (jennananpei) — https://x.com/jennananpei/status/2107950996970148253
- Few good bots, designed with dr eggbot (poteto) — https://x.com/poteto/status/2116576229319233596
