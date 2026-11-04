# Recipe: coding and review

## Engineers' approaches side by side
| Who | Approach | Source |
|---|---|---|
| Lingxi Li | The bot starts Cursor cloud agents with her skills and a detailed prompt that says what proof it expects (before/after screenshots). It watches the transcript and unblocks the agent when it stalls. Every 30 min it checks each PR for Bugbot comments, CI and merge conflicts. A PR merges automatically only with a high-confidence review and a small blast radius (how much could break). Nightly audits at 3 a.m. produce cleanup PRs. | [article](https://x.com/lingxi/status/2094493172516966781), [Engineer Bot](https://x.ai/bot/marketplace/bots/engineer-bot), [Nightly Audit Engineer](https://x.ai/bot/marketplace/bots/nightly-audit-engineer) |
| Lauren Tan | pstack / poteto-mode: pick a playbook, then run the steps, with proof at every step. Adversarial review passes mostly waste tokens; spend them on empirical checks plus formal verification instead. Fix each correction at the strongest layer: architecture → lint/CI → rules/skills → style guide. | [pstack](https://github.com/cursor/plugins/tree/main/pstack), [post](https://x.com/poteto/status/2117437607940681849), [talk summary](https://redreamality.com/blog/lauren-tan-poteto-trust-before-parallel/) |
| Lee Robinson | Plan first. Add short rules only after the agent repeats a mistake. A hook loops until the tests pass. Run parallel agents in worktrees. Cursor Projects is "Grok Bot for Coding". | [blog](https://cursor.com/blog/agent-best-practices), [post](https://x.com/leerob/status/2110730965056131375) |
| David Gomes | Worktrees for parallel agents, with per-worktree setup for node_modules and .env. Debug Mode: logs in, reproduce, logs out before the PR. | [worktrees](https://davidgomes.com/worktrees-coding-agents/), [debug](https://davidgomes.com/cursor-debug-mode/) |
| Eric Zakariasson | Plugins: cursor-team-kit (CI, review, ship), continual-learning (AGENTS.md from transcripts), cli-for-agent. A readiness check for a repo: `npx -y agent-compatibility@latest <repo>`. | [cursor/plugins](https://github.com/cursor/plugins), [agent-compatibility](https://github.com/ericzakariasson/agent-compatibility) |
| Shub Gaur | Proto Bot: an idea becomes a draft PR with screenshots and a video. Startup QA Bot: walks your product every weekday in a test account. | [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team) |
| Michael Truell | 35% of merged PRs at Cursor are made by autonomous cloud agents. The main blockers are flaky tests and broken environments. | [third era](https://cursor.com/blog/third-era) |

## Steps in Grok Bot
1. Connect GitHub (or GitLab, Bitbucket, Azure DevOps). The bot asks with a card when it needs one (v0.49.0).
2. Add [Lingxi's Engineer Bot](https://x.ai/bot/marketplace/bots/engineer-bot), or describe your own: "one area = one bot".
3. In the bot's rules, write that every task to a cloud agent includes a "proof required" line (a screenshot, test output or log).
4. Routine every 30 min: check open PRs (CI, review comments, conflicts) and update the board. Merges only after your approval, unless you set an explicit "auto-merge if…" rule.
5. Nightly audit routine: one cleanup PR per area, at a quiet time.
6. A watch on a single PR is a GitHub routine trigger that removes itself after the merge (v0.25.0).

## Limits
- PR links work only while the cloud agent's run exists.
- A P0 routine every 5 minutes "burns tokens fast", in Lingxi's own warning (guide).
- Sources: kb/features.md §14, §4.

## Added from posts merge (2026-11-04)
- Run pstack /create-verification-skill first (poteto) — https://x.com/poteto/status/2093414407196012990
- Trust checklist: architecture, types/invariants, boundaries (poteto) — https://x.com/poteto/status/2111133080526495985
- Team engineer bot in Slack + cloud agents/Projects (poteto) — https://x.com/poteto/status/2105377066942349794
- Pick model for cloud agents in instructions (lingxi) — https://x.com/lingxi/status/2094522117362688471
