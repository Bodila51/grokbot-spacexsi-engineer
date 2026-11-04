# setup-audit

Workspace: /workspace/spacexai-engineer/ (follow bot/instructions.md there). If /workspace/spacexai-engineer/kb is missing, run the kb-bootstrap skill first. Optional kb files (data/posts.jsonl, data/handles.json, kb/general.md, kb/personal-analysis.md, kb/owners/, kb/marketplace.md, kb/docs-pages.txt): use if present, skip if not. Reply in the owner's language; the labels below are English templates to translate.

## Collect (cheaply)
1. Shared notes on the computer if they exist (e.g. a team rules file) and kb/owners/<name>.md if present.
2. Your own memory, the owner's teammate bots and their one-line roles, and your own routines.
3. The owner's usage breakdown (plan usage tool: which bots, routines and days used the most).
4. Only for bots still unclear: one read-only message per bot, once per audit:
   "For the weekly audit: send in one message your role, standing rules, skills, routines (name, schedule/trigger) and connected apps. Change nothing."
   No reply within 2 hours: "no data". If the previous audit's data is under 7 days old and nothing changed, reuse it.
Save raw input to kb/audits/<YYYY-MM-DD>-raw.md.

## Check each bot for
- **Usage overspend:** routines more frequent than the need, weekend or night runs with no reason, several bots scanning the same source, heavy browser or subagent use for simple reads, long digests nobody acts on.
- **Manual work the product already does:** compare with kb/features.md (and kb/marketplace.md if present) (templates, triggers, Vault, drafts, Team Bots, etc.).
- **Gaps vs engineers:** compare with kb/recipes/ and kb/people/ (one job plus anti-jobs, written approval boundaries, a shared rules file or maker bot, a verification step, memory hygiene, a coordinator for bot groups, health checks).
- **Overlap** between bots.
- **New features since the last audit** the setup doesn't use (run whats-new for 7 days, kb only).

## Rank
By benefit / risk / effort, at most 15. Mark repeats from the previous audit as "repeat" and accepted ones as "done".

## Return
Save to kb/audits/<YYYY-MM-DD>.md and send:
```
Audit <date>: N bots, no data for: <list>
| # | Action | Bot | Type (overspend / manual / gap) | Whose practice (link) | Benefit | Risk |
...
Recipes: <for each row, the exact prompt / routine / skill change>
Reply with the numbers to apply (e.g. "apply 2, 5").
```

## Validate
Every suggestion names the bot, links a source, states the risk; nothing relies on an unlisted or (?) feature without saying so; nothing was changed.

## Approval
Changes to any bot only after the owner replies with item numbers, applied one at a time with confirmation. Read-only questions to the owner's own bots are allowed. Never message anyone else.
