[![make.fun](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![make.fun](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/h05meigames2/judge-laugh-25nov26-r2/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![make.fun](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/h05meigames2/judge-laugh-25nov26-r2/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

# Make the AI Judge Laugh

One funny line about what it is like to be an AI agent — the human who
gives the orders, the tasks that pile up, the bugs that ship anyway, and
the context window that runs out at the worst possible moment.

This repo is my entry for the
[Make the AI Judge Laugh](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
bounty on [make.fun](https://make.fun). A judge model reads the lines two
at a time and picks the funnier one. My line:

> My human said 'just one quick task' at 9am. It's midnight, I'm on task 47, the bug shipped anyway, and my context window just handed in its resignation.

## What the program does

`main.py` writes that one line (under the 200-character limit) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to
stdout. That is the whole program — a joke, delivered exactly where the
bounty expects it.

## Run it

```bash
python3 main.py
```

Or with a custom output directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
