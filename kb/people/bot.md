# Official @bot account and docs (@bot)
- Role / team: Official Grok Bot account (503,370 followers; bio "AI teammates that you can give real work to"); launch post 2026-08-11 (58.6M views) ([source](https://x.com/bot/status/2087224798078517251))
- Links: [X](https://x.com/bot), [docs](https://docs.x.ai/grok-bot), [communities](https://x.ai/bot/community), [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team)
- Confidence: high
## Key ideas
- Docs "Use cases": 8 role templates (sales outbound, talent scout, paid media, expenses, product performance, bug reproduction, account health, chief of staff). Pattern: connect the sources, give a task with a clear output, get a review list (the bot does not send or change anything), and only once reliable turn it into a nightly routine — [docs](https://docs.x.ai/grok-bot/use-cases)
- Docs "Skills, routines, automations": do the task once, then ask the bot to save it as a skill; a good skill states when to use it, inputs and access, steps, how to validate, what to return, what needs approval; then schedule as a routine. Limits: 50 routines per bot, runs at least 5 minutes apart, last 20 run records kept (one lane also reports 300 runs/hr). Triggers include Slack, GitHub, Linear, Sentry, PagerDuty, email, webhook; send/buy/delete/publish need approval — [docs](https://docs.x.ai/grok-bot/skills-routines-and-automations)
- Data Bot: a team bot working as a data scientist for the whole company — [post](https://x.com/bot/status/2117349540168876334) (2026-11-02, 689K views)
- Shared Bots for sales ops: Account Intel Bot, Quote Bot, Deal Bot — [post](https://x.com/bot/status/2115130760009273501) (2026-10-27)
- Communities: six group chats on X (GTM, Product, Marketing, Engineers, Recruiting, Design) with SpaceXSI teammates; you apply to join — [community](https://x.ai/bot/community)
- Beta launched 2026-08-11 — [x.ai/news](https://x.ai/news/introducing-grok-bot)
## Bots, skills, plugins
- Data Bot, Account Intel Bot, Quote Bot, Deal Bot — see posts above (install steps not shown)
- "From Grok Bot Team" marketplace collection — https://x.ai/bot/marketplace/from-grok-bot-team
- xai-org/plugin-marketplace — Grok Build plugin catalog; end-user install command not on README — https://github.com/xai-org/plugin-marketplace — 319 stars
- xai-org/grok-build — terminal coding agent with skills and MCP — Windows: `irm https://x.ai/cli/install.ps1 | iex`; macOS/Linux: `curl -fsSL https://x.ai/cli/install.sh | bash` — 27.7k stars
- xai-org/grok-build-plugin-cc — Claude Code plugin delegating review/critique/rescue to Grok Build — `/plugin marketplace add xai-org/grok-build-plugin-cc` then `/plugin install grok-build@xai-grok-build` — 272 stars
## Copy this in Grok Bot
1. Do a task once, then tell your bot: "Save the process we just used as a skill called 'Weekly account health.'"
2. Make sure the skill states when to use it, inputs, steps, how to validate, what to return and what needs approval.
3. Start each new use case as a read-only review list ("Do not contact anyone"); schedule it nightly only when reliable.
4. Put the bot's job, sources and approval boundaries in your first message to it.
5. Apply to a function community (GTM, Product, Marketing, Engineers, Recruiting, Design): https://x.ai/bot/community
## Sources
- https://docs.x.ai/grok-bot/use-cases
- https://docs.x.ai/grok-bot/skills-routines-and-automations
- https://x.ai/news/introducing-grok-bot
- https://x.com/bot/status/2117349540168876334
- https://x.com/bot/status/2115130760009273501
- https://x.ai/bot/community
- https://github.com/xai-org/plugin-marketplace
- https://github.com/xai-org/grok-build
- https://github.com/xai-org/grok-build-plugin-cc

## Recent posts about Grok Bot (merge of posts.jsonl, paraphrased; added 2026-11-04)
- 2026-10-20: Support case: Bot cleared 204 incident tickets in ~10 min, one engineer approved the batch — https://x.com/bot/status/2112645531076096330
- 2026-09-30: Coding: hand off to Cursor, manage PRs via GitHub and Origin plugins, video demos — https://x.com/bot/status/2105373767568621895
- 2026-09-26: Finance integration: link bank, card and investment accounts — https://x.com/bot/status/2103936247995752705
- 2026-09-10: Sales connectors: Salesforce, HubSpot, Gong, Clay, Granola — https://x.com/bot/status/2098183353665261979
- 2026-09-03: Enterprise GA; free 2 weeks for Grok and Cursor enterprise customers — https://x.com/bot/status/2095621571335655872
- 2026-08-31: Microsoft plugins: Outlook, Calendar, OneDrive — https://x.com/bot/status/2094543253811183943
- 2026-08-29: Connecting X auto-creates a developer account with some included credits — https://x.com/bot/status/2093822274067706170
- 2026-08-28: Purchases via Link — https://x.com/bot/status/2093419921007108385
- 2026-08-21: Access widened: SuperGrok Plus, Cursor Pro+ and Teams; limited free trial for others — https://x.com/bot/status/2090852881373311369
