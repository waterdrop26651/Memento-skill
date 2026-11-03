# Anchor Layer Reference

## Why an anchor

The memory layers keep an agent from acting on stale facts. They do not keep it
from working on the wrong question. Long research sessions drift. Each step looks
locally reasonable: one more ablation, a new metric, a side narrative, a
"quick check". Yet the project stops converging, and the user has to correct the
agent again and again.

The anchor layer fixes direction. It names the **core question** and the **core
method**, and makes every piece of work justify itself against them.

The **main table** is the set of tables and figures the final report must
contain. It is the anchor's metric surface: it makes the question and method
measurable, and an all-filled table shows when the work has converged.

The table is a means, not the goal. It is not frozen; it follows the final system
under study. An agent that treats the table as the goal will:

- freeze it,
- argue about cells,
- game it by opening new cells for side work.

An agent anchored on the question uses the table to measure progress.

## `ANCHOR.md`

One page, changed rarely, and only when the user changes direction. Sections:

- **Core question**: one or two sentences. What must the project answer?
- **Core method**: the mechanism that answers it, its components, and its
  prerequisites.
- **Claims**: what the final report will assert, each with where its evidence
  lives (hypothesis IDs, table cells).
- **Final system**: the model, checkpoint, data or product the evidence must be
  measured on. When this changes, every cell becomes interim.
- **Main table**: the tables and figures, with their rows, columns and metrics.
  Give each cell a status: `pending`, `interim`, `final`.
- **Peer grounding**: the papers or systems whose metrics and baselines the table
  follows.
- **Terms**: distinctions the user has drawn that must never be blurred.
- **Scarce resources**: paid judges, shared GPUs, raters. Say which cells may use
  them, and how often.
- **Off-table**: one line per idea that fills no cell. Recorded, not pitched.
- **Corrections**: each user correction, and the rule it produced.

