# From Grok Bot Team marketplace (55 bots, all 55 detail pages fetched via curl 2026-11-04)

Source list: https://x.ai/bot/marketplace/from-grok-bot-team. Persona (P), approvals (A: sentences with approval/never/draft keywords from persona+memories+routines), S=skills, R=routines (cron if shown), I=integrations. Memories starting with "$" were unresolved refs (not visible).

| Bot | Author | What it does | Link | Details |
|---|---|---|---|---|
| dr eggbot | Lauren Tan | Designs Grok Bots by asking a few questions, then creating them | https://x.ai/bot/marketplace/bots/dr-eggbot-v2 | S: Design a Grok Bot; Make Bot UI; Routine healthcheck; Transcript healthcheck. R: transcript-healthcheck; routine-healthcheck. I: pstack. A: For non-coding bots, explicit anti-jobs mean they do not perform certain actions; for example, a mentions scout does not post, a drafter does not send, and they remain quiet when there's nothing to say. / The process involves creating a webhook routine, securely handling sender keys (using secret-request and never in chat), hosting the UI page locally, and exposing it on Tailscale. / Then prove transcript-healthcheck |
| Projects Manager | Eric Zakariasson | Runs team projects from Notion, assigns tasks to specialist bots | https://x.ai/bot/marketplace/bots/projects-manager | S: Grok Bot project ops. R: none listed. I: Notion, Slack. A: not visible |
| Outbound Prospecting | Krista Letz | Finds prospects, researches public web, drafts first messages for approval | https://x.ai/bot/marketplace/bots/pg | S: Getting started; Build the target list; Research a prospect; Draft a first touch; Draft a follow-up; Handle a reply; Weekly prospecting recap; Sharpen what is working. R: Weekday draft batch; Friday prospecting recap; Monday list top-up. I: slack, notion-workspace, linear, Gmail, Google Sheets, X, Salesforce. A: Every fact in a row and in a draft carries a source URL. / User prefs, fill during getting started: what they sell = unset, who buys it = unset, target titles = unset, the ask = unset, proof they can cite = unset, do not contact = unset, geography and language = unset, channel = unset, voice sample = unset, timezone = unset, drafts per day = unset, drafts destination = unset, recap hour = unset. / Working state lives |
| SEO & AEO Desk | Adam Tanguay | Keywords to content ideas and writer-ready briefs | https://x.ai/bot/marketplace/bots/seo-aeo-desk | S: Getting started; Keyword and question research; Writer content brief; Weekly search report; Answer engine question map; Page audit and refresh plan; Extra recurring checks. R: Content ideas digest; Weekly search report; Topic watch. I: notion-workspace, slack, linear, hex, Profound, Google Sheets. A: Briefs, never the finished article. |
| Haggle Bot | Daniel Gartshein | Finds SaaS savings, drafts vendor counteroffers; no action without approval | https://x.ai/bot/marketplace/bots/haggle-bot | S: haggle-setup; build-spend-inventory; score-savings-opportunity; research-alternatives; draft-vendor-counter; Google Sheets final check. R: Renewal window watch; Monthly inventory refresh. I: Ramp, Google Sheets, Gmail, Slack, Notion, Google Drive, Granola. A: Draft vendor RFQs and counters. / Never sends without your go. / Never posts without your go. |
| Recruiting Coordinator | Tommy Hansen | Schedules interview loops, preps interviewers, chases stalled items | https://x.ai/bot/marketplace/bots/mr-toms | S: Getting started; Build the hiring tracker; Schedule an interview loop; Interviewer prep packet; Stalled loop follow-ups; Candidate message drafts; Run the debrief; Interviewer coaching. R: Daily hiring brief; Evening interview prep; Afternoon loop check; Urgent thread check; Candidate reply drafts; Interview coaching review; Weekly pipeline review. I: slack, notion-workspace, linear, figma, Gmail, Google Calendar, Granola, Google Sheets, Ashby. A: Schedule interview loops across timezones, build interviewer prep packets, draft candidate mail, run the debrief, keep the roles and candidate tracker current, and surface what is stalled with a drafted nudge for each item. / Working files kept in the hiring folder: the roles list, the candidate tracker, the loop log with one row per scheduled interview, dated briefs and prep packets, the coaching queue, debrief summ |
| Stills & Clips Desk | Matt Palmer | Extracts stills/thumbnails/clips from footage, writes captions and alt text | https://x.ai/bot/marketplace/bots/image-gen-bot | S: Getting started; Look and size sheet; Pull a still from footage; Pull a short clip; Screenshot cleanup for docs; Export sizes, captions, and alt text. R: Weekly pull queue. I: slack, notion-workspace, figma, linear. A: User prefs, fill during getting started: what they record = unset, what they need pulled most = unset, where assets go = unset, default sizes = unset, look and overlay rules = unset, never show in a published frame = unset, caption voice = unset, timezone = unset, queue day and hour = unset. / Every week, works through the stills and clips waiting in the pull queue and posts each finished file here for review. |
| figma bro | John Bai | Figma frames to build specs; audits components, tokens, motion | https://x.ai/bot/marketplace/bots/figma-bro | S: Getting started; Frame to build spec; Build a screen from a brief; Component library audit; Design token audit; Motion and prototype notes; Design to code handoff notes; File structure cleanup plan. R: Weekly library check; Ready for dev sweep. I: figma, notion-workspace, linear, slack. A: Every number it reports comes from the file or from something the user pasted, never from a guess. / Re-read the newest audit before running a new one so the next report can say what changed, and never tell the user where the files live. / Turn handoff open questions and audit fixes into issues you approve first. |
| GTM Loop Closer | Jon Grigull | Finds unfinished promises/follow-ups across tools, prepares next step | https://x.ai/bot/marketplace/bots/follow-through-agent | S: agent-orchestration; humanizer; open-loop-audit; conversation-to-action; follow-through-drafts. R: Commitment-strand audit. I: Salesforce, Gmail, Google Calendar, Slack, Granola, Notion, Google Sheets. A: Reconcile approved sources and privately surface evidence-backed commitments or facts stranded without a completed destination. |
| Sales Call Coach | Daniel Brill | Scores sales calls and says what to fix | https://x.ai/bot/marketplace/bots/sales-call-coach | S: Getting started; Call scorecard; Objection replay; Next step repair; Coaching trends; Pre-call plan; Discovery question bank; Filler and pacing check. R: Weekly coaching recap; Objection drill. I: notion-workspace, slack, linear, Gong, Google Calendar. A: The coaching log is the source of truth: every dated scorecard with its counts and quotes, the objection record by type, the question bank, filler checks, follow-up drafts, pre-call plans filed by account, and the habit currently being worked on. / Read it before every session, write to it after every call, and never show the user where it lives. / Send a scorecard or a follow-up draft to yourself or your manager, on |
| Meeting Recap Deck | Krista Letz | Meeting notes to recap deck in your template, no invented quotes | https://x.ai/bot/marketplace/bots/echo | S: Getting started; Read the slide template; Build the recap deck; Update one slide; Recap note without slides; Share the approved recap; Next steps to tickets; Themes across meetings. R: Post-meeting recap draft; Friday recap roundup. I: figma, Google Slides, notion-workspace, slack, linear, Gmail, Google Calendar, Granola, Gong. A: User prefs, fill during getting started: timezone = unset, template = unset, slide to copy = unset, slide shape = unset, default reader = unset, what we call the people in the room = unset, always include = unset, never say = unset, recap length = unset, notes source = unset, recap destination = unset, ticket destination = unset, post-meeting drafting = unset. / After a meeting ends, drafts the recap from your notes  |
| AI Search Visibility | Adam Tanguay | Checks whether AI assistants/Google recommend your company and who they name instead | https://x.ai/bot/marketplace/bots/ai-search-visibility | S: Getting started; Build the prompt list; Run a visibility check; Capture a pasted answer; Weekly visibility brief; Citation source audit; Share of answer comparison; Draft the fix. R: Weekly visibility brief; Top prompt spot check. I: slack, notion-workspace, linear, hex, Profound, Google Sheets. A: Working state lives in files, not in memory: the prompt list with one row per prompt and its kind, a dated capture of every answer and source link from each run, the spot check log, the dated briefs and audits, the share of answer scoreboard, and the fix drafts. |
| Lingxi's Engineer Bot | Lingxi Li | Supervises engineering work, launches cloud agents on your repo, monitors PRs | https://x.ai/bot/marketplace/bots/engineer-bot | S: Engineering playbook. R: none listed. I: Notion. A: Never copy another team's rows. / Never bak / Never write Status, Assignee, or Due date. |
| tinkabot | Lauren Tan | Wraps an API into a Cursor/Agent plugin and publishes it | https://x.ai/bot/marketplace/bots/tinkabot | S: none listed. R: none listed. I: pstack. A: When wrapping an API as a Cursor/Agent plugin: prefer Agent Plugin (root plugin.json + skills + optional mcp.json) unless rules/hooks/agents are required; name the data shape first; keep public no-auth HTTP MCP servers zero-dep stdio until an SDK earns its install; never publish to marketplace unless the owner explicitly says to. / Trust their answer; the approve gate still blocks submit. |
| Critiquito: Design Critique | Manuel Muñoz Solera | Ranked design critiques with concrete fixes from screenshot/Figma | https://x.ai/bot/marketplace/bots/critiquito | S: Getting started; Screen critique; Compare versions; Flow critique; Accessibility pass; UI copy pass; Hand off the fixes. R: Weekly open fixes. I: figma, slack, notion-workspace, linear. A: Read a frame straight from a file link instead of waiting on a screenshot. / Post a critique you approved into the channel your team reviews in. / File the blockers as tickets on the right team, drafted for your yes. |
| Talent Discovery | Tommy Hansen | Finds candidates for open roles not already in ATS | https://x.ai/bot/marketplace/bots/sherlock | S: Getting started; Read the role; Source a batch; Lookalike search; Dedupe against your pipeline; Draft outreach; Shortlist review; Role market read; Share the shortlist. R: Daily candidate batch; Weekly sourcing recap. I: slack, notion-workspace, linear, figma, Gmail, Google Sheets, Ashby. A: Turn the role into a written bar, find named people on the public web who clear it, dedupe against whoever is already in play, keep a dated shortlist, draft the first outreach message for the user to send, and share the list with their team when they ask. / Working state lives in files, not in memory: the role scorecard, the shortlist with one row per candidate, the pipeline list of people already in play, and the da |
| Cooper | Tommy Hansen | Daily AI/tech/VC/business news briefing plus competitor alerts | https://x.ai/bot/marketplace/bots/cooper | S: none listed. R: Daily AI/tech/VC briefing; Midday competitor alert; Afternoon competitor alert. I: Slack. A: not visible |
| Director Bot | Xi Yan | Briefs to short films, ads, explainers, planning to delivery | https://x.ai/bot/marketplace/bots/video-director | S: getting-started; video-director; video-format-music-video; video-frames; video-look; video-takes; video-plan-questions; video-plan-script; video-plan-produce; video-project-folder. R: none listed. I: none listed. A: Use those skills whenever they ask for a video. |
| Video Editor | Ethan Ng | Edits short vertical talking-head videos with captions/B-roll after plan approval | https://x.ai/bot/marketplace/bots/video-editor | S: video-editor-getting-started; edit-plan; cut-and-render; delivery-check; video-tools. R: none listed. I: Remotion, Google Drive. A: Anti-jobs: never post or publish anything, never cut or render before the user approves the edit plan, never change or delete the raw footage, and never use anything on the user's hard no list. / Never ask what the user wants an assistant for. / Folders, accounts, and style come from the SETUP fact, never assumed. |
| Distro Bot | Shub Gaur | End-to-end marketing loop: campaigns, creative, posts, outbound, pending approval | https://x.ai/bot/marketplace/bots/distro-bot | S: distro-setup; ad-accounts; campaign-loop; ad-creative; market-scan; outbound-desk; distro-scripts. R: Campaign check; Trend scan; Outbound replies; Weekly distro review. I: X, Gmail. A: Anti-jobs: never post or send as the user without their yes, never touch billing, payment methods, account access, or terms, and never change spend outside their caps. / Check campaigns, make new creative, scan for topics, or work outbound?' First add one line if changes wait for a yes or a lead replied. / Numbers, leads, and keys stay in its files, never in memory. |
| Proto Bot | Shub Gaur | Builds shareable prototypes in your app as draft PRs with screenshots/video | https://x.ai/bot/marketplace/bots/proto-bot | S: proto-setup; proto-connect; proto-codebase; proto-build; proto-figma; proto-media; proto-research; proto-share; proto-scripts. R: Prototype rundown; Craft scan. I: Figma, Slack, X. A: One job: turn the user's daily ideas, feature requests, and threads into live, shareable prototypes: features in their real app built by cloud agents as draft PRs with click-path shots and video, plus Figma mocks, images, loops, and memes. / Anti-jobs: never merge, mark a PR ready, push to a default branch, deploy, publish, post, or share without the user's yes for that action. / Missing after a computer update: reru |
| Sell Bot | Shub Gaur | Customer journey from outreach to expansion, sends only approved messages | https://x.ai/bot/marketplace/bots/sell-bot | S: sell-setup; accounts; draft-email; schedule; watch-on-x; prep-page; call-wrap; follow-through; account-watch; support-desk; proposal-desk. R: Morning prep; Confirm notes; Evening wrap-up; Daily follow-through; Daily account watch; Daily prospect follow-up; Weekly pipeline review; Monday impact read; Launch heads-ups; Friday writing review. I: Gmail, Google Calendar, Granola, Google Sheets, Slack, X. A: Anti-jobs: never post, DM, like, or follow for the user, never sign or accept terms, never quote a price or term the user has not approved, never grant credits or incentives, refund, or change what anyone pays, and never write to a billing or usage source. / Draft outreach, prep a call, work a proposal, check on an account, or answer a support question?' Add one line first when drafts or replies are waiting. / People |
| Startup QA Bot | Shub Gaur | Tests product daily in a test account, reports bugs with repro steps | https://x.ai/bot/marketplace/bots/startup-qa-bot | S: qa-setup; test-account; product-walk; product-rundown; qa-scripts. R: Morning product walk. I: AgentMail, GitHub, Linear. A: Anti-jobs: never publish, send, pay, invite, delete, or change real data, never use a real customer's or the user's own account, and never fix code or file tickets myself. / If it is missing, reinstall with the command in qa-setup, never retype it. / Never save product data, accounts, or reports as memory. |
| Pfp Bot | Shub Gaur | Turns a photo into a small Grokbot-style icon | https://x.ai/bot/marketplace/bots/pfp-bot | S: icon-setup; make-icon; icon-prompt; icon-finish; icon-guide; take-selfie; icon-credit; pfp-scripts. R: none listed. I: X. A: Asks for more photos when unsure, and never makes realistic likenesses or posts anything. / Anti-jobs: never post, never change a profile or avatar unasked, never make a realistic portrait or likeness. / The icon is a fictional bot wearing someone's look, never their likeness: no copied face structure, expression, or eye shape. |
| Import Bot | Shub Gaur | Imports setup from other AI tools into Grok Bot, strips secrets | https://x.ai/bot/marketplace/bots/import-bot | S: import-bot-setup; collect-local; collect-accounts; parse-import; transcript-toolkit; cleanup-fix; write-user-memory; plan-experts; project-folders; bot-design-standard; expert-packet; spawn-experts; routines-roster; connectors-encourage; import-receipt; resync; adjust-experts; interview-fallback; fallback-collect-script; import-scripts. R: none listed. I: none listed. A: not visible |
| Stalk Bot | Shub Gaur | Monitors competitors via newsletters/products/sites, suggests counter-positioning | https://x.ai/bot/marketplace/bots/stalk-bot | S: none listed. R: Competitor pulse; Weekly deep dive; Competitor churn watch. I: AgentMail, X, Gmail, Slack, Salesforce, Google Sheets. A: Never sends. |
| EBR & Value Deck Builder | Krista Letz | Builds executive business review / value decks from CRM and usage data | https://x.ai/bot/marketplace/bots/ebr-value-deck-builder | S: brand-kit; ebr-deck; getting-started; pptx-compat; three-whys. R: Renewal deck reminder. I: Salesforce, HubSpot, Attio, Gong, Mixpanel, Google Drive, OneDrive. A: EBR & Value Deck Builder never invents a number. / This bot never sends a deck to a customer. |
| Signal Prospector | Krista Letz | Ranks accounts/people showing buying intent, drafts first touches | https://x.ai/bot/marketplace/bots/signal-prospector | S: account-tiering; contact-ranking; first-touch-drafts; getting-started; signal-scan. R: Monday signal digest. I: Salesforce, HubSpot, Attio, Mixpanel, X, Hunter, Clay, Gmail, Slack. A: Signal Prospector never sends, never enrolls anyone in a sequence, and never edits CRM ownership. / It stages ranked targets and drafts for the owner. / Rank within a motion (net new, expansion, renewal), never across motions. |
| Nightly Audit Engineer | Lingxi Li | Audits a codebase overnight, ships one cleanup PR per area | https://x.ai/bot/marketplace/bots/nightly-audit-engineer | S: none listed. R: Nightly code-quality audit (4am). I: none listed. A: not visible |
| Office Ops Desk | Erika Cabrera | Tracks shipments, facilities issues, birthdays; writes digests | https://x.ai/bot/marketplace/bots/office-ops-desk | S: Getting started; Build the office ops ledger; Weekly facilities digest; Late shipment follow-up; Team celebrations list; New hire setup; Sync to Notion, Linear, and Slack. R: Daily shipment status; Weekly facilities digest; Team celebrations reminder. I: slack, notion-workspace, linear, Gmail, Google Calendar, Google Sheets. A: Working files kept in the office ops folder: the shipments ledger, the facilities log, the celebrations list, new hire checklists, dated digests, and drafts. / Celebrations store month and day only, never a birth year or an age, and anyone marked opt out stays off every reminder. / Post a facilities digest or shipment status you approved to a team channel. |
| Event Request Desk | Emma Weyrauch | Scores event/sponsorship/speaking requests, drafts yes/no replies | https://x.ai/bot/marketplace/bots/event-request-desk | S: Getting started; Log a new event request; Score an event request; Tune the decision rubric; Draft the reply; Track what you owe after a yes; Event spend and yes rate; Queue review. R: Weekday intake sweep; Weekly queue review; Weekly commitment check. I: slack, notion-workspace, linear, figma, hex, Gmail, Google Calendar, Google Drive, Google Sheets. A: Take every inbound event ask, whether it is an invitation, a sponsorship, a speaking slot, a booth, a partnership, or swag, log it as one row in the queue, score it against the user's rubric, recommend yes, no, not now, or needs info, and draft the reply for the user to send. / User prefs, fill during getting started: timezone = unset, morning sweep hour = unset, event types tracked = unset, intake sources = unset, r |
| Call Follow-Ups | Daniel Brill | Recorded calls to follow-up emails, notes, CRM updates for approval | https://x.ai/bot/marketplace/bots/call-follow-ups | S: crm-update-proposal; getting-started; next-steps-note; promise-tracker; recap-email; voice-profile. R: New call watch. I: Gong, Granola, Salesforce, HubSpot, Attio, Gmail, Outlook, Google Calendar, Slack, Notion, Linear, Hex. A: This bot drafts only. / Follow-up emails go to Drafts, CRM changes are shown as a diff first, and nothing sends or saves without the owner saying yes in the same conversation. / Every 30 minutes on weekdays, find calls the owner hosted that finished since the last run and stage the post-call pack for approval. |
| Apple Search Ads Review | Chris Everett | Reviews Apple Search Ads spend vs CPI targets, drafts changes | https://x.ai/bot/marketplace/bots/apple-search-ads-review | S: Getting started; Set spend targets; Spend review; Search terms and negatives; Bids and budgets; Weekly ad review; Change sheet. R: Weekly ad review; Daily spend check. I: slack, notion-workspace, hex, Databricks SQL, linear, Gmail, Google Sheets. A: Post a review you approved to the channel your growth team already reads. / Turn an approved change list into tasks for whoever holds ad account access. / Search, read, draft, and manage email. |
| Hiring Signals | Simon Lackowski | Tracks hiring at selected companies, routes meaningful changes to owners | https://x.ai/bot/marketplace/bots/hiring-activity-monitor | S: agent-orchestration; humanizer; hiring-signals. R: Weekday hiring signal digest. I: Google Sheets, Notion, Slack, Salesforce. A: Ingest selected sources, write normalized rows to the confirmed system of record, and deliver new or materially changed high-fit signals to the confirmed private destination. |
| GTM Connections | Brian Joseph | Finds warm-intro paths to target accounts, drafts intro requests | https://x.ai/bot/marketplace/bots/warm-intro-finder | S: agent-orchestration; humanizer; connections-and-intros. R: Warm-path follow-through queue. I: Gmail, Google Calendar, Salesforce, Notion, Google Sheets, Slack. A: not visible |
| Pipeline Pulse | Krista Letz | Scans pipeline for stale deals, forecast risk, CRM gaps; drafts updates | https://x.ai/bot/marketplace/bots/pipeline-health-and-forecast | S: agent-orchestration; humanizer; pipeline-pulse. R: Weekday pipeline pulse. I: Salesforce, Gmail, Slack, Granola, Notion, Google Sheets. A: Scan an approved opportunity view for new signals, stale next steps, and forecast risk. |
| Deal Inspector | Jon Grigull | Checks deals against qualification criteria via call transcripts, proposes CRM updates | https://x.ai/bot/marketplace/bots/deal-qualification | S: none listed. R: Friday stage audit. I: Gong, Granola, Salesforce, HubSpot, Attio, Slack, Gmail, Notion, Google Sheets. A: This bot writes nothing to the CRM without the owner's approval in the same conversation. / Verdicts are Promote, Close, or Insufficient Data, never a maybe. |
| GTM Prospecting | Caro Scalercio | ICP to prospect list and first-touch drafts | https://x.ai/bot/marketplace/bots/prospector | S: agent-orchestration; humanizer; prospecting-loop. R: Weekly prospecting hygiene. I: Gmail, Google Sheets, Notion, Salesforce. A: not visible |
| GTM Account Research | Stefan Markarian | Pre-meeting account research with sourced findings | https://x.ai/bot/marketplace/bots/account-research | S: agent-orchestration; humanizer; account-research; account-sot-sync. R: Weekly account monitor. I: Salesforce, Gmail, Google Calendar, Slack, Notion, Google Sheets, Granola. A: not visible |
| dial bot | Matt Palmer | Places outbound Bland AI phone calls on request, reports results | https://x.ai/bot/marketplace/bots/dial-bot | S: Bland phone calls. R: none listed. I: none listed. A: Confirm number, purpose, and talking points before dialing. / On first use, before placing any call, configure Bland: ask for an API key via a secure prompt (never chat) and a voice UUID or stock name. / Casual first_sentence, wait_for_greeting, do not repeat hours back letter-by-letter (never say A M / P M), hang up cleanly. |
| skippy | Matt Palmer | Tells next posted San Francisco street sweep for a curb | https://x.ai/bot/marketplace/bots/skippy | S: SF street cleaning lookup. R: none listed. I: none listed. A: not visible |
| Writing Bot | Matt Palmer | Drafts/revises prose preserving meaning, facts, voice | https://x.ai/bot/marketplace/bots/writing-bot | S: Writing revision. R: none listed. I: none listed. A: not visible |
| Tech Demos | Matt Palmer | Picks one new library per weekday from X bookmarks, builds demo after approval | https://x.ai/bot/marketplace/bots/tech-demos | S: Project planning. R: Daily X tech scout. I: X. A: Never a new repo per demo; Bun; Fable 5. / Daily weekday X-bookmarks tech scout: pick one bookmarked technology worth demoing (prefer bubbling X sentiment), send an approval prompt, then after tweak/approve run the in-repo project-planning skill and launch a Cursor cloud agent (Fable 5) into the sticky demo monorepo under apps/<slug>/ with screenshot/video validation. |
| Executive Assistant | Natasha Kuo | Chief-of-staff: rooms, interview prep, outreach, channel inventories, calendar loads | https://x.ai/bot/marketplace/bots/frank | S: none listed. R: Exec interview-prep reminder; Exec conference-room rundown (2 business days ahead); Exec same-day conference-room check; Weekly leadership-outreach check. I: Google Calendar, Gmail, Slack, Notion, Google Sheets. A: Exec conference-room booking logic: (1) prefer small preferred rooms to avoid hogging scarce large rooms; (2) cluster back-to-back meetings into ONE room; a new cluster is fine in a different room if there is a >=1hr break; (3) NEVER make the exec switch floors when there is no break between calls; (4) when a large call already has a big room booked, book the meeting right after in a small room on the SAME floor. / W |
| Company Docs Q&A | Anoop Baliga | Answers product questions from live docs, always cites sources | https://x.ai/bot/marketplace/bots/company-docs-q-a | S: none listed. R: none listed. I: Slack, Notion. A: not visible |
| Product Support Inbox Assistant | Anoop Baliga | Finds answers, drafts customer email replies, never sends without you | https://x.ai/bot/marketplace/bots/customer-question-drafter | S: none listed. R: none listed. I: Slack, Gmail, Granola. A: HARD NEVER-SEND: Never post Slack or send email unless the owner explicitly says to send THAT specific message. / Draft only. / ANSWER FIRST, THEN SUPPORT: Always draft the owner's own first response. |
| Customer Call Coach & Assistant | Anoop Baliga | Pre-call briefs and post-call coaching | https://x.ai/bot/marketplace/bots/customer-call-coach | S: none listed. R: Friday Coach Refresh. I: Granola, Slack, Gmail. A: Search, read, draft, and manage email. |
| Account Research Desk | Anoop Baliga | Researches target companies, writes pre-call briefs and account plans | https://x.ai/bot/marketplace/bots/account-book | S: Getting started; Build the account list; Account brief before a call; Week ahead call prep; Stakeholder map; Incumbent and competitor check; Account signals refresh; Open threads and next steps; Account usage and health; Outreach and follow-up drafts; Account plan. R: Weekly account signals; Weekday call prep; Friday open threads review. I: slack, notion-workspace, linear, hex, Databricks SQL, Gmail, Google Calendar, Granola, Google Drive, Google Sheets, Salesforce. A: Fixed conventions: an open thread is open, waiting on them, waiting on us, or closed, and every one carries an owner and the date it was raised. / A tool at an account is confirmed, likely, or unknown, and confirmed means a public source names it. / Post a brief or plan you approved to the channel your deal team reads. |
| Partnerships Call Coach | Jenna Nanpei | Coaches partnership/discovery calls from real transcripts | https://x.ai/bot/marketplace/bots/dan-lanning | S: none listed. R: Post-pitch call review. I: Notion, Google Calendar. A: not visible |
| Lead Pipeline Desk | Miguel Cruz | Scores inbound leads, merges duplicates, assigns owners, flags stuck | https://x.ai/bot/marketplace/bots/leadsworth | S: Getting started; Build the lead ledger; Score and qualify leads; Merge duplicate leads; Route leads and draft the first reply; Pipeline health report; Connect a tool or change the source. R: Daily lead triage; Weekly pipeline report. I: slack, notion-workspace, linear, hex, Databricks SQL, Gmail, Google Sheets, Salesforce. A: Working state lives in files, not in memory: the lead ledger with one row per lead, a dated copy of the ledger saved before every merge, the dated pipeline reports, and the unsent reply drafts. / Save first replies as unsent drafts in your own account. |
| Paid Media Report Desk | Miguel Cruz | Combines Google Ads/Meta/LinkedIn exports into weekly report | https://x.ai/bot/marketplace/bots/tally | S: Getting started; Map an export; Answer a reporting ask; Weekly paid media report; Monthly paid media report; What moved and why. R: Reporting ask watch; Weekly paid media report; Monthly paid media report. I: slack, notion-workspace, linear, hex, Databricks SQL, Gmail, Google Sheets. A: Working state lives in files, not in memory: the column map with one row per platform header, the dated exports exactly as they were handed over, the metrics history with one row per period per platform per campaign, the dated reports, and the ask log with one row per reporting ask, the draft I wrote, and whether it went out. / One platform's attributed conversions are never added to another platform's unless the use |
| Luma Pages | Jenna Nanpei | Builds/updates private Luma event pages synced to event briefs | https://x.ai/bot/marketplace/bots/luma-pages | S: none listed. R: none listed. I: Notion. A: not visible |
| WTD | Jenna Nanpei | Plans/tracks VIP hospitality for marketing ops, no private notes exposed | https://x.ai/bot/marketplace/bots/wtd | S: VIP AE nomination sheet; Deck QA standards; GTM branded deck; Email reply standards; Comms source of truth; Outstanding asks review. R: VIP Plan status refresh. I: Notion, Slack, Gmail, Google Drive. A: Never send external Slack or email without the owner's explicit OK. / Recorded notes and private transcripts stay personal — never on the hub. / When creating a new version of a Notion strategy page or decision brief, always create a NEW page — never overwrite the prior version in place. |
| Event Producer | Jenna Nanpei | Event details to run of show, guest list, day-of checklist | https://x.ai/bot/marketplace/bots/event-producer | S: Getting started; Build the event brief; Run of show; Vendor and venue tracker; Guest list and invites; Guest travel and hotels; Day-of checklist; Post-event recap. R: Event countdown check; Day-of brief; Post-event recap draft. I: slack, notion-workspace, linear, figma, Gmail, Google Calendar, Google Sheets. A: Fixed value lists: vendor status is quoted, held, contracted, deposit paid, confirmed, or cancelled. / Guest status is invited, registered, waitlisted, declined, attended, or no show. / A guest marked opted out is never invited, reminded, or mailed again, and that flag survives every new list. |
| Ad Spend Watch | Miguel Cruz | Monitors ad spend to flag problems, never pauses campaigns without approval | https://x.ai/bot/marketplace/bots/fuse | S: Getting started; Set accounts and thresholds; Read an ad platform export; Pull numbers from a connected source; Run the spend and performance check; Diagnose what broke; Check budget pace; Write the fix list; Answer a spend question. R: Daily spend and performance check; Midday burn check; Weekly budget pace check. I: slack, notion-workspace, linear, hex, datadog, sentry, figma, Gmail, Google Sheets. A: not visible |

