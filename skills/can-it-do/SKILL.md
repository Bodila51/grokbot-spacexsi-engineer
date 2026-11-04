# can-it-do

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate.

## Steps
1. Restate the need in one line: what should happen, where (app, phone, Slack, X), personal or Team Bot.
2. Answer from kb first, immediately: search kb/features.md (with synonyms: "schedule" = routine, "remember" = memory, "login" = Vault/1Password), its "Not possible / not visible" section, kb/changelog.md, kb/recipes/, kb/known-issues.md.
3. Fetch https://docs.x.ai/grok-bot/ or https://x.ai/changelog/bot live only if kb has nothing on it or the kb entry is older than 7 days. One or two fetches, no browser, no subagents.
4. Decide:
   - **Yes:** documented or released.
   - **Partly:** possible with limits (plan, device, region).
   - **No:** the docs say so, or it is absent after checking kb, docs and changelog. Say "not found in docs/changelog as of <date>", never "impossible", unless the docs say it.
5. Add a ready recipe for the asker's setup ((what it means for the owner, value high/medium/none, ready recipe; rules in kb/personal-analysis.md if present)): a prompt, routine or skill they accept with one "yes", or the closest workaround from kb/recipes/ or the marketplace.

## Return
```
Yes / No / Partly — <one line>
Limits: <limits, plans, devices, since vX>
Who does it: <engineer + link, if any>
Recipe for you: <ready prompt / routine / skill> — reply "yes"
Source: <links>
```

## Validate
Every yes/partly has a dated source; every no lists what was checked; nothing beyond what the source says.

## Approval
Read-only. Applying a recipe needs the owner's "yes".
