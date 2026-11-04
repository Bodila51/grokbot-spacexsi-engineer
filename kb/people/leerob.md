# Lee Robinson (@leerob)
- Role / team: SpaceX Superintelligence (prev Cursor, Vercel/Next.js); role not visible; teaching and DevRel ([source](https://x.com/leerob))
- Links: [X](https://x.com/leerob), [site](https://leerob.com), [GitHub](https://github.com/leerob)
- Confidence: high
## Key ideas
- Plan first (save plans in `.cursor/plans/`); keep rules in `.cursor/rules/` short and add one only after the agent repeats a mistake; skills (SKILL.md) load on demand; a "stop" hook in `.cursor/hooks.json` loops until tests pass; parallel agents in worktrees — [Cursor blog](https://cursor.com/blog/agent-best-practices) (2026-01-09)
- Complexity budgets: moved cursor.com off its CMS for about $260 of tokens in ~3 days; content in git; written plan then parallel subagents; screenshots to verify — [leerob.com/agents](https://leerob.com/agents) (Dec 2025)
- Built a Rust image library only with agents; AGENTS.md added only after repeated errors; tests, lints and CI loops; advice: do not over-optimize — [leerob.com/pixo](https://leerob.com/pixo) (Dec 2025)
- Agents carry knowledge through rules and skills files — [leerob.com/model-behavior](https://leerob.com/model-behavior) (Jul 2026)
## Bots, skills, plugins
- pixo — Rust image library written with agents — https://github.com/leerob/pixo — 477 stars
- mcp-servers — fork only — https://github.com/leerob/mcp-servers — 21 stars
- No skills of his own found.
## Copy this in Grok Bot
1. Tell your bot: plan first and save the plan before editing.
2. Add a rule to the bot only after it repeats the same mistake; keep rules short.
3. Put stable how-tos into skills so they load on demand.
4. Add a loop that keeps going until tests pass, and have the bot verify with screenshots.
## Sources
- https://x.com/leerob
- https://cursor.com/blog/agent-best-practices
- https://leerob.com/agents
- https://leerob.com/pixo
- https://leerob.com/model-behavior
- https://github.com/leerob/pixo

## Recent posts about Grok Bot (paraphrased; seen 2026-11-04)
- 2026-10-24: Asks for Grok Bot bug reports/feature ideas; will pay 5 replies $100 via X Money — https://x.com/leerob/status/2113792409448714468
- 2026-10-15: Cursor Projects is like "Grok Bot for Coding": same architecture with more visibility into subagents — https://x.com/leerob/status/2110730965056131375
- 2026-10-09: Stanford CS146S lecture on how always-on proactive agents like @bot work (chaptered video) — https://x.com/leerob/status/2108650243365736855
- 2026-09-30: Asks for Grok Bot feedback/feature requests — https://x.com/leerob/status/2105127956742132156

## Recent posts about Grok Bot (merge of posts.jsonl, paraphrased; added 2026-11-04)
- 2026-08-22: Trust design: LLM reviews every action, asks approval if unexpected, plus customizable rules — https://x.com/leerob/status/2091265397056016677
