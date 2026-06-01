# Memento Skill

[简体中文](./README.zh-CN.md)

![Memory fragments banner](./assets/memory-fragments-banner.jpg)

> "I have to believe in a world outside my own mind."
>
> "We all lie to ourselves to be happy."

**Memento Skill is controlled recall for AI agents.**

It turns scattered experiment runs, notes, evidence, and hypotheses into a
layered external memory system, so an agent can continue a project without
treating every old fragment as current truth.

Don't let every note become a tattoo.

## What It Does

- Keeps current evidence on a short hot path.
- Separates facts, contrasts, and beliefs.
- Archives stale branches without deleting them.
- Recalls old memory only when there is a reason.
- Ranks the next experiment by information gain.

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

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

Manual Codex install:

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

## Skill Files

```text
SKILL.md
agents/openai.yaml
references/REFERENCE.md
references/TEMPLATES.md
scripts/validate_tracker.py
```

Banner image is an original generated asset, not a film still. Short quote
sources: *Memento* (2000), see [IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/)
and [Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29).
