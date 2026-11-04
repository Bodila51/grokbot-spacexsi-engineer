# Grok Bot changelog (newest first)

**Source:** https://x.ai/changelog/bot (the old URL https://x.ai/bot/changelog redirects there). There is an RSS feed at https://x.ai/changelog/bot/rss.xml, but Cloudflare blocks it for scripts; open it in a browser.

**This copy:**
- Read on 2026-11-04 and retold in our own words.
- Each entry keeps the main "New" items. "+N improved / M fixed" counts the other items on the page.
- "Teams" or "Enterprise" means the item is only for those plans.
- The page shows the date a release was published. The team announces "stable" on X 1–2 days later.

**How to update:** the daily-scan skill adds new releases at the top. Format: `### YYYY-MM-DD · vX.Y.Z — title`.

## Announced on X after the latest changelog entry
- 2026-11-03 — new shopping experience: find the best deal, compare items, and Bot tracks your orders. [@bot post](https://x.com/bot/status/2117736249444507834)
- 2026-11-02 — official Team Bot use case "Data Bot", an on-demand data scientist for the whole company. [@bot post](https://x.com/bot/status/2117349540168876334)
- 2026-11-02 — Matt Palmer's "What's New" video. Chapters: shopping cards, product pages, order tracking, payments, custom modes, Team Bot logins and setup, sharing and finding Team Bots, connector asks. [post](https://x.com/mattyp/status/2117302664799396177)
- 2026-10-29 — Eric Zakariasson: 0.78.1 is stable. [post](https://x.com/ericzakariasson/status/2115586309096083730)

## Releases

### 2026-10-27 · v0.78.1 — Shopping cards and subscription templates (also 0.78.0)
- Shopping results appear as product cards: photo, rating, price, store, and up to 2 badges. 3–4 results show as a carousel. On a product page, "Buy now" starts an order that you approve.
- The bot tracks an order after you place it and tells you when it ships or arrives.
- Shop Pay can be connected in Vault → Payments and set as the default payment method.
- Templates:
  - "Try it, don't pay for it": starts a trial, then cancels it or reminds you before it bills.
  - "Find unused subscriptions".
  - "Watch subscription prices".
- Bots can cancel a subscription or look up its price and renewal date, always after confirming with you.
- Bots can start cloud agents in a custom mode you name.
- Teams:
  - "Who has access" shows who can use a Team Bot, and a Team Bot can be set to "Only you".
  - Managers can add logins to a Team Bot's own Vault.
- +27 improved, 60 fixed.

### 2026-10-26 · v0.77.0 — Permissions, Vault payments, and question cards (also 0.76.0)
- 1Password works without a shared vault. You approve each login in 1Password, and it fills the login in the bot's browser without the bot seeing it (needs app 0.68.0+).
- Import Memory: Settings brings your preferences and context from another AI assistant into your primary Bot (0.75.2+).
- One card can ask several questions in a row, with a "Your own answer" option.
- Tables in chat have a copy button for Slack or markdown.
- Vault Payments tab: pick the default payment method. You still approve every purchase.
- When Gmail signs you out, the primary Bot tells you and offers to reconnect.
- New templates "Order Concierge" and "Deal Watcher". They never buy without your OK.
- Custom MCP servers with a private certificate authority work once you approve that authority.
- Teams:
  - In a DM with a Team Bot, a teammate can have it message other Team Bots.
  - Team Bots can edit their own Slack messages.
  - Admins can limit bot sharing to admins.
- +58 improved, 67 fixed.

### 2026-10-24 · v0.75.8 — Auto-review rule cards and smarter connectors (also 0.75.6, 0.75.7)
- A bot can offer to add, change or remove one of your Auto-review rules on a card you confirm (0.75.2+).
- Auto-review takes a second look before showing an approval card, so you see fewer cards for safe actions.
- +11 improved, 11 fixed.

### 2026-10-23 · v0.75.5 — Vault, email forwarding, and fewer approval cards (also 0.75.3, 0.75.4)
- **Vault:** bots can save your logins, cards and contact info in Settings → Vault and use them to sign in or check out (0.75.2+).
- Bots can forward an email from their own inbox with its formatting and attachments.
- In Slack, bots record who asked for each message they post.
- Halloween: pumpkin-shaped bot avatars.
- Auto-review asks less often about actions you asked for in your own words. After you deny a card, the bot stops and doesn't retry that action.
- +11 improved, 10 fixed.

### 2026-10-22 · v0.75.2 — Pages, new chat cards, and video creation (also 0.72.0–0.75.1)
- **Pages:** bots build reports, memos and dashboards that you edit together, or that the bot keeps up to date.
- **Video:** bots create videos from a description or from an image you share.
- **Library:** pin pages, files and links. The dashboard shows the Pages you have shared.
- Payments: bots can pay with Shop Pay. X Money connects in one tap.
- Teams:
  - share a Page with the whole organization;
  - admins can limit who shares Pages;
  - link previews for Team Bots;
  - a team icon;
  - owners and managers can let collaborators create routines.
- **GitHub connector:** list repos, compare commits, list a PR's commits, read branch and issue comments.
- **Gmail:** attach files to drafts, reply all, forward with a note, label colors.
- **Calendar:** create, update or delete several Google Calendar events in one step.
- Routines can read the bot's inboxes. A handed-off task can create images and videos.
- Zoho CRM connector.
- Enterprise: admins can permanently delete a member's Grok Bot data.
- +26 improved, 27 fixed.

### 2026-10-14 · v0.71.2 — Smarter notifications and larger file attachments (also 0.71.0, 0.71.1)
- Bots can send from a tagged form of their address, like name+shop@, and a routine on that tag runs only for its mail.
- Forms a bot asks you to fill arrive with known fields already filled.
- Teams: admins can turn off "Messaging between Bots".
- Enterprise: admins can recreate, terminate or delete members' bot computers.
- When the bot's disk is low, it tells you once, names the largest files, and deletes them only if you agree.
- +28 improved, 72 fixed.

### 2026-10-11 · v0.70.2 — Bot email addresses, X search, and in-chat apps (also 0.69.0–0.70.1)
- Bots can claim their own email address and receive mail there. Email they send waits for your approval on a draft card.
- **X:** bots can search X and read posts and profiles without you connecting an X account.
- Connectors with an app (Figma, Notion, Canva) show it as an interactive card in chat.
- Bots can pay with X Money or Stripe Link.
- Bots can find a bot template that fits what you describe.
- Shared pages have a title bar with "Download" (saves a PDF).
- Glean (MCP URL) and QuickBooks Online connectors.
- Bots can save a web page as a PDF and send audio files (MP3, M4A, WAV).
- Teams: teammates can approve Auto-review requests from their own DM with a Team Bot.
- Before an irreversible action (send, post, buy, delete), the bot asks for approval.
- +22 improved, 31 fixed.

### 2026-10-07 · v0.68.1 — Slide decks and Bot-colored chats
- Bots build slide decks with you, showing sample slides to choose from, and deliver PowerPoint files or Google Slides.
- Formatted emails from a draft card.
- Gmail: search Spam and move a message back to the inbox.
- Your messages take the bot's color in its chat (0.64.0+).
- Teams: Team Bots can mention a Slack user group.
- Typing `/` in the composer no longer opens the skills menu.
- Actions on the bot's computer are faster.
- +4 improved, 7 fixed.

### 2026-10-05 · v0.68.0 — New languages and computer removal
- New languages: Marathi, Tamil, Telugu, Swahili, Hausa.
- Settings → Computer can remove other computers.
- Drafts can go out from a verified Gmail send-as address.
- The command palette finds plugins.
- +6 improved, 5 fixed.

### 2026-10-02 · v0.67.0 — Connect Apps and new working status
- "Marketplace" is renamed "Connect Apps", with category chips.
- New working-status phrases.
- +6 improved, 9 fixed.

### 2026-10-02 · v0.66.0 — Proactivity, primary Bot and more reliable updates
- **Proactivity:** the primary Bot (marked with a star) spots work it can take off your plate and offers to do it (0.59.0+). Announced on X 2026-10-01: [@bot](https://x.com/bot/status/2105713240701538538).
- +1 improved, 3 fixed.

### 2026-09-30 · v0.65.0 — Team Bot voice chat and automatic updates
- Teams: teammates can start a voice chat with a Team Bot.
- Automatic Updates is on by default.
- Your phone skips notifications for a bot you are viewing on your computer.
- +3 improved, 1 fixed.

### 2026-09-30 · v0.64.0 — Team Bot managers and refreshed avatars
- Email and Slack draft cards offer "Disable drafts for this Bot", so that bot then sends messages directly. Ask it to turn drafts back on.
- Teams: the creator of a published Team Bot can add Managers, who can edit its profile, skills, plugins, secrets and Slack app.
- Refreshed bot avatars.
- +3 improved.

### 2026-09-29 · v0.63.0 — Slack approvals and faster browsing
- Teams:
  - In Slack threads, a bot that needs approval posts a "Review an action" card that only you can answer.
  - Ask a Team Bot in Slack to message one of your own bots, and the reply comes to you privately.
- Faster web browsing.
- +4 improved, 8 fixed.

### 2026-09-28 · v0.62.0 — Quotes, lists, and spell check
- Quote selected text into your next message with Cmd/Ctrl+L.
- Lists in the composer, and spell check.
- Teams: admins can search and delete Team Bots.
- +4 improved, 7 fixed.

### 2026-09-26 · v0.61.0 — Team Bots
- **Team Bots:** publish one bot for the whole team. Teammates chat with it in the app or in Slack, each in their own conversation.
- "Publish to Team" makes a copy with its chat and memories, or "Start fresh".
- Setup walks you through plugins, secrets, skills and files.
- The owner edits its name, description, plugins, secrets, skills, files and Slack app.
- It asks before using a teammate's plugins. Use counts against each teammate's allowance. It keeps private notes for each person.
- In Slack it replies in threads, reads channels it has joined, and can create, change, pause or delete your routines.
- Admins can add Team Bots for the whole team or chosen groups.
- Launch article: [n2parko, "Meet your Team Bots"](https://x.com/n2parko/status/2104663299485020568) (2026-09-28).
- +1 fixed.

### 2026-09-26 · v0.60.0 — Outlook drafts and more reliable replies
- Editable Outlook email drafts: review in chat, then "Send email".
- The sidebar's "Marketplace" button becomes "Connect apps".
- +3 improved, 6 fixed.

### 2026-09-25 · v0.59.0 — Team Secrets and a centered layout
- Expired Auto-review cards offer "Always allow this in the future".
- Enterprise: admins store Team Secrets on the dashboard, and Team Setup scripts get them as environment variables.
- +4 improved, 5 fixed.

### 2026-09-22 · v0.58.0 — New languages, sidebar, and accessibility
- New languages: Czech, Danish, Finnish, Hungarian, Norwegian Bokmål.
- Enterprise: "Terminate Inactive Computers" ends members' computers after 30 days without use.
- +4 improved, 8 fixed.

### 2026-09-18 · v0.57.0 — Projects and richer link previews
- A bot can start a **Project**: a Cloud Agent that plans the work and runs its own agents.
- +6 improved, 4 fixed.

### 2026-09-17 · v0.56.0 — GitHub, spreadsheets, and clearer approvals
- Bots work with GitHub releases, tags, labels, sub-issues, discussions and collaborators.
- +4 improved, 5 fixed.

### 2026-09-16 · v0.55.0 — Setup Checklist and form filling
- The dashboard's Setup Checklist is split into Recommended and Optional.
- +2 improved, 3 fixed.

### 2026-09-16 · v0.54.0 — Search, HEIC photos, and 1Password
- Organization admins can delete members' bot computers along with their data.
- Cmd/Ctrl+K search finds bots, settings, actions and routines.
- +2 improved, 4 fixed.

### 2026-09-15 · v0.53.0 — 1Password, file uploads, and time zones
- On a Mac, connect 1Password so the bot signs in with your saved logins, asking you first unless you allow it.
- Bots can upload files to Google Drive or OneDrive, or attach them to a Gmail draft.
- The bot's computer uses your time zone.
- +2 improved, 5 fixed.

### 2026-09-15 · v0.52.0 — GitHub connection and routine pausing
- Routines can be paused and resumed.
- +2 improved, 6 fixed.

### 2026-09-14 · v0.51.0 — First Bot setup, routines, and scrolling
- Setup creates your first bot for you.
- Deleting a routine stops its future runs.
- A bot can change its own title, shape and avatar color.
- +1 improved, 3 fixed.

### 2026-09-11 · v0.50.0 — Route web traffic through your computer
- "Route egress through this desktop": the bot's web traffic goes out from your computer's IP.
- +1 fixed.

### 2026-09-11 · v0.49.0 — Repository access, search, and file links
- When a bot needs a repository, a card lets you connect GitHub, GitLab, Bitbucket or Azure DevOps.
- Clicking a file path opens that file from the bot's computer.
- +4 improved, 3 fixed.

### 2026-09-09 · v0.48.0 — Multiple accounts and a new Marketplace
- Several accounts can be added and switched between, each with its own bots and data.
- A bot can be added straight from its Marketplace row.
- Enterprise: Conversation Insights shows the team's top use cases.
- +2 improved, 2 fixed.

### 2026-09-09 · v0.46.0 — Usage & Billing and chat renaming
- Right-click a chat to rename it.
- Usage & Billing shows weekly usage and your plan, and the chat warns you near the weekly limit.
- +1 improved, 5 fixed.

### 2026-09-08 · v0.45.0 — Email and Slack drafts, and admin Auto-review
- The bot can write an email or Slack message as a draft, then you choose Send or Discard.
- Enterprise: admins can require Auto-review and add team-wide rules.
- +1 improved, 4 fixed.

### 2026-09-06 · v0.44.0 — Chat forms, timestamps, and AutoFill
- When the bot needs a sign-in or similar, it asks with a form in chat and fills the page for you.
- Message timestamps on hover.
- AutoFill on Mac.
- +2 improved, 4 fixed.

### 2026-09-04 · v0.41.0 — Bots in the Marketplace and plugin setup
- The Marketplace lists bots as well as plugins, with a page for each bot.
- Bots made by the Grok Bot team carry a **Verified** badge.
- +2 improved, 3 fixed.

### 2026-09-03 · v0.40.0 — Enterprise access, languages, and Support menu
- Enterprise: Grok Bot is open to every Enterprise team. Audit Logs record bot creation and access changes.
- New languages: Urdu, Thai, Bengali.
- +3 improved.

### 2026-09-03 · v0.39.0 — Vietnamese, Indonesian, and greetings
- New languages: Vietnamese, Indonesian.
- A new bot greets you in the app's language.
- +4 improved, 4 fixed.

### 2026-09-03 · v0.38.0 — Group Access and sidebar names
- Enterprise: Manage Group Access sits next to the on/off switch.
- +1 improved, 1 fixed.

### 2026-09-03 · v0.37.0 — Setup choices, sharing menu, and follow-ups
- Setup asks which tools you use every day, including Cursor.
- Enterprise: the trial counter is on the dashboard.
- +1 improved, 7 fixed.

### 2026-09-02 · v0.36.0 — Copy links, routine chats, and Always allow
- Right-click a pull request to copy its link.
- +1 improved, 2 fixed.

### 2026-09-02 · v0.35.0 — Longer tasks, purchases, and shared Bots
- The bot keeps going through long jobs and page-by-page browsing instead of stopping early.
- +2 improved, 3 fixed.

### 2026-09-01 · v0.34.0 — Pull request previews and Bots in sections
- PR links show their number, title and status.
- **A bot can create a new bot** inside one of your sidebar sections.
- +1 improved, 3 fixed.

### 2026-09-01 · v0.33.0 — Group Access, team trials, and Link cards
- Enterprise: Group Access and team trials.
- "Pay with" lets you pick a saved card from your Link wallet.
- +5 fixed.

### 2026-09-01 · v0.32.0 — International typing and team setup
- The team page offers "Set up Grok Bot".
- +1 improved, 1 fixed.

### 2026-09-01 · v0.31.0 — Onboarding, team invites, and HTML previews
- Onboarding suggests bots for the kind of work you do.
- Teams: invite the whole team, and a Setup Checklist.
- HTML files the bot makes open as a preview.
- A Cloud Agent opens in Web or in Cursor.
- When a firewall or VPN blocks the bot's computer, Grok Bot says so and offers Retry.
- +2 improved, 4 fixed.

### 2026-08-28 · v0.30.0 — Template sharing, Link purchases, and languages
- **Templates:** share a bot as a template for your team or for anyone. Others add their own copy from the link.
- Purchases: a card shows the amount for you to Allow or Deny, then Link completes the payment.
- Enterprise: Action Recording to the audit log.
- New languages: Arabic, Ukrainian, Dutch, Greek, Afrikaans, Hebrew.
- You can approve a task on one computer from another.
- +2 improved, 2 fixed.

### 2026-08-27 · v0.29.0 — Computers in Settings and phone replies
- Settings → Computer: choose Always allow, Ask every time or Never allow for local execution on each computer.
- Notifications in the Grok phone app show the bot's reply.
- +1 improved, 1 fixed.

### 2026-08-26 · v0.28.0 — Russian, Turkish, Italian, and Swedish
- Interface in Russian, Turkish, Italian and Swedish. It follows the computer's language.
- +1 improved, 1 fixed.

### 2026-08-25 · v0.27.0 — Pro and SuperGrok access, and webhook data
- Cursor Pro, SuperGrok and X Premium+ subscribers (with a linked account) can use Grok Bot.
- +2 improved, 1 fixed.

### 2026-08-25 · v0.26.0 — App menu, right-to-left typing, and updates
- The app menu has Settings, Check for Updates and Restart to Update.
- +3 improved, 3 fixed.

### 2026-08-25 · v0.25.0 — Multi-select questions and on-demand limits
- Questions with several answers allowed.
- The individual plan's monthly on-demand limit can be None, Fixed or Unlimited.
- **A GitHub routine can watch a single PR** and removes itself once the PR merges.
- Diagrams download as PNG.
- +2 improved, 5 fixed.

### 2026-08-21 · v0.24.0 — Setting links, team sign-in, and voice input
- "Copy link" to a setting or plugin.
- Save a video from chat.
- Pick a team at sign-in.
- +2 improved, 3 fixed.

### 2026-08-20 · v0.22.0 — Team setup and translation fixes
- +2 fixed.

### 2026-08-19 · v0.21.0 — App languages, emoji, and webhook routines
- The app's language can be picked under Appearance.
- **Routines can start from a webhook**, each with its own Webhook URL and key.
- Enterprise: Team Setup scripts on every member's computer, and a network access policy.
- +3 improved, 3 fixed.

### 2026-08-14 · v0.20.0 — Dictation, formatting, and clearer errors
- **Dictation:** press or hold ⌘D (Ctrl+D on Windows/Linux) to dictate into the message field.
- +3 improved, 1 fixed.

### 2026-08-14 · v0.19.0 — Manage Plan, scrolling, and Bot naming
- Settings has Manage Plan.
- When included usage runs out, you can upgrade to Ultra or link SuperGrok Heavy.
- +4 improved, 3 fixed.

### 2026-08-12 · v0.18.0 — Cancel Trial in Usage & Billing
- A trial can be ended early. Any remaining trial credits are removed.

### 2026-08-12 · v0.17.0 — More routine triggers and pull request links
- Teams: members with a Standard seat can use Grok Bot through a linked SuperGrok Heavy subscription.
- +3 improved, 5 fixed.

### 2026-08-11 · launch — Grok Bot in early beta
- Bots are AI teammates: they sign in to your tools, use them like you do, and bring back finished work. [@bot](https://x.com/bot/status/2087224798078517251) · [x.ai/news/introducing-grok-bot](https://x.ai/news/introducing-grok-bot)
- Versions 0.17.0 and later are on the changelog page. Earlier versions are not visible.
