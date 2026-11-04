# Lauren Tan (@poteto)
- Role / team: Lead engineer, Grok Bot at SpaceXSI/SpaceXAI (prev Cursor, Meta, Netflix; React Compiler core team) ([source](https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan))
- Links: [X](https://x.com/poteto), [GitHub](https://github.com/poteto), [pstack for Grok Bot](https://x.ai/bot/plugin/9717366)
- Confidence: high
## Key ideas
- Fix every correction you give an agent at the strongest layer: architecture first, then lint/CI, then rules and skills, then style guide; human review last (third-party summary of her talk) — [redreamality](https://redreamality.com/blog/lauren-tan-poteto-trust-before-parallel/) (2026-10-05)
- Adversarial review passes mostly waste tokens; spend them on empirical checks (tests, screenshots) plus formal verification; she is cutting the interrogate skill from pstack — [post](https://x.com/poteto/status/2117437607940681849) (2026-11-03)
- Bot design rule: "one job, unslopped, verified"; one job, one voice, explicit anti-jobs, no leftover tools — [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2) (date not visible)
- Eng-lead bot "Matcha" does no work itself; it splits projects into tasks for eng bots, which start cloud coding agents (she runs "really massive agent swarms") — [creatoreconomy](https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan) (2026-09-27, partly paywalled)
- Video "how i shipped 2,500 PRs last month to production": 4.5M views, ~21K likes — [post](https://x.com/poteto/status/2102050467505430555) (2026-09-21). The third-party talk summary says ~2,000 merged PRs/month, self-reported.
- Her verification skill "Control Glass" is internal, not public.
## Bots, skills, plugins
- pstack (poteto-mode) — 58 skills + 2 subagents; /poteto-mode picks one of 23 playbooks (bug fix, perf, feature, orchestrate, babysit PR...); restate goal, reversible work proceeds, pause before irreversible, fresh subagents, main agent reviews every diff — install: Grok Bot "Add to Grok Bot" button at https://x.ai/bot/plugin/9717366; Cursor `/add-plugin pstack` then `/setup-pstack`; source https://github.com/cursor/plugins/tree/main/pstack — version 0.15.36, stars not visible
- Useful pstack commands: /sharpen, /recall, /ketchup, /blast-radius, /correct, /reflect, /automate-me, /arena, /swarm, /interrogate, /create-verification-skill, /unslop, /make-bot-ui (page whose buttons wake a Grok Bot over a webhook)
- dr eggbot — Grok Bot that designs other bots; asks a few preference questions, then creates them with CreateAgent — install: add from https://x.ai/bot/marketplace/bots/dr-eggbot-v2 — installs not visible
- tinkabot — wraps an API into an agent plugin (MCP + skills): data shape first, smallest scaffold, prove locally, then publish — [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team)
- brainmaxxing — persistent memory + reflect/ruminate/meditate/plan/review skills; habit: run /reflect at session end; written for Claude Code, needs adapting — https://github.com/poteto/brainmaxxing — 362 stars
- noodle — orchestrates agents through skills; tell the agent to install it following INSTALL.md — https://github.com/poteto/noodle — 592 stars
- how — explains how a subsystem works using explorer subagents and critics (skills/how/SKILL.md) — https://github.com/poteto/how — 953 stars
- verification-skill-example — project-local verify skill (.cursor/skills/verify-atlas/SKILL.md) — https://github.com/poteto/verification-skill-example — 189 stars
## Copy this in Grok Bot
1. Add pstack with the "Add to Grok Bot" button: https://x.ai/bot/plugin/9717366
2. Add "dr eggbot" from the marketplace and ask it to design your next bot; hold each bot to "one job, unslopped, verified".
3. Make one planner bot (like Matcha) plus worker bots; the planner never does the work, each worker has a test step.
4. Tell your bot to prove changes by running them (tests, screenshots) rather than doing abstract review passes.
5. Under any setup post on X, tag @bot and ask it to read the post and guide you through it ([post](https://x.com/poteto/status/2117366076342460440), 2026-11-02).
6. Every time you correct the bot, ask it to fix that at the strongest layer (checks/lint before rules before docs).
## Sources
- https://x.com/poteto
- https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan
- https://github.com/cursor/plugins/tree/main/pstack
- https://x.ai/bot/plugin/9717366
- https://x.ai/bot/marketplace/bots/dr-eggbot-v2
- https://x.ai/bot/marketplace/from-grok-bot-team
- https://x.com/poteto/status/2102050467505430555
- https://x.com/poteto/status/2117437607940681849
- https://x.com/poteto/status/2117366076342460440
- https://redreamality.com/blog/lauren-tan-poteto-trust-before-parallel/
- https://github.com/poteto/brainmaxxing , https://github.com/poteto/noodle , https://github.com/poteto/how , https://github.com/poteto/verification-skill-example

## Recent posts about Grok Bot (paraphrased; seen 2026-11-04)
- 2026-11-03: Shop/save/ship with @bot; says Bot pays for itself (quoting @bot shopping launch) — https://x.com/poteto/status/2117745465332846698
- 2026-11-02: Tip: to set up a Data Bot like the official one, tag @bot and ask it to read the post and guide you — https://x.com/poteto/status/2117366076342460440
- 2026-11-01: Built tibo's game (tibo.dog) with Grok Bot and Cursor (Day 28 project) — https://x.com/poteto/status/2117004709198475365
- 2026-10-24: Have bots collaborate: add your bots to Slack and work alongside them like teammates — https://x.com/poteto/status/2114071326411690209
- 2026-09-21: Video talk: how she shipped 2,500 PRs last month (made for Cursor Compile London; she was livestreaming Grok Bot Galaxy) — https://x.com/poteto/status/2102050467505430555

## Recent posts about Grok Bot (merge of posts.jsonl, paraphrased; added 2026-11-04)
- 2026-10-31: Guide: create bots via dr eggbot; a few good bots beat many — https://x.com/poteto/status/2116576229319233596
- 2026-10-27: Shared "tibot": watches mentions/keywords, one sorted digest a day (or hourly) — https://x.com/poteto/status/2115205951649423585
- 2026-10-16: How to trust agent work: better architecture, stronger types/invariants, clear boundaries, verification — https://x.com/poteto/status/2111133080526495985
- 2026-10-08: Example prompt: daily 9am Slack digest of interesting Grok Bot uses on X, with ideas for own workflow — https://x.com/poteto/status/2108232222163812795
- 2026-10-06: Release/QA automation: Team Bots "sandcastle" (release manager) + engineer bot in a Slack release channel — https://x.com/poteto/status/2107527180263829827
- 2026-09-30: Favorite setup: Team engineer bot in Slack, @ it for coding work, it can create Projects (cloud agents) — https://x.com/poteto/status/2105377066942349794
- 2026-09-22: 53 desktop perf fixes, e.g. reconnect 60s→0.7s, wake 23s→1s — https://x.com/poteto/status/2102504221648339170
- 2026-09-01: tinkabot: helps build plugins (MCP and/or skills from your API) to submit for approval — https://x.com/poteto/status/2094883369188499937
- 2026-08-28: pstack tip: run /create-verification-skill first, it is the core of a trustworthy agent loop — https://x.com/poteto/status/2093414407196012990
- 2026-08-25: Desktop deeplinks to add plugins: grokbot://app/v1/plugin/add?id=… (X plugin 49086599, pstack 9717366) — https://x.com/poteto/status/2092317628635418739
- 2026-08-23: Usage tip #1: avoid too-frequent routines; a 15-min routine runs ~100x/day; hourly or few/day is enough — https://x.com/poteto/status/2091368467060662497

## pstack in Claude Code (added 2026-11-04)
- Install: `/plugin marketplace add cursor/plugins`, then `/plugin install pstack@cursor-plugins`. Commands are prefixed, e.g. `/pstack:poteto-mode`. Auto-update is off for third-party marketplaces, so update by hand. In Cursor: `/add-plugin pstack`. 23 playbooks. — https://raw.githubusercontent.com/cursor/plugins/main/pstack/README.md (fetched 2026-11-04)

## Interview transcript (added 2026-11-04; source: transcript pasted by owner, video link unknown (?), host likely Matt Pocock (?))
- Trust ladder: verification is the single most important skill; her first Cursor skill was verification; every Cursor/SpaceXAI app has an auto-maintained verify skill.
- Deterministic parts of a skill go into a script/CLI inside the skill; the agent keeps only judgment. Otherwise each agent "rebuilds the world" every run.
- Every repeated agent mistake becomes a lint rule or a codebase constraint (internal framework "Dune", not public).
- Outer loop = Grok Bot (connectors, routines watching Slack, X, email, Linear) sends context to the inner loop = Cursor Projects (coordinator agent that delegates to subagents). One project per cluster of related issues, not one agent per issue.
- Buffer pattern: a routine that only appends found problems to a document; she reviews it every few days to see patterns, instead of fixing each item at once.
- Review by sampling after merge, not blocking every PR; "full autopilot" in pstack spawns verifier agents that fuzz the app; token-heavy, tune down to 1 verifier.
- Mine your past transcripts for the corrections you keep giving, turn them into skills or lint rules; pstack /recall does this for past chats.
- Skills are getting smaller: workflow steps, not exact commands.
- Runs 10+ chief-of-staff agents (perf, user bugs, a native-rewrite experiment); 2,500 PRs in a month, agents merge their own code.
