# Eric Zakariasson (@ericzakariasson)
- Role / team: SpaceXSI, ex-Cursor (year not visible); role not visible; Cursor forum admin ([source](https://forum.cursor.com/about.json))
- Links: [X](https://x.com/ericzakariasson), [GitHub](https://github.com/ericzakariasson), [site](https://anyblockers.com)
- Confidence: high
## Key ideas
- Thread "100 use cases" seen so far: outreach in your own Gmail voice, multi-bot GTM crew (research, outbound, forecast, inbox, slides), chief-of-staff hub routing to specialist bots, screening 1,000+ event applicants against an ideal customer profile, sorting ~200 job applications, weekly Luma + database + Slack summary — [thread](https://x.com/ericzakariasson/status/2087258914060664902) (2026-08-11, 393K views; archive copy shows only 40 of 100)
- Projects live in Notion, one row each, with a channel per project; specialist bots claim tasks; the manager never does specialist work — [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team)
- Talk "Building your own software factory" (AI Engineer, 2026-04-28) — [youtube](https://www.youtube.com/watch?v=rnDm57Py54A) (not opened)
## Bots, skills, plugins
- Projects Manager — Notion-based project manager bot — install: [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team)
- skills — game-builder, game-builder-blender-assets, grok-bot-story (builds a personal story page from your activity) — `npx skills add ericzakariasson/skills` (or `--skill grok-bot-story`) — https://github.com/ericzakariasson/skills — 22 stars
- continual-learning — updates AGENTS.md from chat transcripts, high-signal bullets only (agent memory) — in https://github.com/cursor/plugins
- cursor-team-kit — internal team workflows for CI, review, ship, verify — same repo
- cli-for-agent — how to design CLIs agents can run reliably — same repo
- grok-voice — Grok voice in an app — same repo
- feedback-agent — React widget records session/errors and sends them to a Cursor cloud agent that can open a PR — `npm install feedback-agent` (needs CURSOR_API_KEY) — https://github.com/ericzakariasson/feedback-agent — 55 stars
- agent-compatibility — scores repo agent readiness 1-100 — `npx -y agent-compatibility@latest /path/to/repo` — 2 stars
- ralph-loop-plugin — stop hook re-sends the prompt until a promise phrase or max iterations — `/add-plugin https://github.com/ericzakariasson/ralph-loop-plugin` — 4 stars
- workstation — "OpenClaw at home": macOS setup plus imessage skill — https://github.com/ericzakariasson/workstation — 27 stars
- Repo list only: scandinavian-design 411, pg-mcp-server 179, gloss 104 stars
## Copy this in Grok Bot
1. Add "Projects Manager" from https://x.ai/bot/marketplace/from-grok-bot-team and keep projects in Notion, one row each.
2. Tell your bot: the manager decides and routes; specialist bots claim and do the tasks.
3. Pick 3 items from the "100 use cases" thread and paste each as a bot job.
4. Install the grok-bot-story skill: `npx skills add ericzakariasson/skills --skill grok-bot-story`
5. Run `npx -y agent-compatibility@latest <repo>` to see how agent-ready a repo is.
## Sources
- https://x.com/ericzakariasson/status/2087258914060664902
- https://archive.codenewsletter.ai/2087258914060664902
- https://github.com/ericzakariasson/skills
- https://github.com/cursor/plugins
- https://github.com/ericzakariasson/feedback-agent
- https://github.com/ericzakariasson/agent-compatibility
- https://github.com/ericzakariasson/ralph-loop-plugin
- https://github.com/ericzakariasson/workstation
- https://x.ai/bot/marketplace/from-grok-bot-team

## Official guides by this person
- [How I run multiple teams of Grok Bots](https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots) (2026-08-27) — summary in kb/guides.md

## Recent posts about Grok Bot (paraphrased; seen 2026-11-04)
- 2026-10-30: Prompt: have Bot look through last two weeks of your work (emails, meetings, Slack, docs) and list tasks you did more than once (to automate) — https://x.com/ericzakariasson/status/2116282740802998627
- 2026-10-29: Asks for feedback on how to improve Grok Bot; goes to @poteto and team — https://x.com/ericzakariasson/status/2115871180792176993
- 2026-10-28: Release 0.78.1 stable: shopping results as product cards, new subscription templates, connect Shop Pay in the vault; changelog at x.ai/changelog — https://x.com/ericzakariasson/status/2115586309096083730
- 2026-10-28: Release 0.77.0 stable: permission settings for auto-review rules, pick bots' default payment method in vault, bots can ask several questions on one card — https://x.com/ericzakariasson/status/2115238537792815303
- 2026-10-26: Release 0.75.8 stable: add auto-review rules right in chat (confirm the card); auto-review takes a second look before blocking; Slack approval cards — https://x.com/ericzakariasson/status/2114833082956321095
- 2026-10-21: Grok Bot pages can host games (Doom demo on a pages.grok.bot URL) — https://x.com/ericzakariasson/status/2113041928661205325
- 2026-09-18: Roundup of the last couple weeks of shipping, starting with marketplace + bot templates (2026-09-18) — https://x.com/ericzakariasson/status/2100999909608771829

## Recent posts about Grok Bot (merge of posts.jsonl, paraphrased; added 2026-11-04)
- 2026-10-29: Sync skills from a private repo: Teams/Enterprise import repo as team marketplace (auto refresh on push); individuals: routine with GitHub PR-merged trigger or push webhook — https://x.com/ericzakariasson/status/2115877475138105552
- 2026-10-29: The / skill menu is not shown on any platform; invoke skills by name — https://x.com/ericzakariasson/status/2115887078903071224
- 2026-10-23: 0.75.2 out: Pages, new cards, video creation — https://x.com/ericzakariasson/status/2113423577408278903
- 2026-10-23: 0.75.5 stable: Vault, email forwarding, fewer approval cards — https://x.com/ericzakariasson/status/2113743401975963908
- 2026-10-19: 0.71.2 out: smarter notifications, files 250 MB (1 GB video), 20 per message — https://x.com/ericzakariasson/status/2112299456255381600
- 2026-10-13: 0.70.2 rolling out: bot email at mail.grokbot.com, live app cards — https://x.com/ericzakariasson/status/2110057450850435451
- 2026-10-08: "Disk Saver" bot proposes cleanups when the computer runs low on space — https://x.com/ericzakariasson/status/2108305253129216471
- 2026-10-07: 0.68.1 out: slide decks, formatted email from draft, bot-colored chats — https://x.com/ericzakariasson/status/2107887770937283028
- 2026-10-05: Changelog page launched, with RSS — https://x.com/ericzakariasson/status/2107161574247129284
- 2026-09-04: "x scout" bot: learns your setup and finds setups on X worth copying — https://x.com/ericzakariasson/status/2095904975511843196
- 2026-09-03: Running Grok Bot desktop makes your computer a host you can drive from the phone — https://x.com/ericzakariasson/status/2095382757929336848
- 2026-09-02: Webhook trigger: Add trigger → webhook; ideas: WhatsApp msg, Notion change, sensors — https://x.com/ericzakariasson/status/2095105948016882133
- 2026-08-26: Secret card: credentials never exposed to the model in plain text — https://x.com/ericzakariasson/status/2092642631344161258
- 2026-08-25: Make the plan last: prefer event triggers (Slack, GitHub, reaction) over cron; have bot notify when stuck — https://x.com/ericzakariasson/status/2092281851822113131
- 2026-08-13: Teach a task: + in chat, record yourself in the browser; use when the bot struggles — https://x.com/ericzakariasson/status/2087916871727354302
- 2026-08-11: 100 use cases seen in beta (thread) — https://x.com/ericzakariasson/status/2087258914060664902
