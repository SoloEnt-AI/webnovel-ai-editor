# WebNovel AI Editor Skill

Give your agent an outline and the first three chapters. It uses the **editorial tag pool from SoloEnt Insight MCP** to produce five scores, a verdict, packaging suggestions, and specific revision priorities.

Works with Codex, Claude Code, WorkBuddy, and other agents that support local Markdown instructions and MCP.

> This is an AI simulated editorial review, not an official WebNovel assessment. It does not submit manuscripts, apply for contracts, or review legal contract terms. A score is not a probability of acceptance.

> [!IMPORTANT]
> **Recommended Model Tier:** Use a model with **high instruction-following accuracy and strong execution—at least Claude Sonnet 5.5 or an equivalent-tier model**. **Strongly avoid** overly agreeable/sycophantic or highly imaginative models, as they tend to inflate scores, miss rubric rules, and introduce significant error into the review results.

## What you need

1. An agent client that can read local files and call remote Streamable HTTP MCP tools with OAuth sign-in (such as Codex, Claude Code, WorkBuddy, or another compatible agent).
2. A **[soloent.ai](https://soloent.ai)** account authorized to **SoloEnt Insight MCP** (`https://api.soloent.ai/mcp`) with access to the editorial tag-pool tool (`insight_reference_tags`, `reference:read`). Register or sign in on [soloent.ai](https://soloent.ai), connect the MCP server in your client, and complete browser OAuth authorization—no manual API key is required. You can view client setup guides and manage connected apps anytime in the SoloEnt dashboard under **Connect Other AI** (`https://soloent.ai/en/dashboard/connections`). Metered MCP tool calls deduct from your SoloEnt membership credits. A third-party model subscription or model API key alone does not authorize SoloEnt Insight MCP.
3. An outline and the first three chapters. Title, synopsis, previous work, and verified track record are optional. You can review the story before an English version exists, but English readability remains unverified.

The rubric covers **long-form fiction for the WebNovel Original male-audience market**, regardless of protagonist gender. Reports default to English; you may explicitly request another language. Market scoring uses only the Original six-month tag pool, not RoyalRoad or the translation pool.

## Quick start: ask your agent to configure it

Clone or download the repository. For an unpublished local copy, use its actual local path. Once published, the repository commands are:

```bash
git clone https://github.com/SoloEnt-AI/webnovel-ai-editor.git
cd webnovel-ai-editor
```

Paste this into Codex or Claude Code, replacing the two paths:

```text
Install and configure the WebNovel contract readiness review skill for me.
Skill directory: /absolute/path/webnovel-ai-editor
Novel project: /absolute/path/my-novel
Scope: install the skill only in this novel project.

Read references/setup.md in the skill directory first, then configure this client.
Preserve existing skills, MCP servers, and other settings. Reuse a correct connection.
Use SoloEnt Insight MCP: https://api.soloent.ai/mcp (Streamable HTTP with SoloEnt OAuth).
Do not read, request, or print any tokens or credentials.
After configuring the server, tell me how to complete soloent.ai OAuth sign-in in this client if it is not yet authorized.
Verify the setup by actually calling insight_sites and insight_reference_tags.
For the latter, use {"site":"webnovel_original","window":"6m"}.
If the setup cannot take effect in this session, explain what to run after authenticating and reconnecting.
Do not claim the connection works merely because configuration was written.
```

The agent can install the skill and prepare the MCP server entry for you. You then complete browser OAuth sign-in with your [soloent.ai](https://soloent.ai) account and approve your client's trust prompts. See the [setup guide](references/setup.md) for step-by-step instructions and troubleshooting.

## Manual installation

Requires Python 3.9+. From the repository root, run the appropriate command with your actual novel project path:

```bash
# Codex
python3 scripts/install.py --client codex --project /path/to/novel-project

# Claude Code
python3 scripts/install.py --client claude --project /path/to/novel-project
```

The installer does not use the network, configure MCP, or access keys. It refuses to overwrite an existing destination. Add `--dry-run` to preview. For user-wide installation, use `--scope user` and omit `--project`. Without Python, copy the whole folder into your client's skill directory.

Then follow the [setup guide](references/setup.md) (or the SoloEnt dashboard's **Connect Other AI** page at `https://soloent.ai/en/dashboard/connections`) to add the MCP server and sign in with your [soloent.ai](https://soloent.ai) account:

| Client | Project skill location | MCP template |
|---|---|---|
| Codex | `.agents/skills/webnovel-ai-editor/` | [codex.toml.example](config/codex.toml.example) |
| Claude Code | `.claude/skills/webnovel-ai-editor/` | [claude.mcp.json.example](config/claude.mcp.json.example) |
| Other agents | Their skill directory, or direct loading of `SKILL.md` | Native Streamable HTTP (`https://api.soloent.ai/mcp`) with browser OAuth authorization via `soloent.ai` |

Complete OAuth authorization in your client (or start a new session after authenticating), then verify that `insight_reference_tags` can be called. **Access only to `insight_advisor_intl_*` is insufficient:** it does not provide the `market_score` this rubric needs. Client configuration is documented in the [Codex MCP guide](https://developers.openai.com/codex/mcp/) and [Claude Code MCP guide](https://code.claude.com/docs/en/mcp).

## Run a review

Codex:

```text
Use $webnovel-ai-editor to assess this book's contract readiness.
Outline: draft/outline.md
First three chapters: draft/chapter-01.md, draft/chapter-02.md, draft/chapter-03.md
Title and synopsis: draft/pitch.md
I am a new author with no previous work. Write a full review in English and save it in reviews/.
```

Claude Code:

```text
/webnovel-ai-editor
My outline is draft/outline.md. The opening chapters are draft/chapter-01.md through chapter-03.md.
Check Insight MCP, then review the manuscript and write the report in English.
```

Other agents, or when the skill is not discovered automatically:

```text
Read /absolute/path/webnovel-ai-editor/SKILL.md.
Follow it and its references to review the outline and first three chapters in this project's draft/ folder.
Use the configured SoloEnt Insight MCP connection to obtain the editorial tag pool.
If permissions or materials are missing, explain the gap rather than inventing a complete score.
```

You may paste the manuscript into chat instead; no fixed filenames are required. You can also ask for opening-only feedback or a re-review against a previous report. Focused feedback does not receive a full final tier.

## What the report includes

- Five dimensions, each out of 100: Market Fit, Opening Hook, Premise & Power System, Protagonist & Plot Runway, and Readability & Voice.
- Judgments tied to manuscript evidence, actual tag definitions, and sample counts, with small-sample fallback, high-score reassessment, and optional verified track-record adjustments.
- A final 0-100 score and one of five simulated verdicts. See the [rubric](references/rubric.md) for tiers and calculations.
- Two English title ideas, an English synopsis of at most 60 words, matching tags, and prioritized revision advice.
- Query time, data update time, review scope, and unverified items for later comparison. Preview the [report format](references/report.md).

If the outline or opening chapters are incomplete, MCP is unavailable, permissions are missing, or data is invalid, the agent offers limited feedback rather than a fabricated full score. Requested report files preserve the original manuscript and earlier reports.

## Data and licensing

The skill's text, templates, and script use the [MIT License](LICENSE). **The hosted SoloEnt Insight service, credentials, returned data, user manuscripts, and third-party works are not licensed by this grant.** Service access must be authorized; the provider defines terms, fees, and quotas.

The skill sends Insight only the site and time window, not the manuscript. Your agent's model processes the manuscript under your client's and model provider's data settings. The skill includes no administrative writes, bulk scraping, submission, or signing tools.

## Web version, maintenance, and feedback

This skill is adapted from the **SoloEnt AI Editor** web tool at **[https://soloent.ai/en/ai-editor](https://soloent.ai/en/ai-editor)**, bringing its five-dimension WebNovel review framework to independent agents. **If you do not want to install the skill locally or configure MCP, you can test and review your manuscript directly in the browser at [https://soloent.ai/en/ai-editor](https://soloent.ai/en/ai-editor).**

Results between the web tool and this standalone skill may vary slightly because of different models, prompt updates, and live MCP queries versus website snapshots. See [adaptation notes and maintenance](references/maintenance.md) for intentional differences from the web version and release checks.

Questions, suggestions, or feedback on the skill and rubric are always welcome—reach out to the SoloEnt team at **[team@soloent.ai](mailto:team@soloent.ai)**.
