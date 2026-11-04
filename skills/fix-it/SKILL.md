# fix-it

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate.

## Steps
1. Pin down the symptom in one line: what broke, since when, which bot / routine / skill / connector, the exact error text if any.
2. Gather evidence cheaply, in this order:
   - The routine's saved prompt, trigger and recent runs (if it is your own routine) or the owner's description and screenshots.
   - The skill's text (look for missing files, renamed tools, hard-coded schemas, wrong paths, outdated limits).
   - Connector status (needs auth, error, missing), approvals that were denied or expired, usage limits hit.
   - Transcripts of the failing run, if available.
3. Compare with kb/changelog.md and kb/features.md for recent changes in that area (renamed settings, new limits, changed behavior), and with kb/known-issues.md and team posts (kb/people/, data/posts.jsonl if present). Fetch the changelog top live only if kb is older than 3 days.
4. Name the most likely cause, with evidence. If two causes are possible, list both and the one check that tells them apart.
5. Propose a fix as a ready recipe: the exact new prompt text, schedule, skill edit, reconnect step or setting, plus how to verify it worked (a one-off test run).

## Return
```
What broke: <one line>
Cause: <most likely, with evidence>
Related release: <version/date or "not found">
Fix (reply "yes"): <exact change>
How to verify: <test>
Sources: <links>
```

## Approval
Diagnosis is read-only. Any change to a routine, skill, bot, connector or setting waits for the owner's explicit "yes", then is applied once and verified.
