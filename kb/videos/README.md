# Video transcripts

This folder is empty in version 1.0.0. Add one markdown file per public video when a transcript is worth keeping.

Suggested name: `<YYYY-MM-DD>-<handle-or-source>.md`

Include:

- title, date, speaker, and the public URL
- a transcript or timestamped notes
- a one-line note on what is useful for Grok Bot

Publish only videos you have the right to share. Do not add private recordings, unlisted links that were not meant to be public, or anyone's contact details.

After adding a file, run `python3 scripts/build-version.py` so `version.json` lists it. daily-scan does not fetch a file until that manifest lists it.
