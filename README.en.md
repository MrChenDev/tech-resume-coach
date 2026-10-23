<h1 align="center">Tech Resume Coach</h1>

<p align="center"><a href="README.md">简体中文</a> | <a href="README.en.md">English</a></p>

> An evidence-based resume coach for university students and recent graduates applying for technical roles. Upload a PDF resume and describe your target role to get prioritized feedback and revision suggestions.

**For:** Students and recent graduates in computer science and related majors　|　**Use cases:** Internships, campus recruiting, fall and spring hiring　|　**Resume format:** PDF

[Quick start](#quick-start) · [Installation](#installation) · [How to use](#how-to-use) · [Python and file export](#python-and-file-export) · [Limitations](#privacy-and-limitations)

---

## What this skill does

- **Resume review and scoring:** Identifies strengths, gaps, and supporting evidence using clear scoring criteria. A score is not a hiring probability.
- **Role matching:** Maps the requirements in a job description (JD) to evidence in your resume and highlights gaps.
- **Content editing:** Improves descriptions of projects, internships, competitions, research, coursework, and skills without inventing experience or metrics.
- **Interview preparation:** Suggests likely questions and preparation topics based on your projects and the target role.
- **Complete resume generation:** After you confirm the facts, the skill can export a complete resume as DOCX and PDF.

It covers software development, frontend, embedded software, hardware, data engineering, algorithms, testing, operations, IoT, and other technical roles. Role-specific conclusions are based on the JD and verifiable information you provide. Requirements from one job posting are not generalized as a company's universal preference.

## Quick start

1. Install the skill using the instructions for your agent.
2. Start or refresh a session, then upload a **text-searchable PDF resume**.
3. Invoke the skill and share your hiring stage and target role. Include the JD if you have one.

Copy and customize this prompt:

```text
Use Tech Resume Coach to review the PDF resume I uploaded.

Hiring stage: internship / campus recruiting / fall hiring / spring hiring (fill in)
Target role: fill in the role or technical area
Target city: optional
Target companies: optional
Job description: uploaded / pasted below / not available

Please provide:
1. A resume-to-role match score and the reasons for it
2. My strongest evidence and the issues most likely to hurt screening
3. Prioritized revision suggestions with replacement examples
4. Facts you need me to add or confirm
5. Likely interview follow-up questions based on my projects and how to prepare

Separate information stated in my resume from your inferences. Do not invent experience, responsibilities, technical details, metrics, or outcomes.
If the PDF could not be read completely, identify what is missing first. Do not guess or score unreadable content.
```

## Installation

Python is not required for regular resume reviews. Choose the installation method for your agent.

### Codex Desktop

Clone or copy the repository to the user-level directory:

```text
%USERPROFILE%\.agents\skills\tech-resume-coach\
```

The directory should contain `SKILL.md` directly. Restart Codex, find **Tech Resume Coach** in the **Skills** sidebar, then select it and upload your PDF resume. The Codex Desktop app exposes skills through its Skills sidebar; `$tech-resume-coach` is mainly for Codex CLI and IDE extensions.

### Codex CLI / IDE extensions

Use the user-level directory `%USERPROFILE%\.agents\skills\tech-resume-coach\`. In a new session, enter:

```text
$tech-resume-coach Review my uploaded PDF resume for a backend development internship.
```

### Claude Code

Clone the full repository to:

```text
%USERPROFILE%\.claude\skills\tech-resume-coach\
```

Restart the session, then enter `/tech-resume-coach` and provide the PDF path and target role.

### DeepSeek Harness

Clone the full repository to either user-level directory:

```text
%USERPROFILE%\.dsh\skills\tech-resume-coach\
```

or:

```text
%USERPROFILE%\.agents\skills\tech-resume-coach\
```

Restart the session, then enter `/tech-resume-coach`. For a project-level installation, use `.dsh\skills\tech-resume-coach\` or `.agents\skills\tech-resume-coach\` under the project root.

### Install with npx (Codex CLI / IDE and Claude Code)

Install [Node.js 22.20 or later](https://nodejs.org/en/download/) first. Open PowerShell or a terminal and run the command for your agent:

```powershell
npx skills add MrChenDev/tech-resume-coach --skill tech-resume-coach --global --agent codex
npx skills add MrChenDev/tech-resume-coach --skill tech-resume-coach --global --agent claude-code
```

`npx skills` is a third-party installer. Its current supported-agent list includes Codex and Claude Code, but not DeepSeek Harness. Use the clone/copy instructions above for DeepSeek Harness. If you do not want to install Node.js, clone the repository, download and copy the ZIP, or ask your agent to install it using the prompt below.

### Install manually with Git or ZIP

Example using Git in Windows PowerShell:

```powershell
# Codex and DeepSeek Harness can use this directory
$target = Join-Path $env:USERPROFILE '.agents\skills\tech-resume-coach'
New-Item -ItemType Directory -Force (Split-Path $target) | Out-Null
git clone https://github.com/MrChenDev/tech-resume-coach.git $target

# Claude Code uses its own directory
$target = Join-Path $env:USERPROFILE '.claude\skills\tech-resume-coach'
New-Item -ItemType Directory -Force (Split-Path $target) | Out-Null
git clone https://github.com/MrChenDev/tech-resume-coach.git $target
```

If the destination folder already exists, back it up or compare its contents before replacing anything. For a ZIP installation, extract the archive, rename the extracted repository folder to `tech-resume-coach`, and move it to the appropriate skill directory. Confirm that `SKILL.md`, `references`, and `scripts` are directly inside the skill folder. Do not copy only `SKILL.md`.

### Ask your agent to install it

```text
Please install this repository as a user-level skill for [Codex / Claude Code / DeepSeek Harness]:
https://github.com/MrChenDev/tech-resume-coach

Check the correct skill directory for my agent first. If a skill with the same name already exists, tell me and preserve its files; do not overwrite it.
Copy the complete directory and confirm that it contains SKILL.md, references, and scripts/vendor/pypdf.
When finished, tell me how to invoke it in a new session.
```

### Installation directory reference

| Agent | Windows user-level directory | How to invoke |
|---|---|---|
| Codex Desktop | `%USERPROFILE%\.agents\skills\tech-resume-coach` | Select it from the **Skills** sidebar |
| Codex CLI / IDE | `%USERPROFILE%\.agents\skills\tech-resume-coach` | `$tech-resume-coach` |
| Claude Code | `%USERPROFILE%\.claude\skills\tech-resume-coach` | `/tech-resume-coach` |
| DeepSeek Harness | `%USERPROFILE%\.dsh\skills\tech-resume-coach` or `%USERPROFILE%\.agents\skills\tech-resume-coach` | `/tech-resume-coach` |

On macOS/Linux, the default directories are `~/.agents/skills/tech-resume-coach` for Codex and DeepSeek Harness, and `~/.claude/skills/tech-resume-coach` for Claude Code.

If the agent cannot find the skill, first check that `SKILL.md` is directly inside the directory listed above, then restart or open a new session. Client versions and custom directory settings can affect discovery. See the [Codex](https://developers.openai.com/codex/skills), [Claude Code](https://code.claude.com/docs/en/skills), and [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) documentation for details.

## How to use

Upload a PDF resume, invoke the skill, and provide your target role and hiring stage. Add the JD when available. You can use the prompt in [Quick start](#quick-start). The skill will explain if the file cannot be read fully before making claims about its contents.

## PDF resume requirements

- Use **PDF**. Export Word or image resumes to PDF first. If you cannot upload a PDF, you can paste text exported from the PDF, but the original layout cannot be checked.
- Text-searchable PDFs are best for review.
- Scanned PDFs require OCR or vision support in your agent. If your agent does not have it, provide a searchable PDF or paste the text. The included script does not perform OCR.
- Resolve password protection, file damage, missing pages, or incomplete extraction before continuing with the review.

## Python and file export

### Resume review only

If your agent can read PDFs, **you do not need Python**. If it cannot, the fallback text-extraction script requires Python 3. The `pypdf` dependency is bundled with this skill, so you do not need to install it separately. This script extracts the PDF text layer only; it does not perform OCR.

### Export DOCX / PDF

The local export scripts require Python 3, `python-docx`, `reportlab`, and an available Chinese font. On Windows, select **Add python.exe to PATH** when installing Python, then reopen PowerShell.

Windows:

```powershell
# Change to the actual skill installation directory; this example is for Codex / DeepSeek Harness
cd "$env:USERPROFILE\.agents\skills\tech-resume-coach"
py -3 --version
py -3 -m pip install -r requirements.txt
```

macOS / Linux:

```bash
# This example uses the default Codex / DeepSeek Harness directory; adjust for your installation
cd ~/.agents/skills/tech-resume-coach
python3 --version
python3 -m pip install -r requirements.txt
```

`requirements.txt` contains only the DOCX/PDF export dependencies. If no Chinese font is found, PDF export will ask you to set `RESUME_CJK_FONT`. Check the generated PDF to make sure Chinese characters display correctly. Confirm all resume facts before generating the final files. See [`examples/resume.example.json`](examples/resume.example.json) for sample data and [`references/file-handling.md`](references/file-handling.md) for detailed instructions.

## Privacy and limitations

- The skill does not submit your resume to job sites or other third-party services. When online research is needed, it searches job descriptions and public recruiting information without including personal resume details in search queries.
- How your resume is processed is also governed by your agent client and account privacy settings. Check that the platform is appropriate for your personal information before uploading it.
- The score helps prioritize revisions; it is not an interview-pass or hiring probability. No result can guarantee an interview or an offer.
- Hiring requirements and recruiting schedules change. Company- or role-specific conclusions should use current job descriptions or official recruiting sources and cite them. If information is unavailable, assumptions should be stated clearly.
- This project provides agent instructions and local file scripts. It does not include a job database, and you remain responsible for confirming the facts in your resume.

## Project contents

```text
tech-resume-coach/
├── SKILL.md                  # Core workflow
├── agents/openai.yaml        # Codex interface metadata
├── LICENSE                   # MIT license
├── .gitignore                # Excludes local caches and personal resume files
├── references/               # Scoring, role, writing, and file-handling guidance
├── scripts/                  # Optional PDF extraction and DOCX/PDF export scripts
├── examples/                 # Fictional export data examples
└── evals/                    # Fictional role cases and manual review criteria
```

## License

This project is licensed under the MIT License. The bundled `pypdf` code retains its separate BSD license; see [`scripts/vendor/pypdf-LICENSE`](scripts/vendor/pypdf-LICENSE).
