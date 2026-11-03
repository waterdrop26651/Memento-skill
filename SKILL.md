---
name: memento
description: Controlled recall and anchored direction for research agents. Use it for research memory, experiment tracking, evidence ledgers, hypothesis updates, archival recall, and picking the next high-information contrast. Use it also to keep an agent's experiments tied to the project's core question and method, with a main table as their metric. Use it whenever a long research project needs a tracker or a handoff, whenever the agent keeps drifting into side experiments or invented framings, and whenever the user has to correct the same thing twice or asks to converge, focus, or build a main table.
license: MIT
category: research-data-analysis
section: research-data-analysis
collection: community
short_description: Controlled recall and anchored direction for research memory and experiment tracking.
metadata:
  author: waterdrop26651
  license: MIT
  version: 1.1.0
  categories:
    - research-data-analysis
    - research
    - agent-memory
    - experiment-tracking
    - research-direction
  tags:
    - agent-skills
    - skill-md
    - codex
    - claude-code
    - external-memory
    - ai-memory
    - hypotheses
    - experiments
---

# Memento

## Overview

Memento treats research memory as a controlled recall problem. External
records help an agent continue work across sessions, but they can also pollute
the next decision if stale notes, weak evidence, or misleading summaries are
read as current facts.

The goal is not to remember everything. The goal is to keep the current decision
surface clear: facts in one ledger, contrasts in another, beliefs in a third,
and stale fragments behind an archive index until there is a real reason to
recall them.

Default stance: optimize for fast continuation, not exhaustive replay. A good
tracker lets a fresh agent recover the current decision surface quickly without
re-reading the whole experimental past.

Memory without a compass still drifts. The anchor layer names the project's core
question and core method, and makes every experiment justify itself against them.
A main table, the tables and figures the final report must contain, measures the
question and method. It is a means, not the goal, and it follows the final system
under study.

## Use this skill when

- The user wants an experiment tracker, ablation plan, run table, or research log.
- The project has many runs and needs a global landscape rather than ad hoc notes.
- The user wants help picking the next experiment by information gain, not intuition alone.
- The user wants to compare predictions against outcomes and update beliefs systematically.
- The user wants to prevent old context, archived findings, or memory fragments
  from becoming accidental instructions.
- The agent keeps proposing side experiments, invented metrics, or framings that
  peers do not use, or the user has corrected the same drift more than once.
- The user asks to converge, to focus on the main line, or to define a main table
  of results.
- Scarce resources (paid judges, shared GPUs, raters) must go only to the work
  that matters.

## Core rules

- Anchor before memory: the core question and method decide what counts as
  gradient. The main table measures them; it is not the goal.
- Answer the user's doubts with the existing design and evidence before
  proposing runs.
- Maintain both views at once: the global landscape and the next local gradient.
- Separate active decision support from archival completeness.
- Add a contrast before launching a run.
- Change one primary axis per contrast; keep the rest controlled enough to interpret.
- Prefer experiments whose outcome would most change the roadmap.
- Negative results are useful if the prediction was explicit and the control was clean.
- The worst result is a bad contrast that teaches nothing.
- If an old experiment no longer changes the next decision, demote it out of the
  default working set.
- Do not let every note become a tattoo: a fragment must be classified,
  checked, and placed in the right memory layer before it drives action.

## Required working set

- `runs.csv`: factual ledger, one row per run.
- `contrasts.csv`: reasoning ledger, one row per controlled comparison.
- `hypotheses.md`: belief ledger, one section per claim and update rule.

If these files do not exist, create them. Use the starter schemas in [references/TEMPLATES.md](references/TEMPLATES.md).

## Anchor layer

Add `ANCHOR.md` when the project has a main line to converge on, and always once
the user has had to correct the agent's direction. It holds:

- the core question;
- the core method;
- the claims;
- the final system;
- the main table and its cell status;
- peer grounding;
- terms the user has distinguished;
- scarce-resource rules;
- an off-table list;
- a corrections log.

Derive a short gate (at most about eight lines) from it. Inject the gate every
turn where the harness allows; otherwise reread the anchor before any proposal.

Rules:

- Justify work by the part of the question it answers and the method component
  it tests, then by its table cell. A new cell is a new experiment and needs
  the user's request. Work that maps to nothing gets one line under Off-table,
  not a pitch.
- When the user raises a doubt, ask three questions first: what the design
  already holds constant, what each metric can and cannot be caused by, and how
  the claim can be worded. Propose a run only if the user asks or reasoning
  cannot settle it.
- Follow peer work for metrics, baselines and benchmarks.
- Spend scarce resources only on cells: smoke first, once per cell per final
  system.
- Keep user-defined terms distinct, and answer capability questions literally.
- Turn every correction into a rule in the anchor and the gate. If a rule was
  kept in letter but not intent, rewrite it around the intent.
- When the final system changes, mark cells `interim` and stop spending on the
  superseded one.

Details, hooks and a worked example: [references/ANCHOR.md](references/ANCHOR.md).

## Preferred layered layout

For medium or large research programs, prefer this layout:

- `ANCHOR.md`: the direction (core question, core method, main table). Read
  first, changed rarely.
- `CURRENT_STATE.md`: the minimum entry point for a fresh agent. Keep it short.
- `ACTIVE_TRACKER.md` or `ACTIVE_TRACKER.csv`: only experiments that still have
  decision gradient for the current roadmap.
- `EVIDENCE_LOG.md`: compressed statement of what the project currently believes
  and which few experiments justify that belief.
- `runs.csv`, `contrasts.csv`, `hypotheses.md`: the full ledger.
- `archive/`: experiments and tracker snapshots that should not be read by
  default.
