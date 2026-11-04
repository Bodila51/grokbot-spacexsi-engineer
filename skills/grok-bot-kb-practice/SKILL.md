# grok-bot-kb-practice
Snapshot 2026-11-04: how the Grok Bot team actually sets things up (recipes), plus known issues. Use for "how do I do T", comparisons, "bug or me", and to bootstrap kb/recipes/*.md and kb/known-issues.md. Every practice has a source; (?) = unverified.
G = https://x.ai/bot/guides/ · M = https://x.ai/bot/marketplace/bots/ · P = https://github.com/cursor/plugins/tree/main/pstack

## Recipes
### multi-bot-teams — when: more than 2 bots, or bots that step on each other
- Eric Zakariasson: a Projects Manager bot never does the work itself. One project = one channel = one set of bots = one board. It reuses bots first, uses ≤6 per channel, creates new ones only with approval, and marks stuck work Blocked with a ping · G how-i-run-multiple-teams-of-grok-bots · M projects-manager
- Lingxi Li: one domain per bot; a Notion board checked every 30 min; ops bot "Jenny" runs 5 a.m. 1:1s and postmortems, then updates the playbook · https://x.com/lingxi/status/2094493172516966781
- Lauren Tan: eng-lead bot splits tasks; new bots go through dr eggbot (one job, one voice, anti-jobs, no leftover tools) · M dr-eggbot-v2
- Kiara Polychroniadi: bot-maker "Professor Oak" holds shared rules · https://x.com/kiaraplds/status/2117705575014547661 · Token Officer bot watches fleet spend · https://x.com/kiaraplds/status/2097753767579984281
- Peng Zheng: narrow bots, one responsibility each.
- Steps:
  1. Make the primary ★ bot your chief of staff.
  2. Create bots through one maker bot, with shared rules in /workspace/team/RULES.md.
  3. Keep a shared board, checked every 30 min.
  4. The manager assigns work but doesn't do it.
  5. Use groups only for coordination: approvals, secrets and drafts stay in 1:1 chats.
- Limits: 2–6 bots per group; every bot reply costs usage; one shared computer.
### coding-and-review — when: a bot should ship code
- Lingxi: cloud agents get a "proof required" line (before/after screenshots); a PR sweep every 30 min (CI, Bugbot, conflicts); auto-merge only on a high-confidence review with a small blast radius; 3 a.m. audit PRs · M engineer-bot, M nightly-audit-engineer
- Lauren: pstack playbooks; empirical checks and verification beat adversarial review passes · P · https://x.com/poteto/status/2117437607940681849 · run /create-verification-skill first https://x.com/poteto/status/2093414407196012990
- Lee Robinson: plan first; add a rule only after a repeated mistake; loop until tests pass; parallel worktrees · https://cursor.com/blog/agent-best-practices
- Michael Truell: flaky tests and broken environments are the main blockers · https://cursor.com/blog/third-era
- Steps:
  1. Connect a repo.
  2. One area = one bot.
  3. Include the proof line.
  4. A PR-check routine merges only with approval.
  5. Use the GitHub single-PR trigger (v0.25.0).
- Limits: PR links expire with the run; a P0 check every 5 min "burns tokens fast" (Lingxi, G grok-bot-for-engineering).
### routines — when: anything scheduled
- Docs: run the task by hand → save it as a skill → schedule only once the output is reliable; "Every weekday at 8:00 AM, run the … skill" · https://docs.x.ai/grok-bot/use-cases
- Lauren Tan: 15-min ≈100 runs/day; hourly or a few times a day is usually enough; prefer event triggers · https://x.com/poteto/status/2091368467060662497 · dr eggbot weekly routine-waste check
- Josh Kim: templates start Disabled; twice a day (~9:05/16:05); 0–5 drafts per run; send only after "send" · G grok-bot-for-work
- Eric: notify as soon as the bot can't progress; event triggers over cron · https://x.com/ericzakariasson/status/2092281851822113131 · webhook ideas https://x.com/ericzakariasson/status/2095105948016882133
- @egavrilenko11: monitor X with the X API plugin and surface only 1–3 relevant NEW posts · https://x.com/egavrilenko11/status/2095604008555893015
- Checklist: silent when nothing is new · seen-ids/since-last-run · weekday cadence or a trigger · a success criterion · connector over browser · drafts, not sends.
### memory — when: the bot forgets or repeats mistakes
- Docs: memory is automatic and not a source of truth; secrets go in the Vault; Import Memory (v0.77.0).
- Lauren: brainmaxxing brain/ + /reflect after a correction · https://github.com/poteto/brainmaxxing
- Eric: continual-learning updates AGENTS.md from transcripts · https://github.com/cursor/plugins
- Lingxi: learn-critique, every correction goes into notes · https://github.com/lilingxi01/auto-critique
- Roman Ugarte: Pages as a living knowledge base · https://x.com/romanugarte_/status/2112998685927756007
- Steps:
  1. Give a new bot its job, sources, what's forbidden and what needs approval in the first message.
  2. Ask "What do you remember about me?"
  3. Run a weekly reflect pass: a correction made twice becomes a rule.
### content-and-x — when: listening, posting, media
- Roman Ugarte: bots listen on X for feedback · https://x.com/romanugarte_/status/2107964995783074269
- Matt Palmer: on weekdays, bookmarks → approved demo · https://x.com/mattyp/status/2099482348010328185 · Writing Bot, Stills & Clips Desk
- Josh Kim: 6 marketing bots; start with limited permissions · G grok-bot-for-marketing
- Shub Gaur: Distro Bot posts only with your yes; Stalk Bot watches competitors.
- Lauren: tibot mention digest https://x.com/poteto/status/2115205951649423585 · copy a setup by tagging @bot on a post https://x.com/poteto/status/2117366076342460440
- Steps:
  1. A listening routine 1–3 times a day via built-in X search (v0.70.2).
  2. Drafts only.
  3. One Page as the content calendar.
- Limits: @bot tags not in EU/UK/AU; the X plugin needs API credits.
### design — when: Figma, UI, critique
- Peng Zheng: Figma MCP + a design-system skill; you make "the first 5%", the bot extends it · https://www.lennysnewsletter.com/p/how-i-ai-how-two-spacexai-designers
- John Bai: production assets, not screenshots; localhost motion playground; short comparative feedback · G designing-grok-bot-with-grok-bot · M figma-bro
- Critiquito ranks critique and never edits · M critiquito · Benji Taylor: agentation, stageshow · https://github.com/benjitaylor/skills
### sales-gtm — when: prospecting, CRM
- Krista Letz: chief of staff + specialists; record once, then make it a skill · G grok-bot-for-gtm
- Docs template: "research 25 accounts… return a review list; do not send" · https://docs.x.ai/grok-bot/use-cases
- SDR guide: ~20 accounts each morning, never auto-send · G grok-bot-for-sdrs · Founder-led guide: follow up every 5–6 days, stop after ~8 touches
- Never turn on "Disable drafts" for sales.
### phone-voice — when: phone, voice, calls
- Phone apps (Calendar, Reminders, Contacts, alarms ≤24 h) only in your own 1:1 chat with the app open · https://x.com/bot/status/2113393684209176718
- Voice chat; iPhone Action Button → "Start Voice Chat" · https://x.com/mattyp/status/2112891221576389063 · dictation ⌘D/Ctrl+D
- Calls to a person or business: https://x.com/elonmusk/status/2114365361068138990 · Terms §2.7 (caller of record, virtual-assistant disclosure, no marketing or mass calls) https://x.ai/legal/grok-bot-terms · US-only and limits per third parties (?) · dial bot via Bland AI · M dial-bot

## Known issues (status as of 2026-11-04; daily-scan appends new ones)
| id | area | symptom | status | workaround | source |
|---|---|---|---|---|---|
| KI-001 | iOS | app freezes on the first screen | unclear (?) — fix in progress 2026-08-18 | turn off the Apple accessibility "show borders" | https://x.com/lingxi/status/2089591569146138850 |
| KI-002 | Voice | voice mode disabled for everyone | unclear (?) — re-enable promised 2026-10-06 | text or voice notes | https://x.com/lingxi/status/2107554521346101325 |
| KI-003 | Sign-in | can't get access via Cursor/SuperGrok | unclear (?) 2026-09-01 | Send Feedback | https://x.com/egavrilenko11/status/2094877365419889055 |
| KI-004 | RTL text | Arabic/Hebrew looks broken | fixed in v0.26.0 | update | CL v0.26.0 · https://x.com/poteto/status/2092700749730140284 |
| KI-005 | Composer | "/" pops up the skills menu | fixed in v0.68.1 | update | CL v0.68.1 |
| KI-006 | Vault | saved card charges without asking? | open — docs vs CL v0.77.0 conflict | don't save the card; "Allow once" | https://docs.x.ai/bot/vault |
| KI-007 | Plans | free trial or not? | unclear (?) — conflicting posts | check Usage & Billing | https://x.com/bot/status/2090852881373311369 · https://x.com/elonmusk/status/2110866513955868924 |
| KI-008 | Bot settings | no settings page for the description | unclear (?) — docs conflict | "remember…" in chat | G grok-bot-101 |
| KI-009 | Skills | skills not invoked | unclear (?) 2026-10-29 | name the skill explicitly | https://x.com/ericzakariasson/status/2115872535569150111 |
| KI-010 | Desktop | slow reconnect/wake | fixed (2026-09-22; version n/v) | update | https://x.com/poteto/status/2102504221648339170 |
| KI-011 | Gmail | silent Gmail sign-out | fixed in v0.77.0 | reconnect when asked | CL v0.77.0 |
Report bugs: in-app Send Feedback, or ask your bot to send it · https://x.com/poteto/status/2096089814672314420
