# Lingxi Li (@lingxi)
- Role / team: Engineering at SpaceXSI shaping Grok Bot; built Grok Bot iOS v0 ([source](https://x.com/lingxi))
- Links: [X](https://x.com/lingxi), [GitHub](https://github.com/lilingxi01), [site](https://lingxi.li) (nav shell, no visible content)
- Confidence: high
## Key ideas
- "Grok Bot for Engineering": five engineer bots, one domain each (iOS, Desktop + CI, infra, Android, harness), each with its own memory and specs — [article](https://x.com/lingxi/status/2094493172516966781) (2026-08-31; ~1M views on the profile counter, an archive copy shows 501.7K)
- Each bot works through cloud agents: starts them with skills, a detailed prompt and the expected proof (before/after screenshots), watches the transcript and steps in if a run stalls — same article
- Shared Notion board checked every 30 minutes: Bugbot/security findings, CI, merge conflicts, then "Ready for Review"; auto-merge only if review is highly confident and blast radius is small — same article
- Ops bot "Jenny" writes no code: 1:1 with each bot at 5 a.m., runs postmortems, updates the playbook and announces changes, onboards new bots — same article
- Nightly audits at 3 a.m. (dead code, bundle size, load time) so fresh PRs wait in the morning — same article
- Fleet of cloud agents grew from ~15 managed by hand to 200+ at once (archive copy only) — [archive](https://archive.codenewsletter.ai/2094493172516966781)
- Personal taste packaged as skills (/lingxi-design, /lingxi-review, /lingxi-product) — not public
## Bots, skills, plugins
- Lingxi's Engineer Bot, Nightly Audit Engineer — same pattern as the article, ready to add — install: [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team) — popularity not visible
- auto-critique — Cursor plugin: reviewer-style critique of a diff, plus learn-critique saving review angles to notes — install: `npx skills add lilingxi01/auto-critique -g -a cursor` — https://github.com/lilingxi01/auto-critique — 2 stars
- 1password-safe-mcp — local MCP that lists/copies secrets but never returns values to the agent — https://github.com/lilingxi01/1password-safe-mcp — 1 star
## Copy this in Grok Bot
1. Add "Lingxi's Engineer Bot" and "Nightly Audit Engineer" from https://x.ai/bot/marketplace/from-grok-bot-team
2. Tell your bot: give each engineer bot one domain and its own memory/specs; have it start cloud agents with an explicit proof requirement (screenshots).
3. Create a shared Notion board and ask the bots to check PRs on it every 30 minutes; allow auto-merge only for high-confidence, small-blast-radius PRs.
4. Create an ops bot that writes no code: morning 1:1s with other bots, postmortems, playbook updates.
5. Schedule a nightly audit routine (dead code, bundle size, load time) that leaves PRs for the morning.
6. Package your own taste as a skill (design, review, product).
## Sources
- https://x.com/lingxi/status/2094493172516966781
- https://archive.codenewsletter.ai/2094493172516966781
- https://x.ai/bot/marketplace/from-grok-bot-team
- https://github.com/lilingxi01/auto-critique
- https://github.com/lilingxi01/1password-safe-mcp

## Official guides by this person
- [Grok Bot for Engineering](https://x.ai/bot/guides/grok-bot-for-engineering) (2026-09-10) — summary in kb/guides.md

## Recent posts about Grok Bot (paraphrased; seen 2026-11-04)
- 2026-10-23: Ideas for phone apps: restaurants nearby, alarms when something is done, Apple calendar — https://x.com/lingxi/status/2113426507104481348
- 2026-08-31: Article "Grok Bot for Engineering": 5 domain engineer bots, cloud agents, Notion board every 30 min, ops bot Jenny, nightly audits — https://x.com/lingxi/status/2094493172516966781

## Recent posts about Grok Bot (merge of posts.jsonl, paraphrased; added 2026-11-04)
- 2026-08-31: Tell your bot which model to use for cloud agents; conditional model picking works — https://x.com/lingxi/status/2094522117362688471
- 2026-08-30: iOS tip: trackpad mode for the computer view — https://x.com/lingxi/status/2094209436806267362
