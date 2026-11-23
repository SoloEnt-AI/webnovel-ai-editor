# Installation, Configuration, and Verification

For users and agents performing setup. Client instructions last checked: 2026-11-23.

> [!IMPORTANT]
> **Recommended Model Tier:** Run this skill with a model that has **high instruction-following accuracy and strong execution—at least Claude Sonnet 5.5 or an equivalent-tier model**. **Strongly avoid** overly agreeable/sycophantic or highly imaginative models, which can cause significant scoring and judgment errors.

## Connection contract

Overseas users must connect to `https://api.soloent.ai/mcp`. Do not configure a domestic endpoint as a backup or fallback.

| Setting | Value |
|---|---|
| Suggested client server name | `soloent-insight` (or `soloent`) |
| MCP URL | `https://api.soloent.ai/mcp` |
| Transport | Streamable HTTP (`http` in Claude Code, `streamableHttp` in WorkBuddy) |
| Authentication | OAuth sign-in via your **[soloent.ai](https://soloent.ai)** account (browser authorization in your client) |
| Dashboard setup guide | `https://soloent.ai/en/dashboard/connections` (**Connect Other AI**) |
| Minimum capability | `reference:read` (editorial tag-pool tool) |
| Required tool | `insight_reference_tags` |
| Basic verification tool | `insight_sites` |
| Review arguments | `site=webnovel_original`, `window=6m` |

Register or sign in on **[soloent.ai](https://soloent.ai)**, add `https://api.soloent.ai/mcp` as a Streamable HTTP MCP server in your client, and complete browser OAuth authorization. No manual API key is required for standard user setup.

When you authorize a client on `soloent.ai`:
- The client can call SoloEnt MCP tools on your behalf; metered or paid tools deduct from your SoloEnt membership credits.
- The client **cannot** call SoloEnt AI models, read your local files, or access your SoloEnt chat history.
- You can disconnect any authorized client anytime in SoloEnt Dashboard → **Connect Other AI** (`https://soloent.ai/en/dashboard/connections`) → **Connected Apps**.

Do not use the administrative `/mcp-admin` endpoint or an `sk_` administrative key. A third-party ChatGPT/Claude subscription or model API key alone does not authorize SoloEnt Insight MCP. International topic-advisor tools (`insight_advisor_intl_*`) alone are insufficient—your connection must expose `insight_reference_tags` (`reference:read`). If `insight_reference_tags` is missing after signing in, check your SoloEnt account plan or contact `team@soloent.ai`. Do not promise free access, quotas, or permanent availability; SoloEnt defines service terms.

## Install the skill

Install the entire folder, preserving the relative locations of `references/`, `agents/`, `config/`, and `scripts/`. The installer only copies this skill's files: **it does not modify MCP configuration, read or store keys, or use the network**. It requires Python 3.9+ and refuses to overwrite an existing destination.

Run from the `webnovel-ai-editor` repository root. Replace `/path/to/novel-project` with the actual absolute path to an existing novel project:

```bash
# Codex: install into the project's .agents/skills/
python3 scripts/install.py --client codex --project /path/to/novel-project

# Claude Code: install into the project's .claude/skills/
python3 scripts/install.py --client claude --project /path/to/novel-project
```

Add `--dry-run` to either command to preview the path without writing. For user-wide installation, use `--scope user` and omit `--project`:

```bash
python3 scripts/install.py --client codex --scope user
python3 scripts/install.py --client claude --scope user
```

| Client | Project skill location | User skill location |
|---|---|---|
| Codex | `<project>/.agents/skills/webnovel-ai-editor/` | `~/.agents/skills/webnovel-ai-editor/` |
| Claude Code | `<project>/.claude/skills/webnovel-ai-editor/` | `~/.claude/skills/webnovel-ai-editor/` |

Without Python, copy this whole folder into the relevant location. No SoloEnt-specific `plugin.json` is required. Other agents should use their own skill directories. If an agent cannot discover skills automatically, ask it to read this folder's `SKILL.md` directly and follow the relative reference links.

## Authorize with your soloent.ai account

Sign up or sign in at [soloent.ai](https://soloent.ai). You can also open **Connect Other AI** in your SoloEnt dashboard (`https://soloent.ai/en/dashboard/connections`) for ready-to-copy client configurations.

Standard setup uses your client's built-in **OAuth browser sign-in**—you do not need to paste passwords, tokens, or API keys into chat, config files, or environment variables. Do not paste any tokens or credentials into chat, repositories, screenshots, or reports.

## Configure MCP in ChatGPT / Codex

### Option A: Codex / ChatGPT UI (recommended)

1. Open **Settings → Plugins** and click **Add MCP Server** in the top-right corner.
2. Enter a server name (for example, `soloent` or `soloent-insight`).
3. Set Type to **Streamable HTTP** and URL to `https://api.soloent.ai/mcp`.
4. Switch to the **MCP** tab, select the server, and click **Authenticate**.
5. Complete sign-in and click **Authorize** on the `soloent.ai` browser page, then close the tab.

### Option B: `~/.codex/config.toml`

Merge the table in [config/codex.toml.example](../config/codex.toml.example) into the **user configuration at `~/.codex/config.toml`**:

```toml
[mcp_servers.soloent-insight]
url = "https://api.soloent.ai/mcp"
```

A trusted project's `.codex/config.toml` is another option, subject to the installed client's support and trust prompts. User configuration is usually simpler for initial setup. Merge only this entry and preserve other settings. Reuse an existing correct connection. If a same-named server uses another address or authentication method, explain the conflict before changing it.

The dependency in `agents/openai.yaml` is a declaration only: **it does not authenticate the connection automatically**. After adding the server, trigger OAuth authentication in Codex (or run `codex mcp login soloent-insight` if supported by your Codex CLI version), reconnect MCP or start a new session, and perform the verification below.

## Configure MCP in Claude Code

For project scope, merge `mcpServers.soloent-insight` from [config/claude.mcp.json.example](../config/claude.mcp.json.example) into `.mcp.json`:

```json
{
  "mcpServers": {
    "soloent-insight": {
      "type": "http",
      "url": "https://api.soloent.ai/mcp"
    }
  }
}
```

This project configuration can be shared safely because it contains no credentials. Follow the client's project-MCP trust prompt on first use, then run `/mcp` inside Claude Code to sign in and authorize with your `soloent.ai` account in the browser.

For a user-wide server, run the following in a local terminal after checking for a same-name conflict (writing the config alone does not complete OAuth):

```bash
claude mcp add --transport http --scope user soloent-insight https://api.soloent.ai/mcp
```

Then run `/mcp` inside Claude Code to complete browser OAuth sign-in with your `soloent.ai` account. The skill and MCP connection can use different scopes: a project skill can reuse a user-wide server. Do not assume Claude Code's `.mcp.json` also configures Claude's web app or another client.

## Configure MCP in WorkBuddy or other clients

1. Open **Connect Other AI** (`https://soloent.ai/en/dashboard/connections`) in your SoloEnt dashboard and copy the JSON snippet for your client (for example, WorkBuddy uses `type: "streamableHttp"` and `url: "https://api.soloent.ai/mcp"`).
2. Add it as a custom MCP server in your client, click **Trust** (if prompted), and click **Connect**.
3. Complete sign-in and click **Authorize** on the `soloent.ai` browser page.

## Instructions for an agent performing setup

A request to install or configure authorizes the necessary setup; do not ask for confirmation at every step:

1. Identify the client and requested project. If essential information is missing, ask only about the client, target project, or scope—never ask for passwords or tokens. You can read the downloaded skill first. Default to a project-scoped skill and prefer an existing MCP connection.
2. Run the installer or copy the skill into the client's directory. If the destination exists, establish the version and requested update scope. Do not delete it to bypass overwrite protection.
3. Use client management tools or structured edits to merge the MCP entry (`https://api.soloent.ai/mcp`). Existing configuration may contain other credentials: do not print it in full. Report only the server name, endpoint, and change result. Preserve other servers and options.
4. Guide the user to sign in on `soloent.ai` and complete OAuth authorization in their client (and reconnect if needed). If you cannot modify configuration directly, provide the exact snippet and destination, clearly stating that it is not yet active.
5. After the user authorizes and reconnects, verify the actual tools as described below. Never claim the connection works without a successful call. If tools cannot refresh in this session, provide verification instructions for the next one.

Do not run `env`, `printenv`, or `cat ~/.codex/config.toml`, or dump complete client configuration. Do not read `.env`, build authentication headers containing tokens, or test the service with HTTP scripts.

## Verify the connection

Use the client's MCP tool discovery, allowing client-added name prefixes:

1. Confirm that `insight_sites` and `insight_reference_tags` are available.
2. Call `insight_sites` with `{}` and confirm `webnovel_original` is supported.
3. Call `insight_reference_tags` with `{"site":"webnovel_original","window":"6m"}`.
4. Check the site/window, a nonempty pool, and valid candidate `work_count`, `market_score`, and tag-introduction fields. The [rubric](rubric.md#11-match-tags) specifies the exact introduction property using JSON Unicode escapes. Record the update time without printing the full pool or credentials.
5. Report actual results separately: skill discovered, MCP connected, editorial capability available, and data valid. Writing configuration alone does not pass the last three checks.

A connection check needs no manuscript and does not perform a model manuscript review. Whether remote queries incur charges is determined by the provider.

## Troubleshooting

| Symptom | Action |
|---|---|
| Skill not found | Check that `SKILL.md` is directly inside the skill directory and that the session started in the right project. Reload skills/start a new session, or read the absolute path directly. |
| `insight_sites` exists but the editorial tool is missing | Check your `soloent.ai` account/plan access for `reference:read` (or contact `team@soloent.ai`), then reconnect to refresh the tool list. |
| Only `insight_advisor_intl_*` is available | Topic-advisor access cannot replace the editorial tag pool. |
| HTTP 401 / `UNAUTHORIZED` | Re-run OAuth authentication with your `soloent.ai` account in your client and confirm the URL is `https://api.soloent.ai/mcp`. |
| `KEY_REVOKED` / `KEY_EXPIRED` | Your authorization session was revoked or expired—re-authenticate in your client via `soloent.ai` (or check Connected Apps in your dashboard). |
| `CLIENT_DISABLED` | Check your account/app connection status in SoloEnt Dashboard or contact `team@soloent.ai`. |
| HTTP 403 / `CAPABILITY_DENIED` / `tool not authorized` | Check your SoloEnt plan/capability access (or credits) and reconnect after changes. |
| HTTP 405 / SSE connection failure | Use Streamable HTTP. Traditional GET SSE is not provided; a browser GET is not a connectivity test. |
| Empty or truncated data | Check site/window and client output limits. Stop full scoring if complete valid data remains unavailable. |
| Rate limiting or temporary service failure | Retry a temporary failure at most once, then preserve progress for later. |
| Desktop client fails but terminal works | Re-authenticate inside the desktop client's own MCP settings; OAuth sessions are typically stored per client. |

## Official client references

- [Codex skills and installation locations](https://developers.openai.com/codex/skills/)
- [Codex MCP configuration](https://developers.openai.com/codex/mcp/)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code MCP and environment-variable expansion](https://code.claude.com/docs/en/mcp)

Clients change. If local paths or fields differ, consult the installed client's official documentation. Do not change the review rubric or expand Insight permissions to fix a client configuration issue.
