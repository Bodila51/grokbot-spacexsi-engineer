# bug-or-me

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate. Usage: kb only; no X reads, no browser, no subagents. Fetch the top of https://x.ai/changelog/bot once only if kb/state.json is older than 3 days.

## Steps
1. Restate the problem in one line: what they did, what they expected, what happened, platform and app version if given.
2. Search kb/known-issues.md (symptom keywords and synonyms).
3. Search kb/changelog.md "fixed" and "improved" lines and kb/features.md (limits, "Not possible / not visible").
4. Search kb/recipes/ and kb/people/ for the right way engineers do the same thing.
5. Pick exactly one verdict:
   - **Known bug:** listed in known-issues and not marked fixed. Give the workaround and the source.
   - **Fixed in vX.Y.Z:** a changelog or team post says it was fixed. Tell them to update and how to check their version.
   - **Not a bug:** the docs, a documented limit or an engineer's practice show the expected behavior. Give the right way.
6. If evidence is thin or conflicting, say "not sure (?)", give the most likely verdict with what would confirm it, and suggest reporting it to the team via in-app feedback. Never invent a bug, version or fix.
7. If the owner confirms a new bug, append it to kb/known-issues.md with date, symptom, source "reported by owner" and (?).

## Return
```
Verdict: known bug / fixed in vX / not a bug (or + (?))
Why: <1-2 lines>
What to do: <workaround / update / the right way, as steps or a ready prompt>
Source: <links>
```

## Approval
Read-only. Changing anything in the owner's bots waits for their "yes". For a broken routine or skill with a concrete error, use fix-it.
