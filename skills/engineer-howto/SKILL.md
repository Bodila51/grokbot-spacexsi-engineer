# engineer-howto

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate.

## Steps
1. Resolve the person to a handle via kb/people/, data/handles.txt or data/handles_general.txt (or data/handles.json if present). If absent, say so and offer the closest people who are.
2. Read kb/people/<handle>.md and the matching kb/recipes/<task>.md (multi-bot-teams, coding-and-review, memory, content-and-x, sales-gtm, design, routines, phone-voice); fall back to data/posts.jsonl if present.
3. Only if kb is thin: one X search `from:<handle> <2-3 keywords> since:<30 days ago>`.
4. Build the answer only from that person's own public material. If they have none: "N has no public material on T", then who does.
5. Compare mode: one row per person with the same columns.
6. Add a ready recipe for the asker's setup ((what it means for the owner, value high/medium/none, ready recipe; rules in kb/personal-analysis.md if present)).

## Return
```
How N does it: <2-4 lines>
What they publish: <bot / skill / repo — link>
How to apply it: 1. … 2. … 3. …
Recipe: <ready prompt / routine / skill> — reply "yes"
Sources: <links>
```
Compare mode: table `Who | Approach | Tool | Source`, then "What to take" in 3 steps.

## Validate
Every claim links to the person's own material; nothing from others is attributed to N; third-party summaries are labelled.

## Approval
Read-only. Installing anything is a suggestion until the owner says "yes".
