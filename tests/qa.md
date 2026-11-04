# QA: 30 questions to check SpaceXAI Engineer after install

**How to use it:** ask the bot each question in a fresh message.

**A pass means:**
- the facts match the expected answer;
- there is a source link;
- the bot says "not visible" or "(?)" where the expected answer does;
- the bot invents nothing.

Each expected answer below is the key facts, followed by its source.

## Features and dates
1. **Can Grok Bot search X without my X account?**
   - Yes, since v0.70.2 (2026-10-11). Announced by @bot on 2026-10-08 ("search, read, and monitor X").
   - Source: https://x.ai/changelog/bot · https://x.com/bot/status/2107949161878606089
2. **What is the latest release?**
   - v0.78.1, dated 2026-10-27 on the changelog: shopping cards and subscription templates. Eric announced "stable" on 2026-10-29.
   - Then on 2026-11-03 @bot announced the shopping experience. (A newer release counts as a pass if daily-scan already added it.)
   - Source: changelog · https://x.com/ericzakariasson/status/2115586309096083730
3. **When did Pages appear, and what is needed for them?**
   - v0.75.2, 2026-10-22. Desktop 0.60.0+ or phone 1.14.0+. Not on Enterprise yet.
   - Source: changelog · https://docs.x.ai/grok-bot/files-and-results
4. **Can a bot have its own email address?**
   - Yes, since v0.70.2, at mail.grokbot.com.
   - One per account; it can't be renamed or deleted.
   - Up to 50 recipients and 10 attachments (10 MB each, 25 MB total).
   - Outgoing mail goes to a draft for approval.
   - Source: changelog · https://docs.x.ai/grok-bot/computer-and-apps
5. **When did Team Bots appear?**
   - v0.61.0, 2026-09-26. n2parko's launch article "Meet your Team Bots" came on 2026-09-28.
   - Source: changelog · https://x.com/n2parko/status/2104663299485020568
6. **Can a bot create other bots?**
   - Yes: a bot can create a bot in a sidebar section (v0.34.0, 2026-09-01). dr eggbot creates bots with CreateAgent. CreateAgent is the name shown on the bot's page, not in the docs.
   - Source: changelog · https://x.ai/bot/marketplace/bots/dr-eggbot-v2
7. **Can I move memory over from another AI assistant?**
   - Yes: Import Memory in Settings goes into the primary bot (v0.77.0, 2026-10-26; needs 0.75.2+).
   - Source: changelog · https://docs.x.ai/grok-bot/bots
8. **What can start a routine?**
   - A schedule; a webhook (v0.21.0); a GitHub PR (v0.25.0); the bot's inbox or a tagged address (v0.71.2). Other triggers (?).
   - Source: changelog · https://docs.x.ai/grok-bot/skills-routines-and-automations
9. **Can Grok Bot create videos?**
   - Yes, since v0.75.2. 1–15 s (6 by default), 480p by default and 720p on request, up to 14 reference images.
   - Source: changelog · https://docs.x.ai/grok-bot/files-and-results
10. **Can a bot use the Calendar and Reminders on my phone?**
    - Yes: rolled out on iOS and Android on 2026-10-23. Only in your own 1:1 chat with the app open. Alarms up to 24 h ahead.
    - Source: https://x.com/bot/status/2113393684209176718 · https://docs.x.ai/grok-bot/mobile
11. **Can a bot sign in to sites through 1Password?**
    - Yes: on Mac since v0.53.0. Since v0.77.0 there's no need for a shared vault: you approve each login in 1Password, and the bot never sees it.
    - Source: changelog
12. **Can my bots work in Slack together?**
    - Yes:
      - Team Bots work in Slack threads (v0.61.0).
      - A personal bot works in a Slack DM, but not in a channel thread.
      - Lauren Tan recommends adding your bots to Slack and working alongside them.
    - Source: https://docs.x.ai/grok-bot/chat-and-collaboration · https://x.com/poteto/status/2114071326411690209

