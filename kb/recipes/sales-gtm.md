# Recipe: sales and GTM

## Engineers' approaches side by side
| Who | Approach | Source |
|---|---|---|
| Krista Letz | Chief of Staff plus specialists (prospecting, an expert per account, a product expert, forecasting, slides, a sales coach). Record a task once and turn it into a skill. Bots: Outbound Prospecting, Signal Prospector, Pipeline Pulse, Meeting Recap Deck, EBR & Value Deck Builder. | [guide](https://x.ai/bot/guides/grok-bot-for-gtm), [article](https://x.com/kristaletz/status/2089103618121314689), marketplace |
| Roman Ugarte | A domain expert "dumps" their workflow into a bot, shares it with the team, and the bot keeps learning. | [post](https://x.com/romanugarte_/status/2115133963857690713) |
| @bot (sales ops) | Shared Bots: Account Intel (CRM after calls), Quote Bot (proposals), Deal Bot (non-standard terms). | [post](https://x.com/bot/status/2115130760009273501) |
| Eric Zakariasson | 100 use cases, among them: outbound in your Gmail voice, a multi-bot GTM crew with weekly playbooks, screening event applicants against your ICP. | [thread](https://x.com/ericzakariasson/status/2087258914060664902) |
| Stefan Markarian (guide) | Outbound in 5 stages, about 20 accounts every morning, never auto-send. | [guide](https://x.ai/bot/guides/grok-bot-for-sdrs) |
| Simon Lackowski (guide) | Founder Mode: 1 chief of staff, 8 bots, 16 paused routines. Follow-ups every 5–6 days, stop after about 8 touches. | [guide](https://x.ai/bot/guides/grok-bot-for-founder-led-sales) |
| Docs template | "Research the 25 accounts in this CRM view… Return a review list; do not send or enroll anyone." Schedule it as a routine only once the output is reliable. | [use cases](https://docs.x.ai/grok-bot/use-cases) |

## Steps in Grok Bot
1. Connect CRM, email and calendar.
2. Run the docs' "sales outbound" template once by hand and check the list.
3. Save it as a skill ("Save the process we just used as a skill called 'Outbound research'"), with the rule "nothing is sent without approval".
4. Only then, a daily routine in the morning. Sends always stay drafts.
5. Weekly: Pipeline Pulse or an equivalent for stale deals.

## Limits
Email from routines stays a draft until you press Send. "Disable drafts" removes that protection, so don't turn it on for sales.
