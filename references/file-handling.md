# 简历文件读取与生成

## 简历输入：PDF

简历文件统一使用 PDF；不把 DOCX、PNG、JPG/JPEG 作为简历文件输入格式。用户没有 PDF 时，请其从原简历导出 PDF。无法上传 PDF 时，可让用户粘贴 PDF 导出的文本作为临时替代，并注明未检查原始版面。

优先使用宿主 Agent 已有的 PDF 读取能力。可复制文本的 PDF 通常最可靠。扫描版、加密、损坏或版面无法完整读取的 PDF，只有宿主提供 OCR/视觉能力时才继续；否则说明具体页码或读取限制，请用户提供可搜索的 PDF 或粘贴文本。不得仅凭文件名、缩略图或不完整文本评分。

### 可选读取脚本

需要本地解析且宿主没有相应能力时，可对含文本层的 PDF 使用下列脚本：

```powershell
py -3 scripts\extract_resume.py <简历PDF路径> --output extracted.txt
```

macOS/Linux 使用 `python3 scripts/extract_resume.py <简历PDF路径> --output extracted.txt`。

脚本需要本机已有 Python 3，并使用随 skill 一起打包的 `pypdf`；用户无需另行安装 pypdf 或其他 PDF 解析依赖。安装时必须复制完整的 `tech-resume-coach` 文件夹，包括 `scripts/vendor/pypdf/`。脚本只提取 PDF 中已有的文本，不执行 OCR。如果 Python 或脚本不可用，先尝试宿主 PDF 能力；仍无法读取时，请用户提供可搜索 PDF 或粘贴导出文本。若页面没有可提取文本，说明扫描页码并停止基于该页的判断。

读取后检查：是否有乱码、页序错乱、表格丢列、图片漏字、文本截断；低置信度字段先询问，不将 OCR 猜测写进简历。

## 输出 DOCX/PDF

先生成并让用户确认简历事实内容，再导出。默认使用简洁、单栏、易解析的文字结构；此 skill 不强制使用视觉模板。

Windows PowerShell：

```powershell
py -3 scripts\export_resume.py --input resume.json --output-dir output
```

macOS/Linux：

```sh
python3 scripts/export_resume.py --input resume.json --output-dir output
```

运行前需安装 Python 3，并在 skill 目录执行 `python -m pip install -r requirements.txt`（Windows 可用 `py -3 -m pip install -r requirements.txt`）。`requirements.txt` 安装 DOCX/PDF 导出依赖，不包含 pypdf，因为 PDF 读取库已随 skill 打包。`resume.json` 字段说明与示例见 `examples/resume.example.json`。PDF 生成需要本机存在中文字体；脚本会查找常见字体路径，也可以用 `RESUME_CJK_FONT` 指定字体文件。PDF 导出后确认文件存在且中文字体可读。脚本或依赖不可用时，不声称已生成文件，改为提供完整可复制内容并说明限制。

## 用户文件保护

- 只读取完成本次请求必需的简历和 JD，不额外扫描用户目录。
- 不把简历上传到第三方服务或公开站点；联网搜索招聘信息时不要发送简历个人信息。
- 生成件放在用户指定目录；未指定时先告知默认输出位置或使用当前工作目录下新建的输出子目录。
- 输出前提醒用户检查电话、邮箱、链接等个人信息和所有待确认字段。
- 简历及导出文件属于个人信息；不要将真实简历、提取出的正文或生成件放进源码仓库。仓库 `.gitignore` 已忽略常见简历附件和本地导出文件；新增其他个人数据文件时仍须先检查 Git 变更列表。
- Agent 对话平台可能按其自身服务规则处理用户主动上传的附件；不要把“skill 不调用招聘网站上传简历”表述为“简历不会离开用户设备”。