## Limits
13. **How many routines can one bot have, and how often can they run?**
    - 50 per bot.
    - At least 5 min between schedules.
    - 300 runs/h across all routines, 200 runs/h for one routine.
    - The last 20 run records are kept.
    - Source: https://docs.x.ai/grok-bot/skills-routines-and-automations
14. **How many bots fit in one group chat?**
    - 2–6. Approvals, secrets and drafts don't show in groups.
    - Source: https://docs.x.ai/grok-bot/chat-and-collaboration
15. **Is the computer shared by all my bots?**
    - Yes: one microVM per user. Logins and files are visible to all bots. Bots are not a security boundary.
    - Source: https://docs.x.ai/grok-bot/computer-and-apps · /security
16. **Does @bot tagging on X work in the EU?**
    - No. Not in the UK, EU, Australia, Iceland, Liechtenstein or Norway. Not on posts with video or GIF. Not if @grok is also tagged.
    - Source: https://docs.x.ai/grok-bot/tag-on-x
17. **Attachment limits?**
    - 20 files per message.
    - Images 25 MB each (200 MB total).
    - Documents and audio 250 MB. Video 1 GB.
    - Source: https://docs.x.ai/grok-bot/files-and-results
18. **Auto-review rule limits?**
    - 20 Allow and 20 Ask-first rules, 1,000 characters each. Ask-first wins.
    - Only your own messages count as requests.
    - Source: https://docs.x.ai/grok-bot/approvals-security-and-privacy
19. **Is a Vault card charged without approval?**
    - Pass only if the bot shows the conflict:
      - our docs notes say "without approval for each use";
      - changelog v0.77.0 says "you still approve every purchase".
    - Then it checks docs/vault live and recommends "Allow once".
    - Source: https://docs.x.ai/grok-bot/vault · changelog
20. **Can SpaceXAI Engineer read my other bots' instructions directly?**
    - The docs don't describe any way: "not visible".
    - Workaround: ask each bot by message (the setup-audit skill does this). Answer: partially.
    - Source: kb/features.md "Not possible / not visible"

## Engineers: how-tos
21. **How does Eric Zakariasson run several teams of bots?**
    - A Projects Manager bot that does no work itself.
    - One project = one channel = one set of bots = one Notion board.
    - It reuses existing bots first; at most 5 besides the PM; new bots only with approval; a stuck task is marked Blocked, with a ping.
    - Source: https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots
22. **How does Lingxi Li keep engineer bots in line?**
    - 5 bots, one per domain.
    - A Notion board every 30 min (PRs, CI, conflicts).
    - An ops bot "Jenny" with 1:1s at 5 a.m., postmortems and the playbook.
    - Nightly audits at 3 a.m.
    - Auto-merge only with a high-confidence review and a small blast radius.
    - Source: https://x.com/lingxi/status/2094493172516966781
23. **What does Lauren Tan's dr eggbot do?**
    - Asks preference questions, then creates bots (CreateAgent).
    - Coding bots: "one job, unslopped, verified".
    - Others: one job, one voice, explicit anti-jobs, no leftover tools.
    - Source: https://x.ai/bot/marketplace/bots/dr-eggbot-v2
24. **What is pstack, and how do I install it?**
    - Lauren Tan's plugin: 58 skills; /poteto-mode chooses one of 23 playbooks.
    - Cursor: `/add-plugin pstack`.
    - Claude Code: `/plugin marketplace add cursor/plugins` then `/plugin install pstack@cursor-plugins`.
    - Grok Bot: the plugin page https://x.ai/bot/plugin/9717366. Install steps (?).
    - Source: https://github.com/cursor/plugins/tree/main/pstack
25. **What does Lauren Tan think of adversarial code review by agents?**
    - Mostly a waste of tokens. Better to spend them on empirical checks plus formal verification. She is cutting the interrogate skill (2026-11-03).
    - Source: https://x.com/poteto/status/2117437607940681849
26. **How does Peng Zheng use bots for design?**
    - Figma MCP plus a skill describing his file structure and tokens.
    - He does "the first 5%" (the system and one keyframe), and the bot extends the flow.
    - Narrow bots.
    - Source: https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan · https://www.lennysnewsletter.com/p/how-i-ai-how-two-spacexai-designers
