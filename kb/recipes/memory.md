# Recipe: memory and self-improvement

## Engineers' approaches side by side
| Who | Approach | Source |
|---|---|---|
| Grok Bot docs | Memory saves preferences, rules, facts and a dated work log automatically. It is not a source of truth. Logins go in the Vault. Import Memory brings context in from another AI. | docs/bots, CL v0.77.0 |
| Lauren Tan | brainmaxxing: a `brain/` vault of notes plus `/reflect` at the end of a session or right after a correction. Add only what really improves future work. | [repo](https://github.com/poteto/brainmaxxing) |
| Eric Zakariasson | continual-learning: AGENTS.md is updated from chat transcripts, keeping only high-signal bullets. | [cursor/plugins](https://github.com/cursor/plugins) |
| Lingxi Li | learn-critique: every correction is written into notes. The ops bot keeps a playbook, and the bots "rarely forget" even after weeks. | [auto-critique](https://github.com/lilingxi01/auto-critique), [article](https://x.com/lingxi/status/2094493172516966781) |
| Roman Ugarte | Pages as a knowledge base that the bots keep current and that you can share. | [post](https://x.com/romanugarte_/status/2112998685927756007) |
| Simon Lackowski (guide author) | A correction made twice becomes a saved rule. | [guide](https://x.ai/bot/guides/grok-bot-for-founder-led-sales) |
| Docs get-started | State your lasting preferences in the first message, and save a stable process as a skill or routine. | [cursor.com docs](https://cursor.com/docs/grok-bot/get-started) |
| learncursor.dev (third party) | The first message should give the job, the sources and the approval boundaries. | [guide](https://www.learncursor.dev/learn/cursor-agents/grok-bot-memory) |

## Steps in Grok Bot
1. **First message to a new bot:** its job, its sources, what is forbidden, what needs approval.
2. Check it: "What do you remember about me?" Fix it in chat.
3. Keep the rules for all bots in one file, `/workspace/team/RULES.md` (the computer is shared). Each bot reads it before work.
4. A "reflect" routine once a week: collect the corrections from the week and write rules into the file (only if a correction happened at least twice).
5. Logins and cards go only into the Vault or 1Password, never into memory.
6. Long-lived knowledge (a dashboard, a guide) goes into a Page that the bot keeps up to date.

## Limits
- No memory size limits are shown. You view and edit memory only through chat.
- Deleting a bot deletes its memory. A shared bot saves only team-wide facts.
