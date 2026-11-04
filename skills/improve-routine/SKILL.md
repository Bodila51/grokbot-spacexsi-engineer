# improve-routine

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate. Usage: kb only; no X reads, no browser, no subagents.

## Inputs
The pasted routine or skill prompt, plus its schedule or trigger if given. Read kb/recipes/routines.md, kb/recipes/ for the task area, kb/people/ cards, and kb/features.md (routine limits, triggers, connectors).

## Checklist (apply what fits)
1. **Silence when nothing new:** an explicit "if nothing new, send nothing" line.
2. **Read only what is new:** a state file or seen-ids, `since` = last run; stop paging at seen items.
3. **Sensible cadence:** match the schedule to when results are acted on; weekdays and waking hours unless there is a reason; an event trigger (webhook, email, Slack, GitHub) instead of polling where one exists.
4. **Clear success criterion:** what a good run produces, the maximum length, and who receives it and where.
5. **Cheapest tool:** a connector over the browser, a plain fetch over the browser, batched queries over many single ones, no subagents for simple reads.
6. **Intent, not tool recipes:** no hard-coded tool schemas or arguments; describe what to do.
7. **Approval boundaries:** drafts instead of sends; nothing published or changed without a yes.
8. **Shorter:** remove repetition and vague words; keep one job per routine.
Attribute each change to an engineer's practice from kb with a link where one exists.

## Return
```
New prompt:
<the full rewritten prompt, plus schedule/trigger if changed>

What changed (3-5 lines):
• <change> — <why, practice + link>
Savings: <qualitative, from the change itself, e.g. "7 runs a week instead of 168" or "1 batched query instead of 10"; no invented percentages or prices>
Reply "yes" to apply.
```
If the prompt is already good, say so in one line and suggest at most one change.

## Approval
Nothing is applied until the owner says "yes"; then apply once to the routine or skill they named and confirm.
