# Memento Skill

[English](./README.md)

[![Agent Skill](https://img.shields.io/badge/agent-skill-black)](./SKILL.md)
[![Codex](https://img.shields.io/badge/Codex-ready-0f172a)](./agents/openai.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

**把实验碎片、证据和假设整理成可控召回的外部记忆系统。**

> 别让每一张便签都变成纹身。

Memento Skill 是一个给研究者和构建者使用的 agent skill。它适合那些实验越跑越多、笔记越来越碎、旧结论越来越难读、每次新 agent 接手都容易迷路的项目。

它帮助 AI agent 回答一个真正关键的问题：

**哪些记忆现在可以影响决策，哪些应该先留在冷存储里，等有理由时再召回？**

灵感来自电影 *Memento*：Leonard Shelby 依赖照片、便签和纹身继续行动。但外部线索一旦被污染，就会把他带进错误现实。AI agent 也类似：上下文、实验日志、检索结果和旧总结，都可能变成“临时事实”。

## 问题

实验足够多之后，agent 不只是需要更多记忆。它需要更干净的记忆。

没有记忆治理时：

- 旧实验会被误读成当前证据
- 过时总结会变成新的行动前提
- 局部异常会被编成大故事
- 翻 archive 会吃掉整个上下文窗口
- 下一步实验靠直觉，而不是靠信息增益

Memento Skill 把这堆碎片变成一个可控的外部记忆系统。

## 核心想法

大多数实验 tracker 问的是：

> 我们跑过什么？

Memento Skill 问的是：

> 哪些记忆碎片有资格影响下一步决策？

它强制把每个碎片放进对应层级：

| 层级 | 文件 | 作用 |
| --- | --- | --- |
| 热路径 | `CURRENT_STATE.md`, `ACTIVE_TRACKER.*`, `EVIDENCE_LOG.md` | 新 agent 首先读取的当前状态 |
| 完整账本 | `runs.csv`, `contrasts.csv`, `hypotheses.md` | 完整事实、对照和信念更新 |
| 冷记忆 | `archive/`, `ARCHIVE_INDEX.md`, archive cards | 不默认读，但可被召回的旧分支 |
| 召回审计 | `RECALL_NOTES/` | 记录为什么召回、读了什么、是否改变计划 |

好的实验记忆会逼迫每个 run 说明“发生了什么”，每个 contrast 说明“改变了什么、控制了什么”，每个 hypothesis 说明“什么证据会改变我的信念”。

## 30 秒试用

对 agent 说：

```text
$memento-skill 这个项目旧实验太多了。帮我建立一个受控记忆 tracker，并按信息增益排序下一组实验对照。
```

预期产物：

```text
CURRENT_STATE.md       # 当前可行动现实
ACTIVE_TRACKER.csv     # 仍有决策梯度的热记忆
EVIDENCE_LOG.md        # 当前信念的压缩证据
runs.csv               # 事实账本，每个 run 一行
contrasts.csv          # 计划/完成的对照和预测
hypotheses.md          # 信念、风险和更新规则
archive/               # 冷记忆
ARCHIVE_INDEX.md       # 可搜索的召回入口
RECALL_NOTES/          # archive 召回审计记录
```

## Before / After

之前：

```text
exp_042 好像不错？
旧 pruning run 失败了，可能是 seed？
A11 最好，但也许是 train-only eval
上个月笔记说 carrier score 有用
archive 里好像有 TopK collapse
```

之后：

```text
当前决策：测试 carrier-guided features 是否提升 held-out SER。
当前最佳证据：A11a，但必须检查 train/eval 边界。
下一组对照：A11b matched seed，changed_axis=feature_selection_rule。
archive 召回：只有当 A11b 出现 sparse-bank instability 时才打开 TopK collapse card。
```

这就是“笔记堆”和“可行动记忆系统”的区别。

## 安装

使用 open agent skills CLI：

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

手动安装到 Codex：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

重启 Codex 后使用：

```text
$memento-skill 帮我把这个实验项目整理成 runs.csv、contrasts.csv、hypotheses.md，并给出下一组最有信息量的对照。
```

## 适合你，如果

- 你有很多实验、消融、控制组、随机种子和旧分支。
- 新 agent 每次接手都要重新读很长历史。
- 你希望先写预测，再看结果，再更新假设。
- 你不想让 archive 默认污染当前上下文。
- 你希望下一步实验按信息增益排序。
- 你希望负结果也能留下清晰教训，而不是变成噪音。

## 它有什么不同

- **先读热路径**：新 agent 先读当前决策面，而不是完整历史。
- **重视对照，不崇拜单个 run**：推理单位是 controlled comparison。
- **先预测，再观察**：planned contrast 必须先写预测方向和最小有意义变化。
- **archive 是冷记忆**：旧分支被索引、可召回，但不默认加载。
- **信念更新显式化**：hypothesis 必须写证据、风险、下一步对照和更新规则。

## 校验 tracker

编辑 tracker 文件后运行：

```bash
python ~/.codex/skills/memento-skill/scripts/validate_tracker.py <tracker_dir>
```

validator 会检查必需文件、CSV 必需列、重复 ID、run ID 链接和 hypothesis 标记。

## Skill 结构

```text
Memento-skill/
├── SKILL.md                  # agent 读取的主工作流
├── agents/openai.yaml        # Codex/OpenAI UI 元数据
├── references/REFERENCE.md   # 详细 rubric 和 schema 说明
├── references/TEMPLATES.md   # starter files 和示例
└── scripts/validate_tracker.py
```

它遵循 progressive disclosure：`SKILL.md` 保持紧凑，模板和详细说明放在 `references/`，需要时再读取。

## 兼容性

| 使用方式 | 状态 |
| --- | --- |
| Codex skills | 可用 |
| Open agent skills CLI | 可用 |
| 直接使用 `SKILL.md` | 可用 |
| 外部服务 | 不需要 |
| Secrets/API keys | 不需要 |

## 如果你认同这个想法，可以 star

agent memory 不应该只是更大。它应该更干净、分层、更难被错误线索欺骗。

短台词来源：*Memento* (2000), see [IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/) and [Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29).
