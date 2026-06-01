# Memento Skill

[English](./README.md)

[![Skill](https://img.shields.io/badge/SKILL.md-agent--skill-111111)](./SKILL.md)
[![Codex](https://img.shields.io/badge/Codex-ready-0A7AFF)](https://github.com/waterdrop26651/Memento-skill)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-6B4EFF)](https://github.com/waterdrop26651/Memento-skill)
[![No secrets](https://img.shields.io/badge/secrets-not%20required-2EA44F)](./SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

![记忆碎片头图](./assets/memory-fragments-banner.jpg)

> “我必须相信，在我的意识之外，还有一个真实世界。”
>
> “我们都会骗自己，好让自己快乐。”

**给容易遗忘、过拟合旧笔记、被碎片污染判断的 agent 用的受控召回系统。**

Memento Skill 把零散实验、笔记、证据和假设整理成分层外部记忆，让 agent 能继续推进项目，而不是把每个旧碎片都误当成当前事实。

别让每一张便签都变成纹身。

## 复制给你的 agent

```text
请安装 https://github.com/waterdrop26651/Memento-skill，并在之后的研究记忆、实验追踪和假设更新任务中启用 $memento-skill。
```

多数用户只需要这一句：让 agent 自己把仓库克隆或安装到 skills 目录，必要时重启 agent 生效。

## 30 秒 Demo

Before:

```text
A7 看起来更好，A8 失败了，可能是 retrieval 改动有效？
旧笔记说 reranking 不行，但那可能是在数据修复之前。
需要下一步实验。
```

After:

```text
CURRENT_STATE.md    -> 当前可行动现实
runs.csv            -> A7/A8 的事实，不写解释
contrasts.csv       -> 预测和观测差异
hypotheses.md       -> 什么证据会改变信念
ACTIVE_TRACKER.csv  -> 只保留仍影响下一步决策的证据
```

结果：下一个 agent 先读热路径，只有明确触发时才召回 archive，然后提出信息量最高的下一组对照，而不是重放所有旧笔记。

最小示例见 [examples/minimal-memory](./examples/minimal-memory)。

## 它做什么

- 把当前证据压缩成短热路径。
- 分离事实、对照和信念。
- 归档旧分支，但不删除。
- 只有触发理由时才召回旧记忆。
- 按信息增益排序下一步实验。

## 适合用在

- 实验很多、笔记分散、旧结论容易污染判断的研究项目。
- 跨会话 agent handoff，但不想每次完整重放上下文。
- 需要追踪假设更新，而不是只堆日志的项目。
- 需要按信息增益选择下一组 ablation、control 或 contrast。

## 记忆结构

```text
CURRENT_STATE.md       # 当前可行动现实
ACTIVE_TRACKER.csv     # 仍有决策梯度的证据
EVIDENCE_LOG.md        # 当前信念的压缩证据
runs.csv               # 事实账本
contrasts.csv          # 预测、控制、结果
hypotheses.md          # 信念、风险、更新规则
archive/               # 冷记忆
ARCHIVE_INDEX.md       # 召回地图
RECALL_NOTES/          # 召回审计记录
```

## 安装

### CLI

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

### 手动安装到 Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/waterdrop26651/Memento-skill.git ~/.codex/skills/memento-skill
```

然后使用：

```text
$memento-skill 帮我为这个项目建立受控记忆 tracker，并按信息增益排序下一组实验对照。
```

## 校验

```bash
python ~/.codex/skills/memento-skill/scripts/validate_tracker.py <tracker_dir>
```

## 可信边界

- 不需要 API key 或任何密钥。
- 没有后台服务。
- 输出是普通 Markdown 和 CSV。
- 自带校验脚本。
- 按渐进披露设计：先读热路径，只有触发时才读 archive。

## Skill 文件

- [SKILL.md](./SKILL.md)
- [agents/openai.yaml](./agents/openai.yaml)
- [references/REFERENCE.md](./references/REFERENCE.md)
- [references/TEMPLATES.md](./references/TEMPLATES.md)
- [scripts/validate_tracker.py](./scripts/validate_tracker.py)

## 分享你的记忆布局

如果你在真实项目里用了 Memento Skill，可以开一个 showcase issue，放出热路径、被归档的碎片，以及它帮你选出的下一组 contrast。好的案例会让这个 skill 变得更锋利。

头图为原创生成资产，不是电影剧照。短台词来源：*Memento* (2000)，见
[IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/) 和
[Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29)。
