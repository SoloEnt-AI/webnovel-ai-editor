# Origin, Adaptation Notes, and Release Checks

## Origin and web version

This standalone agent skill is adapted from the **SoloEnt AI Editor** web tool at **[https://soloent.ai/en/ai-editor](https://soloent.ai/en/ai-editor)** (baseline prepared on 2026-11-23), backed by live market data from **SoloEnt Insight MCP** (`https://api.soloent.ai/mcp`).

Users who prefer not to install a local skill or configure MCP can run manuscript reviews directly on the web at **[https://soloent.ai/en/ai-editor](https://soloent.ai/en/ai-editor)**. Because the web app may use updated server-side prompts and saved tag-pool snapshots while this skill runs on your chosen agent model with live MCP queries, scores and phrasing can differ between the two.

This repository is self-contained and includes no credentials, market-data snapshots, or user manuscripts.

## Core rules preserved

- WebNovel Original male-audience reader model; Market Fit 25%, Opening Hook 25%, Premise & Power System 20%, Protagonist & Plot Runway 15%, and Readability & Voice 15%.
- Core lanes versus modifiers; samples >=8 use the market score directly, samples of 3-7 are clamped to 20-75, and samples of 1-2 or no match use the fallback.
- Trope stacks, niche compensation, high-score reassessment, track-record bands, and the 64-point caps; the five fixed English verdicts.
- The editorial pool's `market_score` for the current review, rather than topic-advisor medians or ranking positions.

## Intentional adaptations

| SoloEnt AI Editor web tool (`soloent.ai/en/ai-editor`) | Open-source agent skill |
|---|---|
| Materials are collected by a form; file access and saving are prohibited | Read user-specified files, offer partial feedback for missing materials, and save reports when requested |
| The server injects a saved tag-pool snapshot | Read `webnovel_original/6m` through configured SoloEnt Insight MCP (`https://api.soloent.ai/mcp`, authorized via `soloent.ai` OAuth) for every complete review |
| English/Spanish web headings and parser constraints | English by default, with another report language on explicit request; preserve fixed verdicts without guaranteeing website parser compatibility |
| Spanish marker uses `PLATFORM:webnovel_es` | Use `PLATFORM:webnovel` throughout; language is not a separate market |
| Calibration says approximately 80% of submissions score below 50 | Calibrate against evidence, without forcing a score distribution |
| A style mismatch can trigger a different-author claim and end the review | Describe style differences without inferring identity or ghostwriting; continue evaluating the submission |
| Author achievements directly determine a bonus band | Verify achievements before awarding points; previous work remains optional |
| Inflation correction subtracts 8-12 and lowers dimensions, creating double-deduction ambiguity | Correct unsupported dimensions and recalculate once, without subtracting the same correction again or forcing a target band |
| Dimension bounds, rounding, and threshold order are unspecified | Use 0-100 bounds, half-up rounding, and the unrounded base total for the >=80 check before final rounding |
| Mandatory character dialogue and product promotion | Keep specific editorial feedback, omit forced promotion and mocking disclaimers, and identify the review as AI-generated |

For overseas users, the only configured endpoint is **`https://api.soloent.ai/mcp`**. Do not add a domestic fallback. Documentation, metadata, prompts, and examples are written in English. The rubric represents the existing non-English tag-introduction API key with JSON Unicode escapes so the field remains exact without introducing non-English documentation text.

## Before release

1. Review the README, rubric, and intentional adaptations, including the proposed MIT license.
2. Install into temporary projects for both clients. Confirm the entire package is copied and existing destinations are not overwritten.
3. In actual Codex/Claude Code sessions, verify MCP after signing in and authorizing via `soloent.ai` OAuth with an account that has `reference:read`. Keep any auth tokens out of test files and Git. Static checks cannot replace this step.
4. Complete a review using an authorized sample. Also check missing-material, missing-permission, 1-2-work fallback, and 64-point-cap branches. Do not publish real manuscripts or returned service data.
5. Confirm that Git changes contain only the intended files, without `.env`, auth tokens, caches, temporary reports, or private configuration. Check all files for untranslated documentation or examples.
6. Commit/push to the `SoloEnt-AI/webnovel-ai-editor` GitHub repository after user review.

MIT covers the skill's own content and script in this repository. It does not grant rights to the service, market data, or third-party works.

## Contact and feedback

Feedback on the rubric, MCP workflow, or review quality is welcome at **[team@soloent.ai](mailto:team@soloent.ai)**.
