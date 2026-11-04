# grok-bot-kb-engineers
Snapshot 2026-11-04: Grok Bot / SpaceXAI people and only their Grok-Bot-relevant public practices. Use for "how does N do T", comparisons, and to bootstrap kb/people/<handle>.md, data/handles.txt and data/handles_general.txt. Quote only what is here or in a newer source; (?) = unverified. M = https://x.ai/bot/marketplace/bots/ · TEAM = https://x.ai/bot/marketplace/from-grok-bot-team · G = https://x.ai/bot/guides/

**@poteto — Lauren Tan, lead engineer, Grok Bot**
- Fix each correction at the strongest layer: architecture → lint/CI → rules/skills → style guide · https://redreamality.com/blog/lauren-tan-poteto-trust-before-parallel/ (third-party summary)
- Adversarial review passes mostly waste tokens; spend them on empirical checks plus verification · https://x.com/poteto/status/2117437607940681849
- Bot design: one job, one voice, explicit anti-jobs, no leftover tools · M dr-eggbot-v2 · few good bots https://x.com/poteto/status/2116576229319233596
- Eng-lead bot "Matcha" splits work and does none itself · https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan
- Routine frequency: 15-min ≈100 runs/day; prefer event triggers · https://x.com/poteto/status/2091368467060662497
- Bugs: in-app Send Feedback · https://x.com/poteto/status/2096089814672314420
- Public: pstack (58 skills, /poteto-mode) https://x.ai/bot/plugin/9717366 · https://github.com/cursor/plugins/tree/main/pstack · brainmaxxing https://github.com/poteto/brainmaxxing · dr eggbot
**@lingxi — Lingxi Li, engineering, Grok Bot (iOS v0)**
- 5 engineer bots, one domain each, own memory and specs · https://x.com/lingxi/status/2094493172516966781
- Cloud agents get skills, a detailed prompt and expected proof (screenshots); the bot watches the transcript and unblocks · same
- Board checked every 30 min; auto-merge only on a high-confidence review with a small blast radius; 3 a.m. audits · same
- Ops bot "Jenny": 5 a.m. 1:1s, postmortems, playbook · same · P0 every 5 min "burns tokens fast" · G grok-bot-for-engineering
- Choose the cloud-agent model in instructions · https://x.com/lingxi/status/2094522117362688471
- Public: M engineer-bot, M nightly-audit-engineer, auto-critique https://github.com/lilingxi01/auto-critique
**@ericzakariasson — Eric Zakariasson, SpaceXSI, releases/forum**
- Projects Manager never does the work; one project = channel = bots = Notion row; ≤6 bots per channel; new bots only with approval · G how-i-run-multiple-teams-of-grok-bots · M projects-manager
- 100 use cases thread · https://x.com/ericzakariasson/status/2087258914060664902 · automate what you repeated in 2 weeks https://x.com/ericzakariasson/status/2116282740802998627
- Notify as soon as the bot can't progress; events over cron · https://x.com/ericzakariasson/status/2092281851822113131
- No / skills menu; skills are invoked by name (?) https://x.com/ericzakariasson/status/2115887078903071224
- Public: https://github.com/ericzakariasson/skills (grok-bot-story) · cursor/plugins: continual-learning, cursor-team-kit, cli-for-agent · agent-compatibility https://github.com/ericzakariasson/agent-compatibility
**@mattyp — Matt Palmer, developer experience**
- "Getting Started with Grok Bot" video https://x.com/mattyp/status/2092286281266962681 · "What's New" videos https://x.com/mattyp/status/2117302664799396177
- Bookmarks → approved demo on weekdays · https://x.com/mattyp/status/2099482348010328185 · hourly reservation watch https://x.com/mattyp/status/2116516547007308125
- iPhone Action Button → Start Voice Chat · https://x.com/mattyp/status/2112891221576389063
- Public (TEAM): Tech Demos, Writing Bot, Stills & Clips Desk, dial bot, skippy · mcut https://github.com/mattppal/mcut
**@kiaraplds — Kiara Polychroniadi, field engineer**
- Bot-maker "Professor Oak" holds the rules for all bots · https://x.com/kiaraplds/status/2117705575014547661
- Token Officer bot plus a CFO routine on spend · https://x.com/kiaraplds/status/2097753767579984281
**@pengzheng_ — Peng Zheng, lead designer**
- Narrow bots, one responsibility each; Figma MCP + design-system skill; you make "the first 5%" · https://www.lennysnewsletter.com/p/how-i-ai-how-two-spacexai-designers
- Self-updating personal site; chief of staff on Notion · same · guides G designing-grok-bot-with-grok-bot
**@johnbai — John Bai, designer**
- Production assets, not screenshots; localhost motion playground; short comparative feedback; one auto-layout component · G designing-grok-bot-with-grok-bot
- Voice memo + screenshots → Figma (Figma Bro) · M figma-bro
**@shubgaur — Shub Gaur, startups lead**
- His bots send, post or merge nothing without approval · TEAM
- Public (TEAM): Import Bot (moves setups from Claude/Codex/ChatGPT), Distro Bot, Proto Bot, Startup QA Bot, Stalk Bot, Pfp Bot · connector submissions https://x.com/shubgaur/status/2110436619895570567
**@kristaletz — Krista Letz, GTM**
- Chief of staff + specialists; record once → skill; research only, never invent quotes, send nothing without a yes · G grok-bot-for-gtm · https://x.com/kristaletz/status/2089103618121314689
- Public (TEAM): Outbound Prospecting, Signal Prospector, Pipeline Pulse, Meeting Recap Deck, EBR & Value Deck Builder
**@joshkim — Josh Kim, growth**
- 6 marketing bots; start with limited permissions · G grok-bot-for-marketing · templates start Disabled; twice a day; send only after "send" · G grok-bot-for-work
**@romanugarte_ — Roman Ugarte, product/GTM**
- Finish 100% of the job, not 90% · https://lennysnewsletter.com/p/how-we-built-grok-bot-in-a-month
- X listening for feedback https://x.com/romanugarte_/status/2107964995783074269 · Pages as a knowledge base https://x.com/romanugarte_/status/2112998685927756007 · expert dumps a workflow into a shared bot https://x.com/romanugarte_/status/2115133963857690713
**@leerob — Lee Robinson, teaching/DevRel**
- Plan first; add a rule only after a repeated mistake; hooks loop until tests pass; parallel worktrees · https://cursor.com/blog/agent-best-practices
- Cursor Projects = "Grok Bot for coding" · https://x.com/leerob/status/2110730965056131375
**@davidgomes — David Gomes, engineer**
- Trello → Todoist migration of 1,500+ cards with ~8 parallel workers, resumable progress files, browser fallback when a connector fails (from his card)
- Worktrees primer https://davidgomes.com/worktrees-coding-agents/ · debug mode https://davidgomes.com/cursor-debug-mode/
**@dean_rie — Dean Rie, Cursor forum staff**
- Never paste passwords; payments "Allow once"; Windows My Machines: `agent update` + `agent worker start` · https://forum.cursor.com/t/confused-over-grok-bot/171745.md?page=2
**@n2parko — Kevin Niparko (?), product**
- Core team: chief of staff, EM, 5 engineers, analyst, PM; hourly attention list · https://x.com/n2parko/status/2087251704744235298 · Team Bots launch https://x.com/n2parko/status/2104663299485020568
**@prades_maxime — Maxime Prades, product lead**: named specialists + lead bot "Zidane" · https://x.com/prades_maxime/status/2089217862745698447
**@egavrilenko11 — @egavrilenko11, product growth**: X feedback monitor surfacing 1–3 new posts and calling a cloud agent for a fix · https://x.com/egavrilenko11/status/2095604008555893015 · growth pod https://x.com/egavrilenko11/status/2093409119302791170
**@nickwm — Nick Miller, field engineering**: proactive chief of staff · https://x.com/nickwm/status/2107291948360839536 · plan first, one task per chat
**@jennananpei — field growth**: six field-marketing bots, one per step · https://x.com/jennananpei/status/2107950996970148253
**@benjitaylor — Benji Taylor, head of design**: team brand bot https://x.com/benjitaylor/status/2112986857474585048 · stageshow https://github.com/benjitaylor/skills · agentation https://github.com/benjitaylor/agentation
**@pranavkarthik__**: daily "newspaper" start page https://x.com/pranavkarthik__/status/2112603111156273366 · **@aarniodev**: Slack triage and summaries https://x.com/aarniodev/status/2087238551943426295
**@mntruell — Michael Truell, Cursor CEO**: 35% of merged PRs come from cloud agents; flaky tests are the blocker · https://cursor.com/blog/third-era
**@bot — official**: docs use-case pattern (review list first, then a routine) https://docs.x.ai/grok-bot/use-cases · Data Bot https://x.com/bot/status/2117349540168876334 · sales-ops Shared Bots https://x.com/bot/status/2115130760009273501
**@elonmusk**: Grok Bot announcements only (calls 2026-10-25, purchase guarantee 2026-10-15 (?), ">100 features & fixes a week")
**@sjwhitmore** (Pages), **@shahmeernavid_** (shopping): credits only.
No public Grok-Bot practice found (2026-11-04): @baltaaazr @shaoruu @roshan_s @sunrao @benln @amanrsanger @davep @ellev3n11 @yagiznizipli @cursor_ai (say so honestly; point to someone else).

## Watch handles (daily-scan, Grok Bot posts only)
@poteto @lingxi @mattyp @ericzakariasson @pengzheng_ @shubgaur @johnbai @romanugarte_ @leerob @n2parko @prades_maxime @kristaletz @benjitaylor @joshkim @baltaaazr @shaoruu @roshan_s @kiaraplds @sunrao @egavrilenko11 @nickwm @benln @mntruell @amanrsanger @davep @dean_rie @davidgomes @ellev3n11 @yagiznizipli @nikitabier @aarniodev @thapa_shawn @VineethSendil @bot @cursor_ai @pranavkarthik__ @anishathalye @bliutech @stuart_sul @SirajChokshi @dyl_gat @tidocarriero @sualehasif996 @jennananpei @elonmusk 

## Leads (general AI/design posts, separate block)
@benjitaylor @jennywen @petersellis @singhai @dinkin_flickaa @yagiznizipli @michaelnicollsx @mntruell @amanrsanger @sualehasif996 @leerob @prades_maxime @davep @poteto @pengzheng_ @johnbai @n2parko @ellev3n11 @stuart_sul 
