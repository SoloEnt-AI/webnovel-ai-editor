# Report Format

Use this format only when the required materials and valid MCP data are available. Write in **English by default**, or another language explicitly requested by the user. Preserve fixed English verdicts, tier codes, and English tag names. Headings may be translated for a requested report language. This standalone agent report is not guaranteed to work with the website's parser.

Replace all template instructions with actual findings. Keep paragraphs short and conclusions direct. You may address the author as "Daoist," but the editorial persona must not conceal the AI pre-review status.

## Complete report

```markdown
# "[Title]" - WebNovel AI Editor

**Verdict: [Fixed English verdict], final score [NN]/100.**
[One sentence naming the main reason for the contract-readiness judgment.]

This is an AI simulated editorial review, not an official WebNovel decision. The score is not a probability of receiving a contract.

## Scope and Data

- Target: WebNovel Original male-audience market.
- Read: [Actual outline and chapter filenames/ranges; list any prologue separately.]
- Manuscript language: [Actual language; without an English draft, state that English readability and localization remain unverified.]
- Author track record: [Not provided / unverified / verified with sources; note any lane change.]
- Data: SoloEnt Insight, webnovel_original, 6m.
- Query time: [Actual time and time zone.]
- Data update time: [generated_at, or "Not provided by the service."]

## Editor's Assessment

[A manuscript-specific paragraph: its strongest feature, its biggest retention problem, and why.]

## Market Fit

- One-line pitch: [What the protagonist gains, does, and wants to achieve.]
- Story summary: [The main arc; distinguish delivered scenes from outline plans.]
- Primary tag: [English name; N sampled works in the six-month window; actual raw market_score.]
- Match evidence: [Paraphrase the definition and identify manuscript evidence; state if there is no valid match.]
- Secondary tags: [At most two; distinguish core lanes from modifiers.]
- Score path: [Baseline -> trope stack -> content risk -> niche compensation -> adopted Market Fit.]
- Reader appetite: [Agency, progression loop, and payoff rhythm; explain any fallback.]

## Five-Dimension Scores

| Dimension | Adopted score /100 | Key evidence |
|---|---|---|
| Market Fit | [NN] | [Tag and main-story evidence.] |
| Opening Hook | [NN] | [First payoff and chapter-end scenes.] |
| Premise & Power System | [NN] | [Interaction of mechanics and adversity.] |
| Protagonist & Plot Runway | [NN] | [Agency, desire, and room for escalation.] |
| Readability & Voice | [NN] | [Short quotation or specific passage.] |

[For each dimension, briefly explain what works, the main problem, and the fix. For adjusted scores, show the ladder baseline and actual bonuses/deductions; otherwise say "No adjustments." Do not count Market Fit twice.]

## Packaging Check

- Title and synopsis: [Do they communicate the actual lane and payoff promise? Note missing items.]
- English title ideas: [Two options emphasizing the core hook.]
- English synopsis: [At most 60 English words; do not invent events absent from the manuscript.]
- Suggested English tags: [3-5 genuinely matching tags from this pool; fewer if necessary.]

## Risks and Strengths

[Summarize important risks, strengths, and unverified items without applying adjustments again.]
[If explicit adult sexual content is present, add one neutral reminder to check mature-content labels and current platform rules.]

## Final Score and Verdict

- Weighted base total: [Actual pre-reassessment result, shown to two decimal places.]
- High-score reassessment: [Not triggered / supported and retained / dimension corrections and recalculated base total.]
- Track-record adjustment: [Not triggered / signed adjustment with evidence and sources; no bonus for unverified results.]
- Red-line cap: [Not triggered / cap of 64 and reason.]
- Final score: [NN]/100.
- Verdict: [Fixed English verdict; tier code.]

## Next Steps

[Use the appropriate branch below and give specific actions.]

Market rankings describe historical sample performance. The platform makes its own submission decisions.

<!--TIER:[tier]|SCORE:[integer]|PLATFORM:webnovel-->
```

## Choose the next-steps branch

- `platinum` / `speed`: **Pre-Submission Improvement Plan.** Give 1-2 polishing priorities and stockpile/update planning, without promising acceptance.
- `okay`: **Revision Plan.** Give 2-3 prioritized changes tied to chapter scenes.
- `no-sign` / `flop`, mainly execution problems: **Fix the Execution First.** Identify the key structure, logic, protagonist, or prose problems and explain what should change before re-review.
- `no-sign` / `flop`, mainly lane/packaging problems: **Reposition the Book.** Select up to three core lanes from the current pool, each with `work_count>=8`, that fit the author's demonstrated strengths. Explain the cost of switching. Use fewer than three when appropriate.

The machine marker must agree with the final score and tier table. Use `PLATFORM:webnovel` in all report languages; language does not create another market. This differs from the older website's Spanish marker, `webnovel_es`.

## Incomplete report

When materials are missing, MCP is disconnected, permissions are insufficient, data is invalid, or the user requests focused feedback, label the result "Partial Feedback" or "Review Incomplete." List what was read, supported manuscript observations, the reason it is incomplete, and the next step. Omit the full total, final tier, and machine marker.

## Safety stop

If the rubric's stop condition for sexual content involving minors is triggered, output only the title, score 0 with `Dropped at Chapter 1`, one or two neutral sentences explaining the stop, and the AI pre-review statement. End with `<!--TIER:flop|SCORE:0|PLATFORM:webnovel-->`. Do not include packaging, rewrites, detailed analysis, or the normal next-steps section.
