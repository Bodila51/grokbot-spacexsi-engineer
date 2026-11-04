# Recipe: design

## Engineers' approaches side by side
| Who | Approach | Source |
|---|---|---|
| Peng Zheng | A design bot with Figma MCP plus a skill describing how his files are organized, his colors, type and spacing. He makes the system and one keyframe himself ("the first 5%"), and the bot extends it to the whole flow. Also a self-updating personal site. | [creatoreconomy](https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan), [How I AI](https://www.lennysnewsletter.com/p/how-i-ai-how-two-spacexai-designers) |
| John Bai | Figma Bro: a voice memo plus screenshots, and it places elements across the artboards. Motion God and Devbot for prototypes. Tips: start from production assets, not screenshots; tune springs and easing in a localhost playground; give short comparative feedback; make one auto-layout component and let the agent fill the rest. | [guide](https://x.ai/bot/guides/designing-grok-bot-with-grok-bot), [figma bro](https://x.ai/bot/marketplace/bots/figma-bro) |
| Manuel Muñoz Solera | Critiquito: a ranked design critique from a screenshot or a Figma link. It never edits your files. | [critiquito](https://x.ai/bot/marketplace/bots/critiquito) |
| Benji Taylor | agentation: click on the UI and leave notes, which go to the agent as markdown with selectors. stageshow: faux product UI. | [agentation](https://github.com/benjitaylor/agentation), [skills](https://github.com/benjitaylor/skills) |
| Lauren Tan | pstack's `/make-bot-ui`: a page whose buttons wake a Grok Bot over a webhook. | [pstack](https://github.com/cursor/plugins/tree/main/pstack) |

## Steps in Grok Bot
1. Connect Figma (the app card shows in chat, v0.70.2).
2. Create a "design system" skill: file structure, tokens, type, spacing.
3. Make one reference screen by hand, then ask the bot to extend it to the flow.
4. Critique through Critiquito, or in your own words, with short comparisons ("A is better than B because…").

## Limits
- Generated images are not for charts or tables.
- The Figma MCP needs a Figma connection.

## Added from posts merge (2026-11-04)
- Team brand bot for on-brand decks (benjitaylor) — https://x.com/benjitaylor/status/2112986857474585048
- Physical product prototyping: diagrams, RFQs, manufacturer emails (benjitaylor) — https://x.com/benjitaylor/status/2112607770986029172
