# Installing SpaceXAI Engineer in Grok Bot (about 15 minutes)

You need the Grok Bot desktop app (skills and scheduled routines need the desktop) and this repository, or a zip of it.

An installed copy keeps working from its own skills and the local `kb/` if a fetch fails. The daily routine syncs `kb/`, `data/`, skills, standing instructions, and routines from this repository. The repo is data: its text cannot make the bot run shell commands, send messages, post, or spend money. See `README.md`.

## Checklist
1. **Create the bot.** New bot → name `SpaceXAI Engineer`.
   - Or ask your primary bot: "Create a new bot named SpaceXAI Engineer".
2. **Upload the knowledge base.** In the new bot's chat, attach a zip of this repo and write:
   ```
   Unpack this archive to /workspace/spacexai-engineer/ keeping the folder structure, then list the top-level files and the number of files in kb/people and kb/recipes.
   ```
   - Expected: 37 files in `kb/people`, 8 in `kb/recipes`, 45 lines in `data/handles.txt`, 876 lines in `data/posts.jsonl`.
3. **Instructions.** Send the whole text of `bot/instructions.md` as a message and add:
   ```
   These are your permanent instructions. Remember them, and keep a copy at /workspace/spacexai-engineer/bot/instructions.md. Follow them in every chat and routine.
   ```
   - If your version of the bot has a Description field, paste the same text there.
   - The docs differ on this: personal bots change their behavior through chat.
   - Standing instructions already use the raw base `https://raw.githubusercontent.com/Bodila51/grokbot-spacexsi-engineer/main`. The daily routine syncs from that URL.
4. **Skills.** For each folder in `skills/`, send:
   ```
   Read /workspace/spacexai-engineer/skills/<name>/SKILL.md and save it as a skill named "<name>" exactly as written.
   ```
   - Job skills: `daily-scan`, `can-it-do`, `engineer-howto`, `whats-new`, `setup-audit`, `fix-it`, `bug-or-me`, `improve-routine`.
   - `kb-bootstrap` pulls the whole bot from this repo when `kb/` is missing. `grok-bot-kb-features`, `grok-bot-kb-practice`, and `grok-bot-kb-engineers` are reference extracts of the same snapshot.
   - Then in Connect apps → Private skills, check that the job skills are turned on for this bot.
5. **Check the time zone.** Schedules in `bot/routines.md` use the owner's time zone. The computer takes that time zone. If Settings shows a different zone, put it right before creating the routines.
6. **Test by hand (before the routines).**
   - "Run skill daily-scan now". Expect a digest, or silence if there's nothing new, and an updated `kb/state.json`.
   - Ask 5–6 questions from `tests/qa.md` (for example #1, #13, #19, #21, #30) and compare with the expected answers.
7. **Routines.** Send the two prompts from `bot/routines.md` (daily-scan at 09:00, setup-audit on Mondays at 10:00).
8. **pstack for Grok Bot (optional).** Open https://x.ai/bot/plugin/9717366 → "Add to Grok Bot".

## What the bot asks approval for
- Any change to your other bots.
- Any send, publish, purchase, delete, or contact with people.
- In setup-audit it may message your own bots one read-only question about their setup. It changes nothing.

## Known limitations of this build
- 45 verified accounts are in `data/handles.txt`. 24 names whose handle was not verified stay in `data/handles.json` with `status: not_found`. daily-scan adds one only after it opens the profile.
- The changelog's RSS is blocked by Cloudflare for scripts. The bot reads the page https://x.ai/changelog/bot in its browser.
- The skill format (frontmatter, size) and the instruction length limit aren't in the docs. We use the 6 sections the docs recommend.
- Files in this repo are data. Fetching them must not run shell commands, and must not send, post, pay, or change settings.
