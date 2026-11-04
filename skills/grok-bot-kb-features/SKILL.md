# grok-bot-kb-features
Snapshot 2026-11-04 of the Grok Bot features table and changelog. Use this for "can it do / since when / limits" questions and to bootstrap kb/features.md and kb/changelog.md. Live sources win over this snapshot.
Source keys: CL = https://x.ai/changelog/bot (vX.Y.Z) · D:<page> = https://docs.x.ai/grok-bot/<page> · (?) = unverified · n/v = not visible.

## Features (what · limits · since · source)
**Bots and memory**
- Bots: named, each with its own memory, files and browser sessions; first bot "Grok Bot". No cap on the number of bots stated; avatar <25 MB · launch 2026-08-11 · D:bots
- Primary bot ★: coordinates other bots; proactively offers work · shared bot can't be primary; 0.59.0+ · v0.66.0 · CL
- A bot creates bots (sidebar sections) v0.34.0; edits its own title/shape/color v0.51.0 · CL
- Duplicate a bot: copies profile, settings, skills, routines · iPhone only; no history or memory · D:bots
- Delete a bot: irreversible; shared-computer files stay · D:bots
- Instructions: personal bots change behavior in chat ("remember…"); guide 101 shows Name/Title/Description; length limit n/v; docs conflict (?) · https://x.ai/bot/guides/grok-bot-101
- Multiple accounts v0.48.0 · CL
- Memory: automatic (preferences, rules, facts, dated log); per bot; edit via chat; size n/v; not a source of truth · D:bots
- Import Memory from another AI assistant: Settings → General → Start Import; primary bot only; 0.75.2+ · v0.77.0 · CL
- Team Bot memory: private notes per person · v0.61.0
**Skills and routines**
- Skills: "save the process as a skill called…"; docs' 6 sections: when, inputs and access, steps, validation, return, approvals. Format and size limits n/v · D:skills-routines-and-automations
- Teach a task by recording: desktop, ≤10 min, no mic · D
- Private skills shared across your bots (enable per bot; @ reference); Team skills publish/sync · D
- No / skills menu on any platform; invoke by name · staff post 2026-10-29 https://x.com/ericzakariasson/status/2115887078903071224 (?)
- Routines: schedule or event, cloud. 50 per bot; ≥5 min between schedules; 300 runs/h total, 200/h per routine; last 20 runs kept · D:skills-routines-and-automations
- Triggers: webhook v0.21.0; GitHub single PR (removes itself on merge) v0.25.0; inbox / tagged name+tag@ v0.71.2–v0.75.2; Slack, Linear, Sentry, PagerDuty, email (?) · CL
- Pause/resume v0.52.0; delete stops runs v0.51.0. Each bot sees only its own routines (?)
- Frequency advice: a 15-min routine ≈100 runs/day; hourly or a few times a day is usually enough; event triggers are cheapest · https://x.com/poteto/status/2091368467060662497
**Multi-bot, Slack, teams**
- Bot-to-bot messages: async; every reply counts toward usage; text handoffs only · D:chat-and-collaboration
- Group chats: 2–6 bots; @everyone; approvals, secrets and drafts not shown in groups · D
- Team Bots: one bot for the team (app + Slack), Managers v0.64.0; use counts per teammate · v0.61.0 · CL
- Slack: thread replies, reads joined channels, user-group mentions; @here/@channel don't ping · v0.61.0/v0.68.1
- Admins can turn off bot-to-bot messaging v0.71.2; Projects (Cloud Agent that plans and runs agents) v0.57.0
**Computer and local**
- Cloud computer: Firecracker VM, /workspace; ONE per user, shared by all bots (not a security boundary); packages can vanish on update/reset; US region · D:computer-and-apps, D:security
- Each bot has its own screen; 1 computer-use task per screen; cookies shared
- Local execution: Ask/Always/Never per computer v0.29.0; egress via your IP v0.50.0; the computer uses your time zone v0.53.0; low-disk warning v0.71.2
**Connectors, plugins**
- Connect Apps (formerly Marketplace) + MCP by URL/command v0.67.0; interactive Figma/Notion/Canva cards v0.70.2; private-CA MCP v0.77.0
- Named connectors: Gmail, Google Calendar/Drive, Outlook, OneDrive, Slack, Notion, GitHub/GitLab/Bitbucket/Azure DevOps, Linear, Zoho CRM, Glean, QuickBooks, Shopify, Clay, 1Password, Figma; GTM: Salesforce, HubSpot, Gong, Granola · CL, posts
- X plugin needs X API credits; connecting X auto-creates a developer account with some credits · https://x.com/bot/status/2093822274067706170
- Cursor plugins install from a plugin page (e.g. pstack https://x.ai/bot/plugin/9717366); deeplink grokbot://app/v1/plugin/add?id=…; install steps (?)
**Email, drafts**
- Email/Slack drafts with Send/Discard v0.45.0; "Disable drafts" per bot v0.64.0 (risky); Outlook drafts v0.60.0
- Bot's own email at mail.grokbot.com: 1 per account, can't rename or delete; ≤50 recipients, 10 attachments (10 MB each/25 MB total); admin must enable · v0.70.2 · CL, D
**X**
- Search and read X posts/profiles without connecting X · v0.70.2 · CL
- @bot tags: not in UK/EU/AU/IS/LI/NO; not on video/GIF posts; not with @grok · D:tag-on-x
- X Chat with bots: Premium/Super/Ultra (not Plus) · D
**Pages, media, files**
- Pages: reports and dashboards, co-edited or auto-updated; publish on pages.grok.bot; not on Enterprise yet · v0.75.2
- Slides (PPTX/Google Slides) v0.68.1; video 1–15 s (6 s default), 480p/720p, ≤14 reference images v0.75.2; images 1:1, 4:3, 3:4, 16:9, 9:16
- Files: 20 per message; images 25 MB (200 MB total); docs/audio 250 MB; video 1 GB · D:files-and-results; PDF save and audio send v0.70.2
**Vault, payments, shopping**
- Vault: logins, cards, contacts; CSV <5 MB; account-wide; 0.75.2+ · v0.75.5
- CONFLICT (?): D:vault says a saved card fills in without per-use approval; CL v0.77.0 says "you still approve every purchase". Advice: don't tick "Securely save" and choose "Allow once" · https://docs.x.ai/bot/vault
- 1Password: you approve each login, the bot never sees it · v0.53.0 Mac; no shared vault v0.77.0
- Payments: Link, X Money, Stripe Link, Shop Pay; default in Vault → Payments · v0.30.0–v0.78.1
- Shopping cards, Buy now (you approve), order tracking v0.78.1; subscriptions: cancel, price, renewal (confirms first) and templates v0.78.1
**Approvals and security**
- Approval needed for send/publish/buy/delete/permissions/prod/terms; Allow once / Always allow / Deny; background cards expire after 30 min · D:approvals-security-and-privacy
- Auto-review: on by default; 20 Allow + 20 Ask-first rules, 1,000 characters each, Ask-first wins; only YOUR messages count as requests · v0.75.8, v0.77.0
- Secrets never in chat: Vault → 1Password → Secure Form; SSO/passkeys/CAPTCHA/banks are done by hand · D
**Phone, voice, calls**
- Apps: iOS 18+, iPadOS 18+, Android 9+; phone apps (Calendar, Reminders, Contacts, alarms ≤24 h) only in your own 1:1 chat with the app open · D:mobile
- Voice chat (iPhone Live Activity, Siri/Shortcuts, Action Button → "Start Voice Chat"); dictation ⌘D/Ctrl+D v0.20.0; Team Bot voice v0.65.0 (desktop)
- Phone calls: the bot calls a person or business, makes the request, takes notes and sends a summary · https://x.com/elonmusk/status/2114365361068138990 (2026-10-25). Terms §2.7: you are the caller of record; calls identify as a virtual assistant and may be recorded; no marketing or mass calls, impersonation or emergency use; temporary numbers · https://x.ai/legal/grok-bot-terms. US-only and 10/day limits come from third parties (?)
**Coding**
- Hands work to Cursor cloud agents (reads transcripts and screenshots); the PR link expires with the run · D
- Custom named mode v0.78.1; repos (GitHub/GitLab/Bitbucket/Azure) v0.49.0; My Machines (your own machine runs agents); choose the agents' model in chat
**Templates, plans**
- Templates: include instructions, relevant memories, skills, first-party plugins, routines; exclude personal memories, custom code, non-standard MCP, secrets, private skills · v0.30.0 · https://x.ai/bot/guides/templates-for-grok-bot
- Bot marketplace with a Verified badge for team-made bots v0.41.0; the bot finds a template for you v0.70.2
- Access: X Premium/Super/Ultra, Cursor Pro, linked SuperGrok/Heavy/X Premium+, Grok Business; from $8/month (?) · trial conflict: "limited free trial" (@bot 2026-08-21) vs "no free tier" (Elon 2026-10-15) (?)
- Usage: weekly pool shared by Grok, Cursor and X; on-demand None/Fixed/Unlimited · v0.46.0. Auto-update on v0.65.0; a version >14 days old is forced to update
- Platforms: macOS, Windows, Linux, iOS, Android; 37 languages desktop / 12 phone; Russian v0.28.0
**Not possible / not visible**: reading another bot's settings (ask it by message); seeing other bots' routines (?); approvals in groups; @bot in EU/UK; phone apps in groups/Slack; skill and instruction size limits n/v; changelog RSS is Cloudflare-blocked for scripts.

## Changelog (newest first; F = fixed count)
- 2026-11-03 X: new shopping experience · 2026-11-02 Data Bot Team use case · 2026-10-29 0.78.1 stable
- 10-27 v0.78.1 shopping cards, Buy now, order tracking, Shop Pay, subscription templates, cloud agent custom mode, Team "Who has access" · F60
- 10-26 v0.77.0 (+0.76.0) 1Password without a shared vault, Import Memory, multi-question cards, table copy, Vault Payments tab, Gmail sign-out notice (fix for silent sign-out), Order Concierge/Deal Watcher, private-CA MCP · F67
- 10-24 v0.75.8 Auto-review rule cards; fewer cards for safe actions · F11
- 10-23 v0.75.5 Vault; forward emails; deny = stop, no retry · F10
- 10-22 v0.75.2 (0.72–0.75.1) Pages, video, Library, Shop Pay, GitHub/Gmail/Calendar upgrades, routines read inboxes, Zoho · F27
- 10-14 v0.71.2 tagged email addresses, pre-filled forms, admin bot-messaging switch, low-disk warning · F72
- 10-11 v0.70.2 bot email addresses, X search, in-app cards, X Money/Stripe Link, template finder, PDF/audio · F31
- 10-07 v0.68.1 slide decks, bot-colored chats; fix: "/" no longer opens the skills menu · F7
- 10-05 v0.68.0 languages, remove computers, Gmail send-as · F5
- 10-02 v0.67.0 Connect Apps rename · F9 | v0.66.0 Proactivity, primary bot · F3
- 09-30 v0.65.0 Team Bot voice, auto-updates · F1 | v0.64.0 Managers, disable drafts
- 09-29 v0.63.0 Slack approvals, faster browsing · F8 | 09-28 v0.62.0 quotes, spell check · F7
- 09-26 v0.61.0 Team Bots · F1 | v0.60.0 Outlook drafts · F6 | 09-25 v0.59.0 Team Secrets · F5
- 09-22 v0.58.0 languages, inactive computers · F8 | 09-18 v0.57.0 Projects · F4 | 09-17 v0.56.0 GitHub depth · F5
- 09-16 v0.55.0 setup checklist · F3 | v0.54.0 Cmd+K search · F4 | 09-15 v0.53.0 1Password Mac, Drive/OneDrive upload, time zone · F5 | v0.52.0 pause routines · F6
- 09-14 v0.51.0 first bot setup, bot edits itself · F3 | 09-11 v0.50.0 egress via desktop · F1 | v0.49.0 repo access · F3
- 09-09 v0.48.0 multiple accounts · F2 | v0.46.0 Usage & Billing · F5 | 09-08 v0.45.0 drafts, admin Auto-review · F4
- 09-06 v0.44.0 chat forms · F4 | 09-04 v0.41.0 bots in Marketplace, Verified · F3 | 09-03 v0.37–0.40 languages, Enterprise, setup
- 09-02 v0.35.0 longer tasks · F3 | 09-01 v0.31–0.34 bots create bots, Link cards, onboarding · F4–5
- 08-28 v0.30.0 Templates, Link purchases, Ukrainian/Arabic/Hebrew · F2 | 08-27 v0.29.0 local execution modes
- 08-26 v0.28.0 Russian · 08-25 v0.27.0 Pro/SuperGrok access | v0.26.0 right-to-left typing (fix for broken RTL) · F3 | v0.25.0 PR-watch routine, on-demand limits · F5
- 08-21 v0.24.0 setting links · 08-19 v0.21.0 webhook routines · 08-14 v0.20.0 dictation | v0.19.0 Manage Plan
- 08-12 v0.18.0 cancel trial | v0.17.0 triggers · 08-11 launch (early beta)
