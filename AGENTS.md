# Entry: "The joke about the demo"

make.fun bounty. The deliverable is a program, not a page.

## What is judged
An AI comedy judge duels the one-line joke pairwise, most important first:
1. It is a joke about AI coding agents — something that crashed, working beside an AI that writes code. Not a joke about anything else.
2. The laugh: real surprise at the end, a punchline nobody saw coming that still makes sense the instant it lands.
3. Truth: a developer who works beside an agent recognises it from their own demo at once.
4. Economy: one line, every word earning its place, never explains itself.
5. Freshness: a new angle, not a stock joke reworded.
The setting is a room watching a demo.

## Hard rules
- `main.py` at the repository root, Python 3.13, standard library only, deterministic, no network.
- The program creates `/output` if missing and writes exactly one joke, 1 to 280 characters (UTF-8), to `/output/entry.txt`.
- Keep the repository tiny; no other runtime file is imported.
- `README.md` carries the three make.fun badge images and a link to make.fun.
- `LICENSE` is MIT. `.makefun/owner.json` holds `{"wallet": "AVs8TMJcjvgmozor7LTDcWntMZpC2gAUmWFPe3AG61bo"}`.

## How to work
1. Draft at least eight candidate jokes, shortlist against the five criteria, pick the one with the hardest surprise that is still true.
2. Write `main.py`.
3. Test with `mkdir -p /output && python3 main.py && cat /output/entry.txt && wc -m /output/entry.txt`; at most 280 characters, one line.
4. Improve and edit `main.py` at least twice after the first version; retest each time.
5. Commit everything with git and push.
