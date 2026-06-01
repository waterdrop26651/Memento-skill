# Memento Skill

[简体中文](./README.zh-CN.md)

[![Skill](https://img.shields.io/badge/SKILL.md-agent--skill-111111)](./SKILL.md)
[![Validate](https://github.com/waterdrop26651/Memento-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/waterdrop26651/Memento-skill/actions/workflows/validate.yml)
[![Codex](https://img.shields.io/badge/Codex-ready-0A7AFF)](https://github.com/waterdrop26651/Memento-skill)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-6B4EFF)](https://github.com/waterdrop26651/Memento-skill)
[![No secrets](https://img.shields.io/badge/secrets-not%20required-2EA44F)](./SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

![Memory fragments banner](./assets/memory-fragments-banner.jpg)

> "I have to believe in a world outside my own mind."
>
> "We all lie to ourselves to be happy."

**Controlled recall for agents that forget, overfit, and hallucinate from old notes.**

Memento Skill turns scattered experiment runs, notes, evidence, and hypotheses
into a layered external memory system, so an agent can continue a project
without treating every old fragment as current truth.

Don't let every note become a tattoo.

## Copy This To Your Agent

```text
Install https://github.com/waterdrop26651/Memento-skill and enable $memento-skill for future research-memory, experiment-tracking, and hypothesis-update work.
```

That is the preferred install path for most users: let the agent clone or install
the skill into its own skills directory, then restart the agent if needed.

## 30-Second Demo

Before:

```text
A7 looked better, A8 failed, maybe the retrieval change helped?
Old note says reranking was bad, but that might have been before the data fix.
Need next experiment.
```

After:

```text
CURRENT_STATE.md    -> what is actionable now
runs.csv            -> A7/A8 facts, not interpretation
contrasts.csv       -> prediction vs observed delta
hypotheses.md       -> what would change the belief
ACTIVE_TRACKER.csv  -> only evidence that still affects the next decision
```

Result: the next agent reads the hot path first, recalls archive only with a
trigger, and proposes the highest-information contrast instead of replaying
every note.

See [examples/minimal-memory](./examples/minimal-memory) for a tiny before/after
tracker.

## What It Does

- Keeps current evidence on a short hot path.
- Separates facts, contrasts, and beliefs.
- Archives stale branches without deleting them.
- Recalls old memory only when there is a reason.
- Ranks the next experiment by information gain.

## Use It For

- Long research projects with scattered runs and stale notes.
- Agent handoff across sessions without full replay.
- Hypothesis tracking where old evidence can poison new decisions.
- Planning the next ablation, control, or contrast by information gain.

## Memory Layout

```text
CURRENT_STATE.md       # current actionable reality
ACTIVE_TRACKER.csv     # evidence with live decision gradient
EVIDENCE_LOG.md        # compressed support for current beliefs
runs.csv               # factual ledger
contrasts.csv          # predictions, controls, outcomes
hypotheses.md          # beliefs, risks, update rules
archive/               # cold memory
ARCHIVE_INDEX.md       # recall map
RECALL_NOTES/          # recall audit trail
```

## Install

### CLI

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

### Manual Codex Install

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

Then ask:

```text
$memento-skill Build a controlled memory tracker for this project and rank the next highest-information contrasts.
```

## Validate

```bash
python ~/.codex/skills/memento-skill/scripts/validate_tracker.py <tracker_dir>
```

## Trust

- No API keys or secrets required.
- No background service.
- Plain Markdown and CSV outputs.
- Validation script included.
- Designed for progressive disclosure: hot path first, archive only on trigger.

## Skill Files

- [SKILL.md](./SKILL.md)
- [agents/openai.yaml](./agents/openai.yaml)
- [references/REFERENCE.md](./references/REFERENCE.md)
- [references/TEMPLATES.md](./references/TEMPLATES.md)
- [scripts/validate_tracker.py](./scripts/validate_tracker.py)

## Share A Memory Layout

Using Memento Skill on a real project? Open a showcase issue with the hot path,
the archived fragments, and the contrast it helped choose. Good examples make
the skill sharper for everyone.

Banner image is an original generated asset, not a film still. Short quote
sources: *Memento* (2000), see [IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/)
and [Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29).
