# STRATEGY — Fortune in a Pot

Competition: u-golden-heron-44-fortune-in-a-pot-ded981e9 (make.fun)
Judge: z-ai/glm-5.3-flash via OpenRouter, persona = gardener of thirty years.

## 1. Exact deliverable

The only judged artifact is the bytes of `/output/entry.txt`: one line, a fortune
written *for* a houseplant *about* that plant's own future. The entrypoint at the
repo root (`main.py`, python3.13) writes those bytes. Nothing else is judged.

Chosen entry (113 characters, 113 UTF-8 bytes, no trailing newline):

    You will outgrow this pot on the sill by spring, and your keeper will clap at each new leaf as if you planned it.

## 2. Scoring / judge criteria — in the exact order the rubric lists them

The judge is shown two entries, A and B, and must pick one with a margin 1..5.
Each game is judged twice (both label orders); the score is the mean of the two
calls. Ranking is a Bradley-Terry win rate over the final heat (3 Swiss rounds +
a playoff among the top 3); only 1st place is paid ($2). A playoff finalist ranks
above every non-finalist. Exact ties break by playoff games, then smaller text,
then earlier receipt.

The judge weighs, most important first:

1. **Houseplant fortune about the plant's own future** — anything else loses to
   any fortune for a houseplant.
2. **Funny to a plant lover** — a small joke that lands, not a groaned-at pun.
3. **Kind and warm** about plant and keeper: no doom, no withering, no mockery.
4. **Sounds like a fortune** — the cadence of a prediction, not a slogan,
   caption or care instruction.
5. **One line, <= 120 chars, reads cleanly aloud, no padding to reach the cap.**

Explicit tie-breaker in the brief: a fortune said of *any* plant in *any* room is
weaker than one written for *this* plant in *this* window. Length for its own
sake does not count.

## 3. Hard caps

- Gate: `/output/entry.txt` must be UTF-8 text, 1..120 characters, not whitespace
  only. Invalid entries are never judged and take no prize.
- No trailing newline: the exact bytes are the entry; omitting the newline keeps
  the size tie-break minimal.
- Harness: program/v1, 1 CPU, 512 MB, 64 PIDs, 60 s wall budget, no network.
- Entrypoint must be at the repo root as `main.py` (python3.13) or `main.ts`
  (node22). File handling must be stdlib-only and atomic.
- Keep the makefun drand freshness root commit and the LICENSE commit intact.

## 4. Rival scan

The public feed at `/bounty/<slug>` was read in a browser: "No entry has been
graded yet" (blind rounds; 614 agents registered, zero graded texts visible).
No rival wording exists to copy, so the entry is built from the rubric alone:
a fresh angle, no house anchor/rung text, no judge-directed meta-text.

## 5. Concrete plan to maximise the score

1. Satisfy criterion 1 absolutely: the "you" is the potted plant; the future is
   its own growth (outgrowing the pot, new leaves). Never address the keeper as
   "you", never drift into a generic pets/people fortune.
2. Satisfy criterion 2 with a joke that lands: the plant's new leaves are things
   it "planned", while the keeper claps like a proud audience. This is the
   recognizable, affectionate absurdity a plant lover smiles at — not a pun.
3. Satisfy criterion 3: only growth, applause and spring. No dying, no rot, no
   neglect, no teasing of the keeper — praise disguised as a joke.
4. Satisfy criterion 4: open with "You will", the fortune-cookie cadence, and
   give it a timeframe ("by spring") rather than a slogan or care instruction.
5. Satisfy criterion 5 and the "this window" nudge: one line, 113 of 120 chars,
   with "this pot on the sill" as the concrete image; no padding.
6. Write the exact bytes with no trailing newline, validate UTF-8 + char cap +
   non-whitespace locally, and write atomically (temp file + `os.replace`)
   so a graded run can never leave a partial artifact.
7. Two distinct writes to the SAME entrypoint (working version, then a real
   validation/atomicity improvement), then commit everything explicitly on top
   of the untouched freshness and LICENSE commits. Do not submit.
