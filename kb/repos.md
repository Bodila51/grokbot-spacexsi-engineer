# Repos (fetched via github.com HTML + raw.githubusercontent.com, 2026-11-04; branch main)

## poteto/how - https://github.com/poteto/how - 953 stars (49 forks), MIT
- Skill: `how` - explains how a subsystem/feature/flow works; two modes: Explain (default) and Critique (explain, then several critics on different models review the architecture).
- Install: README gives no command; it is a Cursor plugin (.cursor-plugin/plugin.json). `npx skills add poteto/how` is untested (?).
- SKILL.md: https://raw.githubusercontent.com/poteto/how/main/skills/how/SKILL.md (references/: explainer-prompt.md, explorer-prompt.md, critic-prompt.md, critique-rubric.md)
- Rules: if the question is ambiguous, state your interpretation and explore, do not ask. Simple question = one agent; complex = 2-4 parallel explorers then one explainer. Read real code, do not guess from file names. Explainer output is the product; lightly edit only. Output sections: Overview, Key Concepts, How It Works, Where Things Live, Gotchas. Critique spawns critics in one message on different models (opus, composer-2, gpt-5.4 per file).

## poteto/brainmaxxing - https://github.com/poteto/brainmaxxing - 362 stars (11 forks), MIT
- Persistent-memory markdown/Obsidian vault `brain/` for Claude Code, 16 starter principles, 2 hooks (inject brain index at start, rebuild on change).
- Skills (6, under .agents/skills/<name>/SKILL.md): brain (read/write vault files, every note reachable from brain/index.md); reflect (end of session or after a correction, write learnings); ruminate (mine past conversations for missed patterns); meditate (audit/prune brain, derive principles, review skills); plan (phased plans into brain/plans/, planning only); review (principle-grounded review of code/plans, numbered issues with severity).
- Install: no CLI; tell Claude Code: "Install brainmaxxing from https://github.com/poteto/brainmaxxing into this project." It copies brain/, .agents/skills/, .claude/hooks/ (+ merges settings.json), appends CLAUDE.md instructions.
- Paths: https://raw.githubusercontent.com/poteto/brainmaxxing/main/.agents/skills/{brain,reflect,ruminate,meditate,plan,review}/SKILL.md
- Rules (brain/plan/review/meditate): add to brain only what genuinely improves future work, speculative content degrades everything; plan = no implementation, delegate exploration to subagents, read principles fresh not from memory; review = no changes, options labelled A/B/C, new behavior needs tests asserting outcomes; new principles need 2+ supporting notes and be independent and actionable; shut down agents when done (ruminate).

## ericzakariasson/skills - https://github.com/ericzakariasson/skills - 22 stars (2 forks), MIT
- Skills: game-builder (planner/builder/critic loop building homage games until captures match real shipped-game screenshots); game-builder-blender-assets (companion: hero 3D assets in Blender to GLB, one asset per subagent); grok-bot-story (builds a user's Grok Bot activity story Page ending in a share card).
- Install: `npx skills add ericzakariasson/skills` ; single: `npx skills add ericzakariasson/skills --skill game-builder` ; list: `npx skills add ericzakariasson/skills --list`
- Paths: https://raw.githubusercontent.com/ericzakariasson/skills/main/skills/{game-builder,game-builder-blender-assets,grok-bot-story}/SKILL.md
- Rules (game-builder): orchestrator never builds or scores; refs are real screenshots locked in refs-locked/, never shipped in the game; WIN only when a fresh critic says so and all Visual Bar criteria pass; round count is never a reason to stop; repeating the same punch list is not progress. Blender companion: prefer 2D when refs are 2D, one noun per specialist, orchestrator alone owns turnaround gates. grok-bot-story: every number from user's own data, never invented; one question widget max; needs Python 3.9+.

## lilingxi01/auto-critique - https://github.com/lilingxi01/auto-critique - 2 stars (0 forks)
- Cursor plugin, 2 skills: auto-critique (reviewer-style critiques on current diff, one per round: finder, verifier, parent applies fix); learn-critique (records every corrective callout into notes at ~/notes/auto-critique/).
- Install: Cursor local: `ln -sf /path/to/auto-critique ~/.cursor/plugins/local/auto-critique` then reload. npx: `npx skills add lilingxi01/auto-critique -g -a cursor --skill '*' -y` (one skill: `--skill auto-critique`). Note: notes substrate is not bundled.
- Paths: https://raw.githubusercontent.com/lilingxi01/auto-critique/main/skills/auto-critique/SKILL.md ; .../skills/learn-critique/SKILL.md
- Rules: finder returns exactly one candidate or none, highest impact first (structure/data shape > naming > style); verifier uses /how and /why; parent edits directly, no delegating fix; empty diff = stop and report; learn-critique fires eagerly on any corrective callout, does not pause the main conversation, subagent cross-checks to collapse duplicates.

## benjitaylor/skills - https://github.com/benjitaylor/skills - 1,754 stars (124 forks)
- Skill: stageshow (v1.1.0) - builds faux product UI stills/animated cursor demos in React (windows, phones, bento grids), with kit, examples, film tool.
- Install: `npx skills add benjitaylor/skills --skill stageshow`
- Path: https://raw.githubusercontent.com/benjitaylor/skills/main/stageshow/SKILL.md (also stageshow/README.md, AGENTS.md, CLAUDE.md)
- Rules: use kit parts, never hand-draw windows/devices/bubbles; start from closest gold example and film it; budget of about 3-7 real strings per screen; story = 3-5 beats, 10-16 s, poster frame must tell the story alone; product studies borrow interaction, never another product's identity.
