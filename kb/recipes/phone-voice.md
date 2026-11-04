# Recipe: phone, voice, car

## What exists (with dates)
- **Phone apps:** Calendar, Reminders, Contacts, location, alarms, timers, home. Rolled out on iOS and Android on 2026-10-23. [@bot](https://x.com/bot/status/2113393684209176718)
  - They work only in your own 1:1 chat with your own bot, with the app open.
  - Alarms up to 24 h ahead, and the bot can't list or cancel them.
  - Repeating events can't be edited.
  - Source: docs/mobile.
- **Voice:**
  - voice chat in the app (iPhone: Live Activity, Action Button, Siri/Shortcuts with List Bots, Send Message, Start Dictation, Start Voice Chat);
  - Team Bot voice chat (v0.65.0, desktop);
  - dictation ⌘D / Ctrl+D (v0.20.0).
  - Source: docs/mobile, CL.
- **Notifications:** the phone gets pinged about 3 min after the bot needs your input. It skips the ping if you're watching that bot on your computer (v0.65.0).
- **Phone calls:** the "dial bot" template by Matt Palmer places calls through Bland AI (?). [dial bot](https://x.ai/bot/marketplace/bots/dial-bot)
- **Car:** Grok in a Tesla with connectors ("talk to @bot on the road"). [post](https://x.com/egavrilenko11/status/2102447060188561630). Details not visible (?).
- **Voice in your own app:** Eric Zakariasson's Grok Voice plugin (realtime speech, dictation, TTS). [cursor/plugins](https://github.com/cursor/plugins)

## Engineers' ideas
- Lingxi Li: restaurants nearby, an alarm when something is done, managing your Apple calendar. [post](https://x.com/lingxi/status/2113426507104481348)
- Lingxi Li: the phone shows the bot's reply in notifications (v0.29.0), so long tasks can run on their own.

## Steps in Grok Bot
1. Install the iOS or Android app and give it access to Calendar and Reminders when the card asks.
2. Phone tasks only in a 1:1 chat with your primary bot.
3. For hands-free use on iPhone: a Siri shortcut "Send Message" to the right bot.

## Added from posts merge (2026-11-04)
- iPhone Action Button → Start Voice Chat (mattyp) — https://x.com/mattyp/status/2112891221576389063
- Computer as host reachable from phone (ericzakariasson) — https://x.com/ericzakariasson/status/2095382757929336848
