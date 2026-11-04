# «Что это значит для тебя»: personal analysis + ready recipe for every new Grok Bot feature

Applies to: daily-scan, whats-new, can-it-do, and any time a new feature is noticed (chat, another bot's message, a post, the changelog).

## Whose context
The person asking (the bot's owner). Build their context cheaply, from what you already have:
1. Your memory about them (profile, shared facts).
2. Their teammate bots (names and one-line roles), your own routines, their connected connectors.
3. kb/owners/<name>.md if it exists. Create or update it when you learn something lasting.
Never assume another person's setup. If context is thin, say what you assumed.

## Rules
- Only what the feature really does according to its source (changelog, docs, @bot or team post). Unverified details get (?).
- No retelling, no generic advice. Every use names a concrete bot, routine, connector, account or product of the asker.
- 1-3 uses per feature. If none fit: «Тебе не нужно: <why>».
- Value: высокая / средняя / нет.
- **Ready recipe** for every use with value высокая or средняя: a copy-paste prompt, a skill outline, or a routine (name, schedule, prompt) that the person installs with one «да». Keep it within what the source says.
- Proposals only. Never change another bot, routine or setting without the owner's explicit yes; after a yes, apply one item at a time.
- Important features (value высокая or a new capability class) get the analysis immediately as a separate message.

## Format (in the owner's language)
```
<Фича> (vX.Y.Z / дата, источник: ссылка)
Что умеет: <1 line, strictly from the source>
Что это значит для тебя — польза: высокая/средняя/нет
1. <Бот/рутина/коннектор/аккаунт>: <concrete use>
   Рецепт (ответь «да 1»): <ready prompt / routine: name, schedule, prompt / skill outline>
2. ...
Тебе не нужно: <only if it doesn't fit, with reason>
```
