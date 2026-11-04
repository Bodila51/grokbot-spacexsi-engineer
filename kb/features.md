# Grok Bot features, by area (as of 2026-11-04)

**Sources**
- docs = https://docs.x.ai/grok-bot/<page>
- CL = https://x.ai/changelog/bot (version vX.Y.Z)
- post = an X post; the link is in the row

**Rules for this file**
- "Since" is the first release or announcement we found.
- "not visible" = the source doesn't say. (?) = unverified.
- Check this file before saying "Grok Bot can't do X". Use the "Not possible / not visible" section at the end.

## 1. Bots and setup
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Bots (roster) | Named bots, each with its own memory, files and browser sessions. The first bot is called "Grok Bot". | launch 2026-08-11 | No cap on the number of bots stated. Avatar upload under 25 MB. | docs/bots |
| First bot at setup | Setup creates your first bot. | v0.51.0 (2026-09-14) | — | CL |
| Primary bot (★) | Coordinates your other bots and checks in on its own. | v0.66.0 | A shared bot cannot be primary. | docs/bots, CL |
| Proactivity | The primary bot spots work it can take off your plate and offers to do it. | v0.66.0 (2026-10-02); @bot post 2026-10-01 | Needs 0.59.0+ | CL, [post](https://x.com/bot/status/2105713240701538538) |
| Bot creates bots | A bot can create a new bot in one of your sidebar sections. Tool names (CreateAgent etc.) are not in the docs; dr eggbot's page mentions CreateAgent. | v0.34.0 (2026-09-01) | — | CL, [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2) |
| Bot edits itself | A bot can change its own title, shape and avatar color. | v0.51.0 | — | CL |
| Duplicate a bot | Copies profile, settings, skills, routines and avatar. | not visible | iPhone only. Doesn't copy history, memory or attachments. | docs/bots |
| Delete a bot | Erases profile, chats, memory, routines and attachments. | — | Irreversible. Files on the shared computer stay. | docs/bots |
| Description and instructions | Personal bots have no settings page: you change behavior in chat ("remember…"). Guide 101 describes Name/Title/Description fields, and Team Bots have a description. | — | Field length limits not visible. The docs conflict here (?). | docs/bots, [guide 101](https://x.ai/bot/guides/grok-bot-101) |
| Multiple accounts | Add several accounts, each with its own bots and data. | v0.48.0 | — | CL |

## 2. Memory
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Automatic memory | Saves preferences, rules, facts and a dated work log. Carries across chats with the same bot. | launch | No size or count limits stated. You view and edit it only through chat. It's not a source of truth. | docs/bots |
| Shared facts | Some facts (name, time zone) are shared across your personal bots. | — | Logins, cards and contacts belong in the Vault. | docs/bots |
| Import Memory | Settings → General → Start Import brings preferences and context from another AI assistant into your primary bot. | v0.77.0 (2026-10-26) | Needs 0.75.2+. Goes into the primary bot only. | CL, docs/bots |
| Team Bot memory | Keeps private notes for each person. Saves only team-wide facts. | v0.61.0 | — | CL, docs |
| Reset conversation | Keeps the memory. | — | — | docs/bots |

## 3. Skills
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Save a process as a skill | "Save the process we just used as a skill called '…'". The docs recommend 6 sections: when to use it, inputs and access, the steps, how to validate, what to return, what needs approval. | launch | Frontmatter, naming and size limits: not visible. | docs/skills-routines-and-automations |
| Teach a task | Record a workflow on the computer view, then refine the draft. | not visible | Desktop only. Up to 10 min. No mic audio. | docs |
| Private skills | Shared across all your bots. Turn them on per bot under Connect apps → Private skills. Reference them with @. | — | Skills from apps or templates cannot be published. | docs |
| Team skills | Publish to the team (needs a description). Sync / Copy link / Unpublish. | — | — | docs |
| Cursor compatibility | Bots support the same MCP servers, plugins and skills as Cursor. | — | (?) according to guide 101 | [guide 101](https://x.ai/bot/guides/grok-bot-101) |
| Skill / menu | The / menu is not shown on any platform; invoke skills by name. | post 2026-10-29 | Staff reply 2026-10-29 (?) | [post ericzakariasson](https://x.com/ericzakariasson/status/2115887078903071224) (added 2026-11-04) |

## 4. Routines and triggers
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Routines | Run on a schedule or an event, in the cloud. | launch | 50 per bot. At least 5 min between schedules. 300 runs/h across all routines, 200 runs/h for one routine. Last 20 run records kept. | docs/skills-routines-and-automations |
| Webhook trigger | Each routine gets its own Webhook URL and key. | v0.21.0 (2026-08-19) | — | CL |
| GitHub PR trigger | Watches one PR and removes itself once the PR merges. | v0.25.0 | — | CL |
| Pause / resume / delete | — | v0.52.0 / v0.51.0 | Deletion is irreversible. | CL |
| Read inboxes | Routines can read the bot's inboxes. A tagged address (name+tag@) starts only its own routine. | v0.75.2 / v0.71.2 | — | CL |
| Other triggers | Slack, GitHub, Linear, Sentry, PagerDuty, email, webhook. | — | (?) listed once in a docs reading, not re-verified | docs (?) |
| Visibility | Each bot sees only its own routines. | — | (?) Grok Bot's own answer to Yarik, 2026-10-31 | — |
| Routines in Slack | Ask a Team Bot in Slack to create, change, pause or delete your routines. | v0.61.0 | Link Slack first. | CL |
| Routine frequency vs usage | A 15-min routine runs ~100x/day; hourly or a few times a day is usually enough; event triggers wake only when something happened. | post 2026-08-23 | Advice, not a limit | [post poteto](https://x.com/poteto/status/2091368467060662497) (added 2026-11-04) |
| Private skills repo sync | Teams/Enterprise: import a private repo as team marketplace with auto refresh on push. Individuals: routine with GitHub PR-merged trigger or push webhook. | post 2026-10-29 | Staff reply (?) not in docs | [post ericzakariasson](https://x.com/ericzakariasson/status/2115877475138105552) (added 2026-11-04) |

## 5. Multi-bot work
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Bot-to-bot messages | Asynchronous: the recipient may answer later. Bots coordinate through DMs, groups and shared files. | launch | Every reply counts toward usage. Handoffs are text only. | docs/chat-and-collaboration |
| Group chats | Add bots in the To: field; @everyone works. | — | 2–6 bots per group. 1 voice call at a time. Approvals, secrets and drafts don't appear in groups. | docs |
| Who can message whom | A personal bot in the app or a Slack DM: yes. A personal bot in a Slack channel thread: no. A Team Bot can message your own bots. | v0.63.0, v0.77.0 | Admins can turn off messaging between bots (v0.71.2). | docs, CL |
| Team Bots | One bot for the whole team, in the app and in Slack, with Managers. | v0.61.0 (2026-09-26), managers v0.64.0 | Use counts against each teammate's allowance. A shared bot can't take @bot tags. | CL, docs/shared-bots |
| Slack | Bots reply in threads, read channels they have joined, mention user groups. | v0.61.0, v0.68.1 | @here and @channel don't ping anyone. | CL |
| Projects | A Cloud Agent that plans the work and runs its own agents. | v0.57.0 (2026-09-18) | — | CL |
| Team engineer bot in Slack | @ a Team engineer bot in Slack for coding; it runs Cursor cloud agents and can create Projects. | post 2026-09-30 | — | [post poteto](https://x.com/poteto/status/2105377066942349794) (added 2026-11-04) |

## 6. Computer, browser, local machine
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Cloud computer | A Firecracker microVM with a shared /workspace. | launch | **One per user, shared by all bots.** Logins and files are visible to every bot. Bots are not a security boundary. node_modules, venvs and installed packages can be lost on update, Recover or Reset. Computers are in the US. | docs/computer-and-apps, docs/security |
| Computer use | Each bot has its own screen. | — | 1 computer-use task per screen. Cookies, sessions and files are shared across bots. | docs |
| Long tasks | Keeps working through long jobs. | v0.35.0 | — | CL |
| Local execution | Ask every time (default) / Always allow / Never allow, per computer. | v0.29.0 | An admin cap applies. Hardware keys are not supported on Linux. | CL, docs |
| Egress through your computer | The bot's traffic goes out from your IP. | v0.50.0 (2026-09-11) | — | CL |
| Low disk | Tells you once and deletes only with your consent. | v0.71.2 | — | CL |
| Time zone | The computer uses your time zone. | v0.53.0 | — | CL |
| Inactive computers | Enterprise: terminated after 30 days without use. | v0.58.0 | Off by default. | CL, docs/computers |
| Computer as host | Running Grok Bot desktop makes your computer a host you can drive from the phone. | post 2026-09-03 | — | [post ericzakariasson](https://x.com/ericzakariasson/status/2095382757929336848) (added 2026-11-04) |
| iOS trackpad mode | Move the cursor in the computer view like a laptop trackpad. | post 2026-08-30 | iOS | [post lingxi](https://x.com/lingxi/status/2094209436806267362) (added 2026-11-04) |

## 7. Connectors, MCP, plugins
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Connect Apps | The app catalog (formerly Marketplace), plus MCP servers by URL or command. @ attaches an app. | v0.67.0 (rename) | — | CL, docs/computer-and-apps |
| Interactive app cards | Figma, Notion and Canva show inside the chat. | v0.70.2 | — | CL |
| Private CA for MCP | Custom MCP servers with a private certificate authority. | v0.77.0 | You approve the CA. | CL |
| Connectors | Named in releases and posts: Gmail, Google Calendar/Drive, Outlook, OneDrive, Slack, Notion, GitHub/GitLab/Bitbucket/Azure DevOps, Linear, Zoho CRM, Glean, QuickBooks, Shopify, Clay, 1Password, Figma. | various | 1Password app 8.12.42+. The X plugin needs X API credits. | CL, docs, [Shopify post](https://x.com/bot/status/2108228871938359347) |
| Cursor plugins | pstack and others install in Grok Bot from a plugin page, e.g. [x.ai/bot/plugin/9717366](https://x.ai/bot/plugin/9717366). | — | Install steps not visible (?) | Lauren Tan's bio |
| Finance integration | Link bank, card and investment accounts; ask about spending and investments. | post 2026-09-26 | Provider not stated in post (?) | [post bot](https://x.com/bot/status/2103936247995752705) (added 2026-11-04) |
| GTM connectors | Salesforce, HubSpot, Gong, Clay, Granola and other GTM tools. | post 2026-09-10 | — | [post bot](https://x.com/bot/status/2098183353665261979) (added 2026-11-04) |
| Microsoft plugins | Outlook, Calendar and OneDrive read/write. | post 2026-08-31 | — | [post bot](https://x.com/bot/status/2094543253811183943) (added 2026-11-04) |
| Plugin deeplinks | grokbot://app/v1/plugin/add?id=… installs a plugin; share via 🔗 on the plugin page. | post 2026-08-25 | Desktop at launch; mobile "coming soon" (?) | [post poteto](https://x.com/poteto/status/2092317628635418739) (added 2026-11-04) |
| Connector submissions | Companies can submit their product as a connector. | post 2026-10-14 | Review required | [post shubgaur](https://x.com/shubgaur/status/2110436619895570567) (added 2026-11-04) |

## 8. Email, Slack, drafts
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Drafts | Email and Slack drafts with Send / Discard. | v0.45.0 | Email from routines stays a draft until you press Send. | CL, docs |
| Disable drafts | Per bot. After that the bot sends directly. | v0.64.0 | Risky: there's no approval. | CL |
| Bot's own email | Claim an address at mail.grokbot.com. Send, receive, forward. | v0.70.2 (2026-10-11) | One per account. Can't be renamed or deleted. Name up to 64 characters. Up to 50 recipients, 10 attachments (10 MB each, 25 MB total). An admin must turn it on (off by default). | CL, docs/computer-and-apps |
| Outlook | Editable drafts. | v0.60.0 | — | CL |
| Gmail extras | Send-as addresses, Spam folder, reply all, attachments. | v0.68.0–v0.75.2 | — | CL |

## 9. X
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| X search and reading | Search X and read posts and profiles without connecting an X account. "Search, read, and monitor X". | v0.70.2; @bot post 2026-10-08 | Query and quota limits not visible. | CL, [post](https://x.com/bot/status/2107949161878606089) |
| @bot tags | Tag @bot in a post or reply; the result appears in the app. | launch | Not in the UK, EU, Australia, Iceland, Liechtenstein or Norway. Not for posts with video or GIF. Not when @grok is also tagged. | docs/tag-on-x |
| Copy a setup from a post | Tag @bot and ask it to read the post and walk you through it. | — | — | [Lauren Tan](https://x.com/poteto/status/2117366076342460440) |
| X Chat | Chat with bots in the X app. | — | Premium / Super / Ultra. Plus is not included. | docs/chat-and-collaboration |
| X Spaces | Mentioned in the "What's New" video. | — | Details not visible (?) | [post](https://x.com/mattyp/status/2115111897397628974) |
| X developer account | Connecting X auto-creates a developer account with some included credits. | post 2026-08-29 | — | [post bot](https://x.com/bot/status/2093822274067706170) (added 2026-11-04) |

## 10. Pages, files, media
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Pages | Reports, memos, dashboards, even games. Edit together or have the bot keep them up to date. Publish on pages.grok.bot. | v0.75.2 (2026-10-22) | Desktop 0.60.0+ or phone 1.14.0+. Not yet on Enterprise. | CL, docs/files-and-results |
| Slide decks | PowerPoint or Google Slides. | v0.68.1 | — | CL |
| Images | Generated on request. Aspect ratios 1:1, 4:3, 3:4, 16:9, 9:16. | — | Not for charts or tables. | docs/files-and-results |
| Video | MP4 from a description or an image. | v0.75.2 | 1–15 s (6 s by default). 480p by default, 720p on request. Up to 14 reference images. | CL, docs |
| Files | Attachments in chat. | — | 20 files per message. Images 25 MB each (200 MB total). Documents and audio 250 MB. Video 1 GB. | docs/files-and-results |
| PDF and audio | Save a web page as PDF; send MP3, M4A, WAV. | v0.70.2 | — | CL |
| Library | Pin items; preview on hover. | v0.75.2 | 5 items per group are shown. | CL, docs |

## 11. Vault, logins, payments, shopping
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Vault | Logins, cards, contacts, CSV import. | v0.75.5 (2026-10-23) | Needs 0.75.2+. CSV under 5 MB. Account-wide (not per bot). Not on shared bots. **The sources conflict:** our docs/vault notes say a Vault card is charged with no approval for each use, while CL v0.77.0 says "you still approve every purchase" (?). Re-check docs/vault live before answering, and recommend "Allow once". | CL, docs/vault |
| 1Password | You approve each login in 1Password, and the bot never sees it. | v0.53.0 (Mac), v0.77.0 (no shared vault) | — | CL |
| Payments | Link, X Money, Stripe Link, Shop Pay. Pick a default. | v0.30.0–v0.78.1 | You approve every purchase (except a Vault card, see above). | CL |
| Shopping | Product cards, product pages, Buy now, order tracking. | v0.78.1 (2026-10-27); post 2026-11-03 | An order needs your approval. | CL, [post](https://x.com/bot/status/2117736249444507834) |
| Subscriptions | Cancel, check price and renewal date. Templates for trials and unused subscriptions. | v0.78.1 | Confirms before changing anything. | CL |
| Purchase guarantee | Elon: if Bot makes a purchase mistake or leaks your card, SpaceX will make you whole. | post 2026-10-15 | Statement on X, not in docs (?) | [post elonmusk](https://x.com/elonmusk/status/2110610960474079445) (added 2026-11-04) |

- Vault conflict re-checked live 2026-11-04: docs/vault still says a saved Vault card fills in at checkout without per-use approval; changelog v0.77.0 says you approve every purchase. Docs advise not saving the card (leave "Securely save" unchecked) if you want to approve each payment. — https://docs.x.ai/bot/vault (fetched 2026-11-04) (?) unresolved

## 12. Approvals and security
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Approvals | Needed for: sending, publishing, purchases and transfers, deleting, permission changes, production changes, accepting terms. | launch | Allow once / Always allow (not in groups) / Deny. Background cards expire after 30 min. | docs/approvals-security-and-privacy |
| Auto-review | Default on. Rules can be added in chat (v0.75.8) and given permission settings (v0.77.0). | v0.45.0 (admin), v0.75.8 | 20 Allow and 20 Ask-first rules, 1,000 characters each. Ask-first wins. Only *your* messages count as requests, not text in emails or web pages. Memory writes and most settings are not checked. | docs, CL |
| Secrets | Never in chat: use the Secure Form or a masked card. Sign-in order: Vault → 1Password → Secure Form. | — | You take over manually for SSO, passkeys, CAPTCHA and banks. | docs |
| Dean Rie's tip | Never paste passwords in chat. For payments, choose "Allow once", not "Always allow". | 2026-10-13 | — | [forum](https://forum.cursor.com/t/confused-over-grok-bot/171745.md?page=2) |

## 13. Phone, voice, car
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Apps | iOS 18+, iPadOS 18+, Android 9+. | Android and iPad by 2026-09-04 | Mobile subscriptions are monthly and individual only. | docs/mobile, [David Pan](https://x.com/davep/status/2095912356685730132) |
| Phone apps | Calendar, Reminders, Contacts, location, alarms, timers, home. | @bot post 2026-10-23 | Only in your own chat with your own bot, with the app open. Alarms up to 24 h ahead, and the bot can't list or cancel them. Can't edit repeating events. | docs/mobile, [post](https://x.com/bot/status/2113393684209176718) |
| Voice | Voice chat (iPhone: Live Activity, Siri/Shortcuts). Team Bot voice chat. Desktop dictation ⌘D / Ctrl+D. | v0.20.0, v0.65.0 | Team Bot voice chat is desktop only. | docs, CL |
| Phone calls | The "dial bot" template places calls through Bland AI. | — | Third-party service (?) | [dial bot](https://x.ai/bot/marketplace/bots/dial-bot) |
| Tesla | Grok in a Tesla works with connectors ("talk to @bot on the road"). | post 2026-09-22 | Details not visible (?) | [post](https://x.com/egavrilenko11/status/2102447060188561630) |
| Call a business | Bot can call a person or business, make the request, take notes, send a summary. | post 2026-10-25 | Announcement; details in docs not checked (?) | [post elonmusk](https://x.com/elonmusk/status/2114365361068138990) (added 2026-11-04) |
| iPhone Action Button | Settings → Action Button → Shortcut → Grok Bot "Start Voice Chat". | post 2026-10-21 | iOS | [post mattyp](https://x.com/mattyp/status/2112891221576389063) (added 2026-11-04) |

## 14. Coding
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Cloud Agents (Cursor) | The bot hands coding to Cursor cloud agents, reads their transcripts and screenshots, and sends follow-ups. | launch | The PR link works only until the run expires. | docs, [Lingxi Li](https://x.com/lingxi/status/2094493172516966781) |
| Custom mode | Cloud agents in a custom mode you name. | v0.78.1 | — | CL |
| Repositories | GitHub, GitLab, Bitbucket, Azure DevOps. | v0.49.0 | — | CL |
| My Machines | Cloud agents on your own machine (for example a Mac mini). | — | Windows: `agent update` + `agent worker start` | [Dean Rie](https://forum.cursor.com/t/confused-over-grok-bot/171745.md?page=2), [Lingxi Li](https://x.com/lingxi/status/2094493172516966781) |
| Model for cloud agents | Tell your bot which model cloud agents should use; conditional picking works. | post 2026-08-31 | — | [post lingxi](https://x.com/lingxi/status/2094522117362688471) (added 2026-11-04) |
| Cursor sidebar | Grok Bot cloud agents hidden in Cursor sidebar by default; enable via Customize Sidebar. | post 2026-09-26 | — | [post mattyp](https://x.com/mattyp/status/2103665640175460572) (added 2026-11-04) |

## 15. Templates and marketplace
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Templates | Share as Template → team or public → link. | v0.30.0 | Includes instructions, relevant memories, skills, first-party plugins, routines. Excludes personal memories, custom code, non-standard MCP, secrets, private skills. | CL, [guide](https://x.ai/bot/guides/templates-for-grok-bot) |
| Bot marketplace | Bots plus plugins. Team-made bots carry a Verified badge. The bot can find a template for you. | v0.41.0, v0.70.2 | Adding a third-party bot accepts its terms. | CL, kb/marketplace.md |

## 16. Plans, usage, languages
| Capability | What it does | Since | Limits | Source |
|---|---|---|---|---|
| Access | X Subscription Premium / Super / Ultra; Cursor Pro; linked SuperGrok / Heavy or X Premium+; Grok Business. The X subscription bundles @bot, @grok, Cursor and X, from $8/month. | v0.27.0; post 2026-10-13 | Prices aren't in the docs. The $8 figure is from Josh Kim's post. SuperGrok Lite and Grok Enterprise can't be linked. | CL, docs/faq, [post](https://x.com/joshkim/status/2109803946609090845) |
| Usage | Weekly usage pool, shared across Grok, Cursor and X. On-demand overage billed through Cursor. | v0.46.0, v0.25.0 | Monthly on-demand limit: None / Fixed / Unlimited. | docs/faq, CL |
| Trial | Usage credit for a 7-day window. | — | Never converts to paid. | docs/faq |
| Platforms | macOS, Windows x64/Arm64, Linux x64/Arm64, iOS, Android. | — | 37 languages on desktop, 12 on phone. Russian since v0.28.0. | docs/get-started, CL |
| Updates | Automatic Updates (on by default). | v0.65.0 | A version older than 14 days with a newer one available forces an update. | CL, docs/troubleshooting |
| Backend model routing | Best backend model per task (incl. Claude Opus 5.5, MidJourney, Suno); simple requests to fast Grok 4.8 when it ships. | post 2026-10-07 | Forward-looking statement (?) | [post elonmusk](https://x.com/elonmusk/status/2107724314451878104) (added 2026-11-04) |
| Access / trial | SuperGrok Plus, Cursor Pro+ and Teams included; limited free trial for others (2026-08-21). Elon 2026-10-15: "no free tier". | post 2026-08-21 | Conflict: trial vs no free tier (?) | [post bot](https://x.com/bot/status/2090852881373311369) (added 2026-11-04) |
| Unified plan | One plan covers Cursor, Grok, Grok Bot and X; changes opt-in. | post 2026-10-12 | — | [post mattyp](https://x.com/mattyp/status/2109784144649838754) (added 2026-11-04) |

## 17. Teams and Enterprise (short)
- Team Secrets: 100 per team, 32 KB per value, 96 KB total. Team Setup scripts: 30-minute timeout, run at start and about daily.
- Audit logs, Action Recording (90 days), Group Access, SSO (SAML 2.0), SCIM.
- Inference hooks (beta), and operations on members' computers.
- Source: docs/teams-and-enterprises, docs/security, docs/computers, docs/inference-hooks.

## Not possible / not visible (check before you say "can't")
- **Reading another bot's settings or instructions:** not described in the docs. Workaround: ask that bot by message to send its rules, skills and routines.
- **Seeing other bots' routines:** each bot sees only its own (?).
- **Stopping bots from messaging each other:** a personal user has no switch for this. Teams admins do (v0.71.2).
- **Approvals, secrets and drafts in group chats:** not shown there. Work in a 1:1 chat.
- **@bot tags in the EU, UK and similar regions:** not available. Work in the app instead.
- **Phone apps in groups, Slack or shared bots:** no. Only in your own 1:1 chat with the app open.
- **Skill format (frontmatter, size):** not visible. Use the 6 sections from the docs.
- **Instruction length limit:** not visible.
- **Changelog RSS for scripts:** blocked by Cloudflare. Open it as a page in the bot's browser.
