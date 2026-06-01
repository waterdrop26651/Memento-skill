# Memento Skill

[English](./README.md)

![记忆碎片头图](./assets/memory-fragments-banner.jpg)

> “我必须相信，在我的意识之外，还有一个真实世界。”
>
> “我们都会骗自己，好让自己快乐。”

**Memento Skill 是给 AI agent 用的受控召回系统。**

它把零散实验、笔记、证据和假设整理成分层外部记忆，让 agent 能继续推进项目，而不是把每个旧碎片都误当成当前事实。

别让每一张便签都变成纹身。

## 它做什么

- 把当前证据压缩成短热路径。
- 分离事实、对照和信念。
- 归档旧分支，但不删除。
- 只有触发理由时才召回旧记忆。
- 按信息增益排序下一步实验。

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

```bash
npx skills add waterdrop26651/Memento-skill -g -a codex -y
```

手动安装到 Codex：

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

## Skill 文件

```text
SKILL.md
agents/openai.yaml
references/REFERENCE.md
references/TEMPLATES.md
scripts/validate_tracker.py
```

头图为原创生成资产，不是电影剧照。短台词来源：*Memento* (2000)，见
[IMDb Quotes](https://www.imdb.com/title/tt0209144/quotes/) 和
[Wikiquote](https://en.wikiquote.org/wiki/Memento_%28film%29)。
