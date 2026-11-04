# whats-new

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate.

## Steps
1. Start date: as asked, default 7 days ago. Optional topic filter.
2. Use kb only: kb/changelog.md, data/posts.jsonl if present, "Recent posts" in kb/people/. If kb/state.json last_scan_utc is older than 24 h, fetch only the top of https://x.ai/changelog/bot once (no X reads, no browser).
3. Group: Big features · Multi-bot and routines · Connectors and apps · Security and payments · Team/Enterprise (only if asked) · Practices from engineers. Drop minor items unless asked for everything.
4. For each item, add "what it means for you" and a ready recipe (what it means for the owner, value high/medium/none, ready recipe; rules in kb/personal-analysis.md if present), from the asker's context.

## Return
At most 10 items, most valuable first:
`• <date> · <vX or @handle> — <what> — for you (value X): <use or "you don't need this"> — recipe: "yes N". <link>`
Then: "Full list: kb/changelog.md".

## Validate
Each item has a version and date or a post link; none older than the start date; changelog page dates win over X "stable" posts (say if they differ).

## Approval
Read-only. Recipes apply only after the owner's "yes".
