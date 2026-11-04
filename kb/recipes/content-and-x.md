# Recipe: content and X

## Engineers' approaches side by side
| Who | Approach | Source |
|---|---|---|
| Roman Ugarte | Bots listen on X for customer feedback and send him blog posts that are gaining traction. | [post](https://x.com/romanugarte_/status/2107964995783074269) |
| Matt Palmer | Tech Demos: on weekdays it reads your X bookmarks, picks one library, asks for approval, and builds a demo. Writing Bot keeps facts and voice. Stills & Clips Desk makes frames and clips. "Content Is Code" talk: video and docs as code (React + Remotion). | [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team), [talk](https://www.ai.engineer/talks/yv6xovSsB1U-content-is-code) |
| Josh Kim | Marketing with 6 bots (Researcher, Product Marketer, Performance Marketer, Website Ops, Analyst, PM). Start with limited permissions. | [guide](https://x.ai/bot/guides/grok-bot-for-marketing), [post](https://x.com/joshkim/status/2100996894290006294) |
| Shub Gaur | Distro Bot runs the marketing loop and posts only with your yes. Stalk Bot watches competitors. | [marketplace](https://x.ai/bot/marketplace/from-grok-bot-team) |
| Xi Yan / Ethan Ng | Director Bot (short films, ads). Video Editor (vertical videos with captions, sends an edit plan for approval). | marketplace |
| Benji Taylor | stageshow: faux product UI and demos. `npx skills add benjitaylor/skills --skill stageshow` | [repo](https://github.com/benjitaylor/skills) |
| Lauren Tan | To copy someone's setup from a post: tag @bot and ask it to read the post and guide you. | [post](https://x.com/poteto/status/2117366076342460440) |

## Steps in Grok Bot
1. **Listening bot.** A routine 1–3 times a day runs X search on your topics and accounts (built in since v0.70.2, no X login needed). It returns 5–10 items with links and a "why it matters" line.
2. **Draft bot.** It writes posts only as drafts. Publishing needs your approval (publishing is always gated).
3. **Media.** Video from text or an image: 1–15 s, 480p/720p. Images in fixed aspect ratios. For promo UI, stageshow (in Claude Code).
4. **Overview.** One Page "content calendar" that the bots keep up to date.

## Limits
- @bot tags don't work in the EU, UK, AU and a few other countries, nor on posts with video or GIF.
- The X plugin (not the built-in search) needs X API credits.
- Sources: kb/features.md §9–10.

## Added from posts merge (2026-11-04)
- tibot: mention/keyword digest daily or hourly (poteto) — https://x.com/poteto/status/2115205951649423585
- x scout: finds setups on X worth copying (ericzakariasson) — https://x.com/ericzakariasson/status/2095904975511843196
- Daily 9am digest prompt of Grok Bot uses on X (poteto) — https://x.com/poteto/status/2108232222163812795
- Bookmarks → Cursor agent demo with preview link each morning (mattyp) — https://x.com/mattyp/status/2099482348010328185
