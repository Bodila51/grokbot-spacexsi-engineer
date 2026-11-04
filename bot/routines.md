# Routines for SpaceXAI Engineer (time zone Europe/Kiev)

The bot's computer uses your time zone (v0.53.0). If Settings shows a different zone, put it right first.

Create each routine by sending the prompt to the SpaceXAI Engineer bot. Before scheduling, test the skill once by hand. The docs advise scheduling only after a one-off run is reliable.

## 1. daily-scan, every day at 09:00
Prompt to the bot:
```
Create a routine named "Daily Grok Bot scan": every day at 09:00 Europe/Kiev, run the skill "daily-scan" using /workspace/spacexai-engineer/. Send the digest in this chat only if there is something new (max 8 items). Never post, reply or message anyone. If a source is blocked, note it in the digest and continue.
```

## 2. setup-audit, Mondays at 10:00
Prompt to the bot:
```
Create a routine named "Weekly setup audit": every Monday at 10:00 Europe/Kiev, run the skill "setup-audit". You may send each of my own bots one read-only question asking for its role, rules, skills and routines. Change nothing. Save the report to /workspace/spacexai-engineer/kb/audits/ and send me the table with up to 15 numbered suggestions.
```

## Notes
- Both are well within the limits: 50 routines per bot, at least 5 min apart, 300 runs/h (docs/skills-routines-and-automations).
- On Mondays, daily-scan at 09:00 runs before the audit at 10:00, so the audit sees fresh features.
- Each run uses your weekly usage. setup-audit costs more, because 15 bots reply.
- To pause: "Pause the routine Weekly setup audit" (v0.52.0).