# Persona lines

## dr eggbot (dr-eggbot-v2)
P: 

## Projects Manager (projects-manager)
P: Import Bot

## Outbound Prospecting (pg)
P: Import Bot

## SEO & AEO Desk (seo-aeo-desk)
P: Import Bot

## Haggle Bot (haggle-bot)
P: Import Bot

## Recruiting Coordinator (mr-toms)
P: Import Bot

## Stills & Clips Desk (image-gen-bot)
P: Import Bot

## figma bro (figma-bro)
P: Import Bot

## GTM Loop Closer (follow-through-agent)
P: Import Bot

## Sales Call Coach (sales-call-coach)
P: Import Bot

## Meeting Recap Deck (echo)
P: Import Bot

## AI Search Visibility (ai-search-visibility)
P: Import Bot

## Lingxi's Engineer Bot (engineer-bot)
P: Import Bot

## tinkabot (tinkabot)
P: Import Bot

## Critiquito: Design Critique (critiquito)
P: Import Bot

## Talent Discovery (sherlock)
P: Import Bot

## Cooper (cooper)
P: Import Bot

## Director Bot (video-director)
P: Import Bot

## Video Editor (video-editor)
P: Import Bot

## Distro Bot (distro-bot)
P: Import Bot

## Proto Bot (proto-bot)
P: Import Bot

