# Memento Skill

[![Agent Skill](https://img.shields.io/badge/agent-skill-black)](./SKILL.md)
[![Codex](https://img.shields.io/badge/Codex-ready-0f172a)](./agents/openai.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

**Controlled recall for fragmented experiments, evolving hypotheses, and high-information next steps.**

**把实验碎片、证据和假设整理成可控召回的外部记忆系统。**

> Don't let every note become a tattoo.

Memento Skill is an agent skill for researchers and builders whose projects
produce too many runs, notes, partial conclusions, dead branches, and "maybe
important later" findings.

It helps an AI agent answer the one question that matters after the context gets
messy:

**What should I remember right now, and what should stay in cold storage until
there is a reason to recall it?**

Inspired by *Memento* (2000), the skill treats external notes the way Leonard
Shelby treats photos, paper notes, and tattoos: powerful, necessary, and
dangerous when polluted.

> "I have to believe in a world outside my own mind."

## The Problem

After enough experiments, an agent does not just need more memory. It needs
memory hygiene.

Without it:

- old runs become accidental evidence
- stale summaries become current truth
- one-off anomalies become story anchors
- archive spelunking eats the whole context window
- the next experiment is chosen from vibes instead of information gain

Memento Skill turns the pile into a controlled memory system.

## The Core Idea

Most trackers ask:

> What did we run?

Memento Skill asks:

> Which memory fragments are allowed to steer the next decision?

It forces every fragment into a layer:

| Layer | What goes there | Why it exists |
| --- | --- | --- |
| Hot path | `CURRENT_STATE.md`, `ACTIVE_TRACKER.*`, `EVIDENCE_LOG.md` | What a fresh agent reads first |
| Full ledger | `runs.csv`, `contrasts.csv`, `hypotheses.md` | Complete facts, comparisons, and beliefs |
| Cold memory | `archive/`, `ARCHIVE_INDEX.md`, archive cards | Old branches that should not pollute default context |
| Recall audit | `RECALL_NOTES/` | Why the archive was opened and what changed |

> "We all lie to ourselves to be happy."

Good experiment memory makes that harder. A run must say what happened. A
contrast must say what changed and what stayed controlled. A hypothesis must say
what would change its mind.

## 30-Second Test Drive

Ask your agent:

```text
$memento-skill This project has too many old experiments. Build a controlled memory tracker and rank the next highest-information contrasts.
```

Expected output:

```text
CURRENT_STATE.md       # current actionable reality
ACTIVE_TRACKER.csv     # only evidence with live decision gradient
EVIDENCE_LOG.md        # compressed support for current beliefs
runs.csv               # factual ledger, one row per run
contrasts.csv          # planned/completed comparisons and predictions
hypotheses.md          # beliefs, risks, and update rules
archive/               # cold memory
ARCHIVE_INDEX.md       # searchable recall entry point
RECALL_NOTES/          # audit trail for archive recalls
```

## Before / After

Before:

```text
exp_042 looked good?
old pruning run failed, maybe because seed?
A11 was best but maybe train-only eval
notes from last month say carrier score mattered
archive has something about TopK collapse
```

After:

```text
Active decision: test whether carrier-guided features improve held-out SER.
Current best evidence: A11a, but train/eval boundary must be checked.
Next contrast: A11b matched seed, changed_axis=feature_selection_rule.
Archive recall: TopK collapse card only if A11b shows sparse-bank instability.
```

That is the difference between a note pile and a usable memory system.

## Install

With the open agent skills CLI:

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

Manual Codex install:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

Restart Codex, then invoke:

```text
$memento-skill Create a tracker for this experiment program and rank the next highest-information contrasts.
```

## Use It When

- You have many experiments, ablations, controls, seeds, and abandoned branches.
- A new agent keeps rereading old history before it can act.
- You need predictions written before results arrive.
- You want negative results to teach something instead of becoming clutter.
- You want archived findings to stay recoverable without staying always-present.
- You care about the next experiment's information gain, not just the next idea.

## What Makes It Different

- **Hot path first**: new agents read the current decision surface before the
  full history.
- **Contrasts over runs**: the reasoning unit is a controlled comparison, not a
  single result.
- **Prediction before observation**: planned contrasts record the expected
  direction and minimum meaningful delta.
- **Archive as cold memory**: old branches are indexed and recallable, not
  deleted and not always loaded.
- **Belief updates are explicit**: hypotheses include evidence, risks, next
  contrast, and update rules.

## Validate a Tracker

After editing tracker files:

```bash
python ~/.codex/skills/memento-skill/scripts/validate_tracker.py <tracker_dir>
```

The validator checks required files, required CSV columns, duplicate IDs, linked
run IDs, and hypothesis markers.

## Skill Structure

```text
Memento-skill/
├── SKILL.md                  # agent-facing workflow
├── agents/openai.yaml        # Codex/OpenAI UI metadata
├── references/REFERENCE.md   # detailed rubric and schema guidance
├── references/TEMPLATES.md   # starter files and examples
└── scripts/validate_tracker.py
```

The skill follows progressive disclosure: `SKILL.md` stays compact, while
templates and detailed guidance live in `references/` and are loaded only when
needed.

## Compatibility

| Surface | Status |
| --- | --- |
| Codex skills | Ready |
| Open agent skills CLI | Ready |
| Manual `SKILL.md` usage | Ready |
| External services | Not required |
| Secrets/API keys | Not required |

## Star This If

You think agent memory should not just be bigger. It should be cleaner,
layered, and harder to fool.

---

## 中文说明

**Memento Skill 是一个给 AI agent 用的外部记忆治理系统。**

它适合那些实验越跑越多、结论越来越碎、旧分支越来越难读的研究项目。它不是普通实验日志，而是帮助 agent 判断：

**哪些记忆现在可以影响决策，哪些应该先留在冷存储里？**

灵感来自电影 *Memento*：Leonard Shelby 依赖照片、便签和纹身继续行动。但外部线索一旦被污染，就会把他带进错误现实。AI agent 也一样：上下文、实验日志、检索结果和旧总结，都可能变成“临时事实”。

Memento Skill 的目标是：**不要让每一张便签都变成纹身。**

### 它解决什么问题

没有记忆治理时：

- 旧实验会被误读成当前证据
- 过时总结会变成新的行动前提
- 局部异常会被编成大故事
- 翻 archive 会吃掉整个上下文窗口
- 下一步实验靠直觉，而不是靠信息增益

### 它怎么工作

它把研究记忆分层：

| 层级 | 文件 | 作用 |
| --- | --- | --- |
| 热路径 | `CURRENT_STATE.md`, `ACTIVE_TRACKER.*`, `EVIDENCE_LOG.md` | 新 agent 首先读取的当前状态 |
| 完整账本 | `runs.csv`, `contrasts.csv`, `hypotheses.md` | 完整事实、对照和信念更新 |
| 冷记忆 | `archive/`, `ARCHIVE_INDEX.md`, archive cards | 不默认读，但可被召回的旧分支 |
| 召回审计 | `RECALL_NOTES/` | 记录为什么召回、读了什么、是否改变计划 |

### 快速开始

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

或者手动安装：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

重启 Codex 后使用：

```text
$memento-skill 帮我把这个实验项目整理成 runs.csv、contrasts.csv、hypotheses.md，并给出下一组最有信息量的对照。
```

### 适合你，如果

- 你有很多实验、消融、控制组、随机种子和旧分支。
- 新 agent 每次接手都要重新读很长历史。
- 你希望先写预测，再看结果，再更新假设。
- 你不想让 archive 默认污染当前上下文。
- 你希望下一步实验按信息增益排序。

短台词来源：*Memento* (2000), see [IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/) and [Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29).