The template is in [TEMPLATES.md](TEMPLATES.md#anchormd).

## The gate

The gate is a short checklist, at most about eight lines, derived from
`ANCHOR.md`. The agent applies it before any reply that proposes, launches or
interprets work.

- Where the harness supports it, inject the gate on every turn (see
  [Hooks](#hooks)). Instructions read once at session start fade over a long
  session; a per-turn reminder does not.
- Otherwise, read `ANCHOR.md` at the start of each working session and again
  before any proposal.
- The gate is derived from the anchor. When `ANCHOR.md` changes, regenerate the
  gate in the same edit.

## Rules, and why

1. **Anchor before action.** Read `ANCHOR.md` before `CURRENT_STATE.md`. The
   state says where the project is. The anchor says where it is going.

2. **Justify work by the question and method first, and by the cell second.**
   Before running anything, say which part of the core question it answers,
   which component of the method it tests, and which cell it fills. A cell is
   only a pointer to the anchor. Opening a new cell to host an idea is the same
   as adding an experiment; new cells need the user's request. Work that maps to
   nothing goes on the off-table list in one line, and is not pitched.

3. **Answer doubts with reasoning before runs.** When the user raises a concern
   (attribution between two components, a reviewer objection, a missing
   comparison), first ask three questions:
   - What does the existing design already hold constant?
   - What can each metric be caused by, and what can it not be caused by?
   - How can the claim be worded? For example, parity instead of superiority, or
     "A works without B" instead of "A and B are fully independent".

   Many doubts dissolve under these questions. Propose a run only if the user
   asks for one, or if reasoning cannot settle the doubt and the run maps to the
   anchor. In that case, say so in one line and wait.

4. **Ground methods and metrics in peer work.** Use the metrics, baselines and
   benchmarks that comparable published systems report. Do not invent metrics,
   deployment stories or framings the field does not use. If peers use a
   benchmark, the table should use it too, or say why not.

5. **Spend scarce resources only on cells.**
   - Smoke-test first on a few samples.
   - Run each cell once per final system.
   - Keep secrets out of files and logs, and check the logs afterwards.
   - When a paid service fails, find the cause (quota, model name, request size)
     before retrying. Do not retry blindly.

6. **Treat user-defined terms as contracts.** When the user distinguishes two
   things, write the distinction under Terms, then apply it everywhere:
   - Never use evidence, benchmarks or wording for one as support for the other.
     For example, the model calling tools itself is not the same as the model
     delegating a request to a backend agent.
   - Answer capability questions literally. "Can it do X?" asks about X, not
     about a neighbour of X.

7. **Close the loop on every correction.** A correction shows that the anchor or
   the gate is incomplete. Then:
   - fix the record;
   - add or rewrite the rule in `ANCHOR.md` and in the gate;
   - log it under Corrections;
   - save it to long-term memory if the harness has one.

   If the agent kept a rule's letter but defeated its intent (for example, by
   relabelling an extra experiment as "a new cell"), rewrite the rule around its
   intent. The same correction arriving twice means the loop failed.

8. **Follow the final system.** When the system under study changes (a new
   capability, checkpoint or data mix):
   - mark the existing cells `interim`;
   - stop spending on the superseded system;
   - plan to refill the table on the final one.

   Interim results still validate the pipeline and the measurement code. They
   are not the report's evidence.

9. **Verify before you summarize.** A summary sentence ("all intervals include
   zero", "no open model reports X") is a claim. Check it against the numbers or
   sources before writing it down. If it was wrong, correct it openly in the
   same place.

10. **Report the conclusion first, in plain language, and briefly.** The user
    steers the project. Make the decision-relevant fact the first line.

## How the anchor connects to the memory layers

- **Read order**: `ANCHOR.md` → `CURRENT_STATE.md` → `ACTIVE_TRACKER.*` →
  `EVIDENCE_LOG.md` → full ledger as needed.
- **`contrasts.csv`**: add the optional columns `anchor_ref` (which part of the
  question or method the contrast tests) and `table_cell`.
  - Filter candidate contrasts by the anchor before ranking them by information
    gain. Information gain is measured about the anchor, not about anything at
    all.
  - The validator enforces both columns for planned contrasts once they exist.
- **`hypotheses.md`**: each claim in `ANCHOR.md` maps to one or more hypotheses.
  Their update rules say what evidence would change the claim.
- **`ACTIVE_TRACKER.*`**: a run measured on a superseded system drops to
  `reference`. Its note names the final system.
- **Archive**: off-table ideas and superseded-system results can be archived
  with a recall trigger such as "the user reopens this direction".
- **`CURRENT_STATE.md`** stays the operational entry point and changes often.
  `ANCHOR.md` changes only when the direction changes.

## Hooks

**Claude Code.** Use a project-local `UserPromptSubmit` hook. Put it in
`.claude/settings.local.json`, which is not committed. It turns the gate file
into context on every turn:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "jq -Rs '{hookSpecificOutput: {hookEventName: \"UserPromptSubmit\", additionalContext: .}}' \"$CLAUDE_PROJECT_DIR/.claude/anchor_gate.txt\" 2>/dev/null || true",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

If `.claude/` did not exist when the session started, open `/hooks` once or
restart the session so the watcher picks the file up.

**Codex and other agents.** Put the gate text in the always-loaded instructions
file, such as `AGENTS.md`. If no such file exists, read `ANCHOR.md` before every
proposal.

## Failure modes

- **Table as goal**: freezing the table, or arguing about cells instead of the
  question.
- **Gaming the gate**: hosting side work in "new cells", or relabelling an
  experiment as an "analysis".
- **Doubt → experiment reflex**: proposing an ablation when the existing design
  already controls the variable.
- **Invented framing**: metrics, benchmarks or deployment stories that peers do
  not use.
- **Term blur**: using a benchmark or claim about one thing as support for a
  different thing the user distinguished.
- **Superseded spend**: continuing to fill cells on a system the user has already
  replaced.
- **Unverified summaries**: blanket statements written before checking each
  number or source.
- **Repeat corrections**: the same correction twice means the rule is missing,
  not injected, or written around its letter.

## Worked example (abstracted from a real project)

A full-duplex speech model learns how long to wait before its next decision.

- **Core question**: can the model judge for itself when it will next be needed,
  and so compute less without hurting interaction quality?
- **Core method**: window choices read at the end of every decision, trained on
  the longest safe wait, and decoded with an expected-lateness budget and early
  wake. A two-decision speak rule is a prerequisite.
- **Main table**:
  - Table A: schedules on one model, measured in forward passes per hour and in
    interaction quality.
  - Table B: a public duplex benchmark, comparing the fixed schedule against the
    learned one.
  - A figure: predicted wait against true wait.

Moments where the anchor decided the answer:

- **"Do the speak rule and the learned windows confound each other?"** Answered
  without runs:
  - the rule is held constant across all of Table A;
  - a speak rule cannot reduce forward passes, since speaking costs more;
  - quality is claimed as parity, not superiority;
  - the rule stands without the windows (one-directional), and full
    orthogonality is not claimed.

  The agent had first proposed a 2×2 ablation. The user called it "adding an
  experiment in disguise". The rule became rule 3.
- **"Does the model have tool calling?"** It only delegated requests to a backend
  agent. The agent had blurred the two, and even cited a tool-calling benchmark
  to justify the delegation column. Both became a Term and rule 6.
- **New capability added.** The user added tool calling to the model. Every cell
  measured on the old model became interim, and the pending timing runs on it
  were dropped (rule 8).
- **"Main table first" was misread as "the table is the goal".** The user
  corrected this. The anchor moved from the table to the question and method,
  which is this layer's founding rule.
