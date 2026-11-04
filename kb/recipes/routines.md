# Recipe: routines and schedules

## Hard limits (docs)
- 50 routines per bot.
- At least 5 min between scheduled runs.
- 300 runs/h across all routines; 200 runs/h for one routine.
- The last 20 run records are kept.
- Triggers: schedule, webhook (v0.21.0), GitHub PR (v0.25.0), the bot's inbox / a tagged address (v0.71.2). Others (Slack, Linear, Sentry, PagerDuty) (?).
- Pause and resume (v0.52.0). Deleting is irreversible.

## Engineers' approaches side by side
| Who | Cadence | Source |
|---|---|---|
| Docs | Schedule it as a routine only once the one-off output is reliable. Save the process as a skill first. Routine example: "Every weekday at 8:00 AM, run the … skill". | [use cases](https://docs.x.ai/grok-bot/use-cases), [skills & routines](https://docs.x.ai/grok-bot/skills-routines-and-automations) |
| Lingxi Li | PR sweep every 30 min, audits at 3 a.m., bot 1:1s at 5 a.m. A P0 check every 5 min "burns tokens fast". | [guide](https://x.ai/bot/guides/grok-bot-for-engineering) |
| Josh Kim | Templates start Disabled (you press Enable). Twice a day (around 9:05 and 4:05), 0–5 drafts per run. Sending only after you type "send". | [guide](https://x.ai/bot/guides/grok-bot-for-work) |
| Blake Schuller (guide) | Daily brief at 8:30, checks every 15 min (call prep, unanswered asks). | [guide](https://x.ai/bot/guides/grok-bot-for-post-sales) |
| Lauren Tan | dr eggbot sets up two health checks: transcripts on weekdays, and routine token waste on Mondays. | [dr eggbot](https://x.ai/bot/marketplace/bots/dr-eggbot-v2) |
| Matt Palmer | Hourly watch for reservation openings. The bot found cancellations. | [post](https://x.com/mattyp/status/2116516547007308125) |

## Steps in Grok Bot
1. Run the task by hand → check it → "Save the process we just used as a skill called '…'".
2. "Create a routine: every weekday at 09:00 run skill '…'. Pause if the source is unavailable."
3. A health-check routine once a week: which routines produced nothing or burned too much (Lauren's pattern).
4. Routines that send anything work only through drafts and approval.

## Added from posts merge (2026-11-04)
- Keep routine frequency low (15-min ≈ 100 runs/day; hourly is usually enough), prefer event triggers — https://x.com/poteto/status/2091368467060662497
- Webhook trigger ideas: WhatsApp contact, Notion page change, sensor threshold — https://x.com/ericzakariasson/status/2095105948016882133
- Notify as soon as the bot can't progress; event triggers over cron — https://x.com/ericzakariasson/status/2092281851822113131