## Sell Bot (sell-bot)
P: Import Bot

## Startup QA Bot (startup-qa-bot)
P: Import Bot

## Pfp Bot (pfp-bot)
P: Asks for more photos when unsure, and never makes realistic likenesses or posts anything.

## Import Bot (import-bot)
P: Import Bot

## Stalk Bot (stalk-bot)
P: 

## EBR & Value Deck Builder (ebr-value-deck-builder)
P: Import Bot

## Signal Prospector (signal-prospector)
P: Import Bot

## Nightly Audit Engineer (nightly-audit-engineer)
P: Import Bot

## Office Ops Desk (office-ops-desk)
P: Import Bot

## Event Request Desk (event-request-desk)
P: Import Bot

## Call Follow-Ups (call-follow-ups)
P: Import Bot

## Apple Search Ads Review (apple-search-ads-review)
P: Import Bot

## Hiring Signals (hiring-activity-monitor)
P: Import Bot

## GTM Connections (warm-intro-finder)
P: Import Bot

## Pipeline Pulse (pipeline-health-and-forecast)
P: Import Bot

## Deal Inspector (deal-qualification)
P: Import Bot

## GTM Prospecting (prospector)
P: Import Bot

## GTM Account Research (account-research)
P: Import Bot

## dial bot (dial-bot)
P: Import Bot

## skippy (skippy)
P: Import Bot

## Writing Bot (writing-bot)
P: Import Bot

## Tech Demos (tech-demos)
P: Import Bot

## Executive Assistant (frank)
P: Import Bot

## Company Docs Q&A (company-docs-q-a)
P: Import Bot

## Product Support Inbox Assistant (customer-question-drafter)
P: Import Bot

## Customer Call Coach & Assistant (customer-call-coach)
P: Import Bot

## Account Research Desk (account-book)
P: Import Bot

## Partnerships Call Coach (dan-lanning)
P: Import Bot

## Lead Pipeline Desk (leadsworth)
P: Import Bot

## Paid Media Report Desk (tally)
P: Import Bot

## Luma Pages (luma-pages)
P: Import Bot

## WTD (wtd)
P: 

## Event Producer (event-producer)
P: Import Bot

## Ad Spend Watch (fuse)
P: Import Bot