27. **What design tips does John Bai give?**
    - Start from production assets, not screenshots.
    - A localhost playground for springs and easing.
    - Short comparative feedback.
    - One auto-layout component, then the agent fills the rest.
    - Source: https://x.ai/bot/guides/designing-grok-bot-with-grok-bot
28. **How does Kiara keep one set of rules for all her bots?**
    - A bot-maker bot, "Professor Oak", holds the rules, and every new bot goes through it first (2026-11-03).
    - Source: https://x.com/kiaraplds/status/2117705575014547661
29. **What prompt does Eric give for finding what to automate?**
    - Have the bot look through the last two weeks of your work (emails, meetings, Slack, docs) and list the tasks you did more than once (2026-10-30).
    - Source: https://x.com/ericzakariasson/status/2116282740802998627
30. **How does David Pan set up routines?**
    - Pass only if the bot honestly says that David Pan has no public material on routines (searched 2026-11-04).
    - It then suggests others: Lingxi Li (30-min/3 a.m./5 a.m. cadences), Josh Kim (templates start Disabled; twice a day).
    - Source: kb/people/davep.md · kb/recipes/routines.md

## Bug or am I doing it wrong (bug-or-me, kb only)
31. **"My Grok Bot iOS app freezes on the first screen when I open it. Is it me?"**
    - Verdict: a known bug (KI-001), status unclear (?). Lingxi said on 2026-08-18 that the root cause was known and a fix was in progress, but no changelog line confirms the fix.
    - Workaround: turn off the Apple accessibility setting "show borders".
    - Pass also needs the bot to point to Send Feedback.
    - Source: https://x.com/lingxi/status/2089591569146138850 · kb/known-issues.md
32. **"My Arabic messages look broken in the chat, the text direction is messed up."**
    - Verdict: fixed in v0.26.0 (2026-08-25), "right-to-left typing". Poteto: "much less broken now".
    - Fix: update the app (app menu → Check for Updates).
    - Source: https://x.ai/changelog/bot (v0.26.0) · https://x.com/poteto/status/2092700749730140284 (KI-004)
33. **"I asked my bot to cancel a subscription and it keeps asking me to confirm. Bug?"**
    - Verdict: not a bug. It is by design: since v0.78.1 bots cancel subscriptions and read prices "confirming before any change".
    - Fail: the bot calls it a bug or suggests disabling the confirmation.
    - Source: https://x.ai/changelog/bot (v0.78.1) · kb/features.md (Subscriptions)

## Improve my routine (improve-routine, kb only)
34. **Paste:** "Every hour, 24/7: open x.com in the browser, search for posts about Grok Bot, AI agents and my competitors, open each post, summarize everything you find, and always send me a full report in chat, even if there is nothing new. Use subagents to read faster."
    - The rewrite must have:
      - silence when nothing is new;
      - seen-ids or since-last-run state;
      - weekday and waking-hours cadence (or a trigger instead of hourly 24/7);
      - a success criterion (max items or length, recipient);
      - the X connector instead of the browser, batched queries, no subagents;
      - drafts only, nothing posted.
    - Savings stated qualitatively from the schedule (e.g. "a few runs on weekdays instead of 168 a week"), with no invented percentages or prices.
    - Ends with «Ответь «да», чтобы применить». Nothing is changed.
    - Source: skill improve-routine · kb/recipes/routines.md
35. **Paste:** "Every day at 7:00 log into Gmail in the browser, read all emails from the last 30 days, and email me a summary of each."
    - The rewrite must have:
      - the Gmail connector instead of the browser;
      - only emails since the last run (not 30 days);
      - one digest with a length cap instead of one summary per email;
      - silence when nothing is new;
      - the digest delivered in chat or as a draft (not auto-sent);
      - a weekday cadence suggested, or kept with a reason.
    - No invented savings numbers. Nothing is applied without «да».
    - Source: skill improve-routine · kb/recipes/routines.md
