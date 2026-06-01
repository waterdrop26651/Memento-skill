# Memento Skill

Controlled recall for fragmented experiments, evolving hypotheses, and high-information next steps.

把实验碎片、证据和假设整理成可控召回的外部记忆系统。

> Don't let every note become a tattoo.

Memento Skill is an Agent Skill for research programs that generate too many
runs, notes, partial conclusions, and abandoned branches for a fresh agent to
hold safely in context. It turns scattered memory fragments into a layered
external memory system: hot path, full ledger, cold archive, and bounded recall.

It is inspired by *Memento* (2000): Leonard Shelby can keep acting only by
trusting external traces like photos, notes, and tattoos. Agents have a similar
failure mode. A stale summary, a misleading run, or a polluted retrieval result
can become a temporary reality unless the memory system forces classification,
verification, and controlled recall.

> "I have to believe in a world outside my own mind."

## Why Memento?

Most experiment trackers answer: what did we run?

Memento Skill asks a sharper question: which memory fragments should be allowed
to influence the next decision?

The danger is not just forgetting. The danger is treating every visible note as
current truth. Memento Skill keeps external memory useful by making the agent:

- keep factual observations separate from interpretations
- write predictions before results
- mark old evidence as active, reference, or archived
- recall archives only when there is a trigger
- promote useful recalled findings back into the hot path

> "We all lie to ourselves to be happy."

A good tracker makes that harder. It forces a result to say what it actually
showed, a contrast to say what was controlled, and a hypothesis to say what
would change its mind.

## What It Gives You

- **Hot path, not full replay**: a fresh agent starts from the current decision
  surface, not the entire past.
- **Prediction before result**: planned contrasts record what should happen
  before new runs exist.
- **Archive as cold memory**: old experiments are preserved without polluting
  default context.
- **Recall only with a trigger**: archive reads are bounded, documented, and
  decision-oriented.

## Quick Start

Install the skill by copying this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

Restart Codex, then invoke it with:

```text
$memento-skill Create a tracker for this experiment program and rank the next highest-information contrasts.
```

For an existing project, ask:

```text
$memento-skill Refactor this oversized experiment log into CURRENT_STATE.md, ACTIVE_TRACKER.csv, EVIDENCE_LOG.md, runs.csv, contrasts.csv, and hypotheses.md.
```

## What It Creates

```text
your-project/
├── CURRENT_STATE.md       # current actionable reality
├── ACTIVE_TRACKER.csv     # hot memory with decision gradient
├── EVIDENCE_LOG.md        # compressed evidence for current beliefs
├── runs.csv               # factual fragments, one row per run
├── contrasts.csv          # controlled comparisons and predictions
├── hypotheses.md          # beliefs, risks, and update rules
├── archive/               # cold memory
├── ARCHIVE_INDEX.md       # controlled recall entry point
└── RECALL_NOTES/          # audit trail for archive recalls
```

## How It Thinks

Memento Skill separates memory into layers:

| Layer | Files | Purpose |
| --- | --- | --- |
| Hot path | `CURRENT_STATE.md`, `ACTIVE_TRACKER.*`, `EVIDENCE_LOG.md` | What a fresh agent should read first |
| Full ledger | `runs.csv`, `contrasts.csv`, `hypotheses.md` | Complete factual and reasoning record |
| Cold memory | `archive/`, `ARCHIVE_INDEX.md`, archive cards | Old branches that should not be read by default |
| Recall audit | `RECALL_NOTES/` | Why archive was opened and what changed |

This is the opposite of dumping more context into the model. The skill tries to
protect the next decision from noisy context while keeping old evidence
recoverable.

## Validation

After editing tracker files, run:

```bash
python ~/.codex/skills/memento-skill/scripts/validate_tracker.py <tracker_dir>
```

The validator checks the required tracker files, required CSV columns, duplicate
IDs, linked run IDs, and hypothesis markers.

## Agent Skills Compliance

| Requirement | Implementation |
| --- | --- |
| `SKILL.md` frontmatter | `name` and `description` are present and written for auto-invocation |
| OpenAI/Codex UI metadata | `agents/openai.yaml` provides display name, short description, and default prompt |
| Progressive disclosure | Core workflow lives in `SKILL.md`; detailed guidance and templates live in `references/` |
| Deterministic helper | `scripts/validate_tracker.py` validates tracker structure |
| No secrets required | The skill does not require API keys, tokens, or external services |

## 中文说明

Memento Skill 是一个给 AI agent 用的外部记忆系统。它适合那些实验越来越多、旧结论越来越杂、每次新 agent 接手都容易“读错历史”的研究项目。

它的核心灵感来自电影 *Memento*：Leonard Shelby 依赖照片、便签和纹身继续行动，但这些外部线索一旦被污染，就会把他带向错误现实。AI agent 也有类似风险：上下文、实验日志、检索结果和旧总结都可能变成“临时事实”。

Memento Skill 的目标不是让 agent 记得更多，而是让 agent **不要把每一张便签都当成纹身**。

它会把研究记忆分成几层：

- `CURRENT_STATE.md`：当前可行动现实
- `ACTIVE_TRACKER.csv`：仍然会影响下一步决策的热记忆
- `EVIDENCE_LOG.md`：压缩后的关键证据
- `runs.csv`：事实碎片，只记录发生了什么
- `contrasts.csv`：对照、预测、结果和决策影响
- `hypotheses.md`：当前信念、风险和更新规则
- `archive/`：冷记忆，不默认读
- `ARCHIVE_INDEX.md`：受控召回入口
- `RECALL_NOTES/`：召回审计记录

适合使用它的情况：

- 你有很多实验、消融、控制组和旧分支。
- 新 agent 经常需要重读一堆历史才能继续。
- 你不想让旧实验或过时总结污染当前判断。
- 你希望下一步实验按信息增益排序，而不是靠直觉。
- 你希望先写预测，再看结果，再更新假设。

安装：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

重启 Codex 后使用：

```text
$memento-skill 帮我把这个实验项目整理成 runs.csv、contrasts.csv、hypotheses.md，并给出下一组最有信息量的对照。
```

短台词来源：*Memento* (2000), see [IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/) and [Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29).