- optional `ARCHIVE_INDEX.md`: a searchable index for cold-memory recall.
- optional archive cards: one short note per archived cluster explaining when it
  should ever be revisited.
- optional `RECALL_NOTES/`: small audit trail for archive recalls that actually
  happened.

Think of these as memory layers:

- anchor: `ANCHOR.md` and its gate
- hot path: `CURRENT_STATE.md`, `ACTIVE_TRACKER.*`, `EVIDENCE_LOG.md`
- full ledger: `runs.csv`, `contrasts.csv`, `hypotheses.md`
- cold memory: `archive/`, `ARCHIVE_INDEX.md`, archive cards, `RECALL_NOTES/`

Compatibility rule:

- Do not break projects that only have `runs.csv`, `contrasts.csv`,
  `hypotheses.md`.
- When the tracker has become too large, introduce the layered files above and
  make them the default reading path.
- Do not require archive files for projects that do not need cold-memory recall
  yet.

## Archive recall model

Treat archive as a cold-memory layer, not as dead storage and not as part of the
default read path.

Rules:

- Do not read archive by default.
- Only recall archive when the current problem justifies it.
- Recall should begin from an index or archive card, not from blind directory
  traversal.
- Recall is for extracting reusable assets, not for replaying the entire old
  branch.
- If recall finds a still-useful result, promote that result back into the hot
  path (`CURRENT_STATE.md`, `ACTIVE_TRACKER.*`, `EVIDENCE_LOG.md`) rather than
  leaving it buried.

Recommended recall triggers:

- current mainline has stalled or failed repeatedly
- current question is structurally similar to an archived question
- a new result conflicts with the active project story
- a high-value anomaly appears and active evidence does not explain it
- the user explicitly asks for historical excavation

Recommended recall budget:

- first read `ARCHIVE_INDEX.md` or the relevant archive card
- select at most 1-2 archive clusters
- read at most 1-3 source files per cluster before deciding whether to stop
- write a short recall note if the recall materially informs the next step

## Workflow

1. Read the smallest authoritative entry point first: `ANCHOR.md` if it exists,
   then `CURRENT_STATE.md`, then `ACTIVE_TRACKER.*`, then `EVIDENCE_LOG.md`, then
   the full ledger only as needed.
2. Identify the active questions, hypotheses, and unresolved decision points, and
   map each one to the anchor. A question that maps to nothing is off-table.
3. Mark old experiments as one of:
   - `active`: still changes current decisions
   - `reference`: useful supporting evidence but not part of the default working set
   - `archived`: historical only unless a specific question reopens
4. Propose candidate contrasts. Keep only those with an anchor reference and a
   table cell, then rank them by expected information gain about the anchor.
   When the user raised a doubt, answer it from the existing design first, and
   add a contrast only if the user asks for a run.
5. Write the prediction before execution: direction, minimum meaningful delta,
   and reason.
6. Record observed facts in `runs.csv`, not interpretation.
7. Update `contrasts.csv` with actual deltas, information gain, and next
   action.
8. Update `hypotheses.md` based on the gap between expected and observed
   results.
9. If archive recall is triggered, consult `ARCHIVE_INDEX.md` or archive cards,
   do a bounded read, and summarize reusable findings in a recall note.
10. Promote any recalled high-value finding into the hot path instead of keeping
    it archive-only.
11. Refresh `CURRENT_STATE.md` and `ACTIVE_TRACKER.*` so a new agent can resume
    without replaying the whole ledger. Update the main-table cell status in
    `ANCHOR.md`. If the final system changed, mark the old cells `interim`.
12. If the user corrected the agent, record the correction in `ANCHOR.md`, turn
    it into a rule, and regenerate the gate.
13. If tracker files exist, run
    `python <path-to-this-skill>/scripts/validate_tracker.py <tracker_dir>`
    after editing them. Resolve the script path relative to this `SKILL.md`.

## Deliverables

When using this skill, produce:
- A concise landscape summary
- For each proposed contrast, its anchor reference (question part, method
  component) and its table cell
- The most informative next contrasts, ranked
- The control requirements for each contrast
- The predicted gradient or decision impact for each contrast
- Explicit hypothesis updates after new evidence
- A statement of what moved into the active set, what stayed as reference, and
  what was archived out of the default reading path
- When archive recall happened: why recall was triggered, what was read, what
  reusable asset was found, and whether it changed the plan
- When the user corrected the agent: the rule added to `ANCHOR.md` and the gate

## Quality bar

- `ANCHOR.md` fits on one page and names the final system. Every planned
  contrast in a project with an anchor fills `anchor_ref` and `table_cell`.
- No doubt from the user turned into an experiment without first being answered
  from the existing design and evidence.

- `runs.csv` should store facts and quality flags, not conclusions.
- `contrasts.csv` should make it obvious what changed, what stayed controlled, what was predicted, and what was learned.
- `hypotheses.md` should state what would change the belief, not just the belief itself.
- If a contrast is weakly controlled, mark it inconclusive instead of pretending it resolved the question.
- `CURRENT_STATE.md` should be readable in one short sitting.
- `ACTIVE_TRACKER.*` should contain only the experiments with nontrivial current
  decision gradient.
- Historical completeness belongs in the ledger and archive, not in the default
  agent entry point.
- Archive should be indexed by problem value, not only by date or snapshot name.
- Useful archived findings should be promotable back into the hot path with
  minimal rewriting.

See [references/REFERENCE.md](references/REFERENCE.md) for the full rubric and [references/TEMPLATES.md](references/TEMPLATES.md) for starter files and examples.
