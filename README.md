<h1 align="center">Tech Resume Coach</h1>

<p align="center"><a href="README.md">简体中文</a> | <a href="README.en.md">English</a></p>

> 面向大学生与应届毕业生的技术岗简历教练。上传 PDF 简历，说明目标岗位，即可获得有证据、有优先级的诊断与修改建议。

**适用人群：** 计算机及相关专业在校生、应届毕业生　|　**适用场景：** 实习、校招、秋招、春招　|　**简历输入：** PDF

[快速开始](#快速开始) · [安装](#安装) · [怎么使用](#怎么使用) · [Python 与文件生成](#python-与文件生成) · [能力边界](#能力边界)

---

## 这个 Skill 能帮你做什么

- **简历诊断与评分：** 按明确的评分维度指出优势、短板和依据，不把分数说成录用概率。
- **岗位匹配：** 对照你提供的岗位 JD，逐项映射要求、简历证据和差距。
- **内容改写：** 优化项目、实习、竞赛、科研、课程设计和技能描述，保留真实贡献，不编造经历或数据。
- **面试准备：** 根据简历项目和岗位要求整理可能的追问与准备方向。
- **生成完整简历：** 你确认内容后，可按需导出 DOCX 和 PDF。

覆盖软件研发、前端、嵌入式、硬件、数据工程、算法、测试、运维、IoT 等技术方向。岗位判断以你提供的 JD 和可核实的信息为准；不会把某家企业的个别经验泛化成“企业偏好”。

## 快速开始

1. 按下方对应客户端安装 Skill。
2. 新开或刷新会话，上传一份**可搜索文字的 PDF 简历**。
3. 按客户端调用 Skill，并告诉它求职阶段、目标岗位；有 JD 时一并提供。

可以直接复制这段提示词：

```text
请使用 Tech Resume Coach 诊断我上传的 PDF 简历。

求职阶段：实习 / 校招 / 秋招 / 春招（填写）
目标岗位：填写岗位名称或技术方向
目标城市：可选
目标公司：可选
岗位 JD：已上传 / 粘贴如下 / 暂无

请给出：
1. 简历与目标岗位的匹配诊断分及评分理由
2. 最有竞争力的证据和最影响筛选的问题
3. 按优先级排列的修改建议，并给出可替换的改写示例
4. 需要我补充或确认的事实
5. 基于项目经历的面试追问和准备建议

请区分简历中已有的信息与推断，不要编造经历、职责、技术细节、指标或结果。
如果 PDF 没有完整读取，请先说明具体缺失，不要猜测或打分。
```

## 安装

Skill 不需要安装到 Python 环境才能进行常规诊断。选择与你使用的 Agent 对应的方式即可。

### Codex 桌面版

将仓库克隆或复制到用户级目录：

```text
%USERPROFILE%\.agents\skills\tech-resume-coach\
```

目录内应直接有 `SKILL.md`。重新打开 Codex 后，在侧边栏 **Skills** 中找到并使用 **Tech Resume Coach**，然后上传 PDF、描述目标岗位。Codex 桌面版可从 Skills 侧边栏查看和使用 Skill；`$tech-resume-coach` 主要用于 Codex CLI 和 IDE 扩展。

### Codex CLI / IDE 扩展

安装目录同为用户级 `%USERPROFILE%\.agents\skills\tech-resume-coach\`。在新会话输入：

```text
$tech-resume-coach 请诊断我上传的 PDF 简历，目标岗位是后端开发实习。
```

### Claude Code

将完整仓库克隆到：

```text
%USERPROFILE%\.claude\skills\tech-resume-coach\
```

重开会话后输入 `/tech-resume-coach`，并上传或提供 PDF 路径和目标岗位。

### DeepSeek Harness

将完整仓库克隆到以下任一用户级目录：

```text
%USERPROFILE%\.dsh\skills\tech-resume-coach\
```

或：

```text
%USERPROFILE%\.agents\skills\tech-resume-coach\
```

重新打开会话后输入 `/tech-resume-coach`。项目级安装可放在项目根目录的 `.dsh\skills\tech-resume-coach\` 或 `.agents\skills\tech-resume-coach\`。

### 使用 npx 安装（Codex CLI / IDE、Claude Code）

需要先安装 [Node.js 22.20 或更高版本](https://nodejs.org/en/download/)。打开 PowerShell 或终端，分别运行需要的命令：

```powershell
npx skills add MrChenDev/tech-resume-coach --skill tech-resume-coach --global --agent codex
npx skills add MrChenDev/tech-resume-coach --skill tech-resume-coach --global --agent claude-code
```

`npx skills` 是第三方安装器；当前支持列表包含 Codex 和 Claude Code，没有 DeepSeek Harness。DeepSeek Harness 请使用上面的克隆/复制方式。若不想安装 Node.js，也可使用 Git 克隆、下载 ZIP 后复制，或让 Agent 按下方提示词协助安装。

### Git 克隆或 ZIP 手动安装

Git 克隆示例（Windows PowerShell）：

```powershell
# Codex 与 DeepSeek Harness 可共用此目录
$target = Join-Path $env:USERPROFILE '.agents\skills\tech-resume-coach'
New-Item -ItemType Directory -Force (Split-Path $target) | Out-Null
git clone https://github.com/MrChenDev/tech-resume-coach.git $target

# Claude Code 使用自己的目录
$target = Join-Path $env:USERPROFILE '.claude\skills\tech-resume-coach'
New-Item -ItemType Directory -Force (Split-Path $target) | Out-Null
git clone https://github.com/MrChenDev/tech-resume-coach.git $target
```

如果目标文件夹已经存在，不要直接覆盖；先备份或比较旧文件。下载 ZIP 后解压，将解压出来的仓库文件夹重命名为 `tech-resume-coach`，再放到对应技能目录。确认目录中直接包含 `SKILL.md`、`references` 和 `scripts`；不要只复制 `SKILL.md`。

### 让 Agent 帮忙安装

```text
请帮我把这个仓库安装为【Codex / Claude Code / DeepSeek Harness】的用户级 Skill：
https://github.com/MrChenDev/tech-resume-coach

先检查对应客户端的正确技能目录。若已有同名 Skill，先告诉我并保留原文件，不要直接覆盖。
请复制完整目录，并确认目标目录里有 SKILL.md、references 和 scripts/vendor/pypdf。
完成后告诉我如何在新会话中调用。
```

### 安装目录速查

| 客户端 | Windows 用户级目录 | 调用方式 |
|---|---|---|
| Codex 桌面版 | `%USERPROFILE%\.agents\skills\tech-resume-coach` | 从侧边栏 **Skills** 中选择 |
| Codex CLI / IDE | `%USERPROFILE%\.agents\skills\tech-resume-coach` | `$tech-resume-coach` |
| Claude Code | `%USERPROFILE%\.claude\skills\tech-resume-coach` | `/tech-resume-coach` |
| DeepSeek Harness | `%USERPROFILE%\.dsh\skills\tech-resume-coach` 或 `%USERPROFILE%\.agents\skills\tech-resume-coach` | `/tech-resume-coach` |

macOS/Linux 用户目录对应为 `~/.agents/skills/tech-resume-coach`（Codex、DeepSeek Harness）和 `~/.claude/skills/tech-resume-coach`（Claude Code）。

如果安装后找不到 Skill，先确认 `SKILL.md` 是否位于上表目录中，再重启/新建会话。客户端版本和自定义目录配置可能影响发现路径，可参考 [Codex](https://developers.openai.com/codex/skills)、[Claude Code](https://code.claude.com/docs/en/skills) 和 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) 的官方说明。

## 怎么使用

上传 PDF 简历并调用 Skill，说明求职阶段和目标岗位；有岗位 JD 时一并提供。可以直接使用[快速开始](#快速开始)中的提示词。若文件无法完整读取，Skill 会先说明缺失内容，再进行诊断。

## PDF 简历要求

- 统一使用 **PDF**。Word 或图片简历请先导出为 PDF；无法上传 PDF 时，可粘贴 PDF 导出的文本，但无法检查原始版面。
- 可搜索文字的 PDF 最适合诊断。
- 扫描版 PDF 需要当前 Agent 具备 OCR/视觉读取能力。若没有，请提供可搜索 PDF 或粘贴文字；不要根据模糊截图推断内容。
- 加密、损坏、缺页或读取不完整的文件，应先处理读取问题，再继续诊断。

## Python 与文件生成

### 只做简历诊断

如果 Agent 自带 PDF 阅读能力，**不用安装 Python**。如果 Agent 无法读取 PDF，备用文本提取脚本需要 Python 3；`pypdf` 已随 Skill 提供，不用单独安装。该脚本只提取 PDF 文字层，不做 OCR。

### 导出 DOCX / PDF

本地导出脚本需要 Python 3、`python-docx`、`reportlab` 和可用的中文字体。Windows 安装 Python 时建议勾选 **Add python.exe to PATH**，完成后重新打开 PowerShell。

Windows：

```powershell
# 进入 Skill 实际安装目录；以下以 Codex / DeepSeek Harness 为例
cd "$env:USERPROFILE\.agents\skills\tech-resume-coach"
py -3 --version
py -3 -m pip install -r requirements.txt
```

macOS / Linux：

```bash
# 以下以 Codex / DeepSeek Harness 的默认目录为例；其他客户端请换成实际安装目录
cd ~/.agents/skills/tech-resume-coach
python3 --version
python3 -m pip install -r requirements.txt
```

`requirements.txt` 只包含 DOCX/PDF 导出依赖。中文字体缺失时，PDF 导出会提示设置 `RESUME_CJK_FONT`；PDF 生成后应检查中文是否正常显示。简历事实需先由你确认，再生成最终文件。数据字段示例见 [`examples/resume.example.json`](examples/resume.example.json)，详细步骤见 [`references/file-handling.md`](references/file-handling.md)。

## 隐私与能力边界

- Skill 不会把简历发到招聘网站或其他第三方服务。需要联网核实岗位信息时，只查询 JD 和公开招聘信息，不把简历个人信息放进搜索请求。
- 简历内容如何被处理，仍受你使用的 Agent 客户端及其账户/隐私设置约束；提交前请自行确认平台适合处理你的个人信息。
- 诊断分用于整理修改优先级，不代表通过率或录用概率。任何结果都不能保证获得面试或录用。
- 招聘要求、招聘季安排会变化。企业/岗位特定结论应基于当年 JD 或官方招聘来源，并注明来源；没有资料时会明确说明假设。
- 本项目提供的是 Agent 工作指引和本地文件脚本，不包含招聘数据库，也不替代用户对简历事实的确认。

## 项目内容

```text
tech-resume-coach/
├── SKILL.md                  # 核心工作流程
├── agents/openai.yaml        # Codex 界面信息
├── LICENSE                   # MIT 许可证
├── .gitignore                # 忽略本地缓存和个人简历文件
├── references/               # 评分、岗位、写作和文件处理规则
├── scripts/                  # 可选 PDF 提取与 DOCX/PDF 导出脚本
├── examples/                 # 虚构的导出数据示例
└── evals/                    # 虚构岗位案例和人工验收要点
```

## 许可证

本项目采用 MIT License。随包分发的 `pypdf` 代码保留其单独的 BSD 许可证，见 [`scripts/vendor/pypdf-LICENSE`](scripts/vendor/pypdf-LICENSE)。
