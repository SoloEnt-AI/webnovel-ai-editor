# Scoring Rubric

Read this entire reference before a full review. Each dimension is scored from 0 to 100. Select a ladder baseline, check the permitted bonuses, then apply deductions, with manuscript evidence for every adjustment. Where ladder boundaries overlap, choose the band supported by the evidence; do not mechanically stack maximum adjustments. Use only the listed bonuses. Other demonstrated problems may justify deductions with an explanation. Deduct a fact in its most relevant dimension only, and do not deduct it again if it was already fully accounted for in the baseline.

## 1. Reader Model and Market Fit (25%)

This rubric follows SoloEnt's simulated WebNovel editor model: clear mobile reading, a proactive protagonist with a goal, visible progress, frequent payoffs, compelling chapter endings, and room for sustained serial escalation. Familiar tropes do not lose points by themselves. Boredom, confusion, and failed payoff delivery do. System and LitRPG are examples, not claims about current popularity; use the current tag pool to establish market strength.

The original rubric treats literary slow-burn without a progression hook, real-history settings, horror/mystery, sports other than football, and hard science fiction/space opera as demanding lanes. Use this as a prompt to scrutinize structure and setup, not as proof that these lanes are currently unpopular or as an automatic deduction. For a new author with average execution, reconsidering the lane may be appropriate.

### 1.1 Match tags

Use the title, synopsis, outline, and chapters to write a story summary and a one-line selling point. Distinguish:

- **Core lane tags:** Genre, central mechanism, or the book's main selling point, such as progression systems, cultivation, or business building.
- **Modifier tags:** Location, period, viewpoint, or cast traits. These cannot be the primary tag.

Select one primary core lane and at most two secondary tags. Match the whole book's main story strictly against the tag introduction, not one scene, a supporting character, or a future arc. User-supplied labels alone do not prove a match. A tag with null `writing_advice` or an empty introduction cannot count as a hit.

**Exact API field:** The introduction has a non-English JSON key. To keep these files in English without renaming the upstream schema, represent its path as `writing_advice["\u6807\u7b7e\u4ecb\u7ecd"]`. Decode those standard JSON Unicode escapes when locating the actual property. This is the existing tag-introduction field, not a new English `introduction` field. Internal tag names and definitions returned by MCP may also be non-English.

Valid data has top-level `site=webnovel_original`, `window=6m`, and a complete, nonempty `tags` array. Entries used must have a nonempty string `tag`, a nonnegative integer `work_count`, and a finite numeric `market_score`. Use returned market scores without reconstructing them. A score outside this rubric's 0-100 range indicates a data-contract mismatch: stop full scoring and report it rather than silently changing the value.

Display `tag_en` exactly as returned. When null, translate the internal name into natural English and label it "translated name." Paraphrase definitions in the report language; do not expose internal non-English field names in English reports. If another report language is requested, an explanatory translation may accompany the English tag name.

### 1.2 Primary-tag baseline

| Result | Baseline |
|---|---|
| Hit with `work_count >= 8` | Round `market_score` to the nearest integer |
| Hit with 3-7 works | Round `market_score`, then clamp to 20-75 |
| Hit with 1-2 works | Insufficient evidence; use the reader-appetite fallback |
| No valid primary-tag hit | Use the reader-appetite fallback |

`work_count=0` is not a sampled hit. A failed data request is not "no match."

**Trope-stack bonus:** If a secondary core lane is central to the book's hook, has at least 8 works, and its market score is at least 15 points above the baseline above, add 3-8 points. The result cannot exceed that secondary tag's market score. Award the combination once, not separately for each secondary tag. Modifier tags cannot trigger this bonus.

**Reader-appetite fallback:** Only for no valid match or a matched sample of 1-2 works:

- Strong progression loop, proactive protagonist, and payoff rhythm: 25-40.
- Partly serves that appetite: 10-25.
- Does not serve it: 0-10.

### 1.3 Content-risk adjustments

Assess severity across the manuscript. Do not apply the maximum deduction for a single minor moment.

| Risk | Market Fit deduction |
|---|---|
| Demeaning real religions, ethnicities, or nationalities, or extremist expression | 5-15 |
| Defamatory treatment of real-world politics or living public figures | 5-10 |
| Gore or torture far beyond genre conventions | 3-8 |
| Fan fiction of copyrighted IP submitted as an Original | 20, plus the cap in section 6 |

Adult sexual content itself is not a deduction. Judge whether it advances relationships, character, or plot; evaluate filler in the relevant execution dimension. A neutral reminder to check mature-content labels does not establish compliance with current platform policy. Sexual content involving minors triggers the stop condition in section 6.

## 2. Opening Hook (25%)

| Baseline | Evidence |
|---|---|
| 0-20 | World history, a waking routine, or a lore prologue dominates; no conflict by the end of chapter 1; a system story still lacks its core mechanism by chapter 3 |
| 20-45 | Conflict is late or generic; humiliation goes unanswered; the first payoff is after chapter 3 |
| 45-65 | Chapter 1 enters through an event with a clear situation and inciting incident; the mechanism appears in chapters 1-2, with a first payoff by chapter 3 and chapter-end pull |
| 65-80 | The first 500 words engage; each chapter ends with a pull; setup/payoff loops have begun, with concrete reasons to want chapter 4 |
| 80-100 | Exceptional tension and hook density across scenes, supported by substantial evidence |

Check roughly the first 500 English words or an equivalent opening length, payoff timing, the last lines of the three chapters, and the function of status windows. Do not require a system in a story without one; assess the core mechanism it actually promises.

| Problem | Deduction |
|---|---|
| Lore dumps or a history prologue crowd out the opening | 5-15 |
| Opening humiliation is unanswered within three chapters | 5-15 |
| Status blocks occupy about a fifth of a chapter or full sheets are repeatedly dumped | 5-10 |
| A cheat instantly removes the crisis without replacement tension | 5-10 |
| All three chapter endings are flat | 5-10 |
| Nonstop combat without breathing room, or aimless daily life without stakes | 5-15 |

There is no separate bonus for this dimension; strong execution belongs in the baseline.

## 3. Premise & Power System (20%)

| Baseline | Evidence |
|---|---|
| 0-30 | Unclear or contradictory mechanics, no payoff, or random genre mixing |
| 30-50 | Stock sign-in, points, or similar mechanics without a meaningful variation |
| 50-68 | A clear one-line pitch, a real twist on a familiar trope, and a logical payoff loop |
| 68-82 | A distinctive selling point; mechanics interact with adversity, deliver in the prose, and reveal the next tier |
| 82-100 | The premise itself has exceptional selling power with sound logic; rare and requires substantial evidence |

Can you explain what the protagonist gains, what they do, and what goal that serves in one line? Check escalation, limits, costs, and the internal logic of combinations. Without supernatural powers, assess the actual core commercial mechanism. If title and synopsis are supplied, check whether they communicate the hook; their absence loses no points.

**Check the bonus first:** Mechanics and adversity interact so that the protagonist must think, pay a cost, or exploit rules to profit, demonstrated in an actual scene: +5-10.

| Problem | Deduction |
|---|---|
| Generic cheat without a twist | 5-10 |
| Multiple currencies/subsystems and unclear early rules | 5-15 |
| Power removes every threat or meaningful cost | 10-20 |
| Unprepared genre mixing breaks setting or tone | 10-20 |

## 4. Protagonist & Plot Runway (15%)

| Baseline | Evidence |
|---|---|
| 0-30 | No clear desire or direction in the prose; the outline is also only setting notes |
| 30-50 | A goal exists but escalation ends with the first arc, making an early stall likely |
| 50-68 | Clear goals, progression tiers, arc opponents, and a proactive protagonist |
| 68-82 | Within three chapters, readers can explain what the protagonist wants and why they cannot stop; mysteries, ranks, maps, and opponents sustain a serial |
| 82-100 | Beyond a long-run engine, designed secrets and reversals make each arc serve the central drive; requires substantial evidence |

Prioritize execution in the chapters. The outline supports future runway; unconventional outline formatting does not erase a main plot already present in the prose. Check desire, urgency, competence, decisiveness, early memorable moments, antagonist motives, and the agency of relationship characters.

**Check the bonus first:** The protagonist turns mechanics, rules, or circumstances toward a personal goal through negotiation, rule use, or reversals: +3-8, with scene evidence. This may coexist with the previous dimension's bonus, but distinguish premise design from character action.

| Problem | Deduction |
|---|---|
| Events drive the protagonist, or tasks are completed without a personal goal | 5-20 |
| Doormat behavior, indecision, or repeatedly sparing opponents without a reason | 5-15 |
| Antagonists exist only to insult the protagonist and be humiliated | 5-10 |
| Harem characters are rewards without personality or relationship progress | 5-10 |
| The protagonist's goal drifts randomly | 5-15 |

Receiving system tasks does not automatically mean passivity. Aligning tasks with a personal goal, bargaining, or exploiting rules demonstrates agency.

## 5. Readability & Voice (15%)

| Baseline | Evidence |
|---|---|
| 0-25 | Meaning-blocking errors in most paragraphs, or chaotic tense/POV |
| 25-45 | Understandable but error-heavy, exposition-heavy, and stiff in dialogue |
| 45-65 | Clear prose, consistent tense/POV, mobile-friendly paragraphs, and character established through action |
| 65-82 | Distinctive narration, humor, dialogue, and vivid scenes; requires short quotation evidence |
| 82-100 | Distinctive voice plus emotionally powerful scenes and convincing characters; requires substantial evidence |

Evaluate grammar and dialogue punctuation in the actual manuscript language, viewpoint, paragraphs, showing versus explanation, and localization. Do not heavily punish occasional second-language slips. Clearly separated POV switches are acceptable. Cultivation idioms can fit an Eastern setting; judge whether they clash with a Western or modern setting. Criticize repetitive cadence or empty ornament as prose features, not proof of AI generation.

**Check the bonus first:** A memorable protagonist voice, natural humor, sharp banter, or a personal tone that holds under pressure: +5-12 when any one is supported by a short quotation.

| Problem | Deduction |
|---|---|
| Pervasive grammatical errors obstruct comprehension | 10-25, plus the final-score cap |
| Unmotivated tense changes or head-hopping within a scene | 5-15 |
| Repeated walls of text, such as English paragraphs over roughly 120 words | 5-10 |
| Explanation and internal monologue crowd out dramatic action | 5-15 |
| Empty ornament, repetitive cadence, or generic stock phrases | 5-15 |
| Voice, calques, or slang clash with the setting | 5-10 |

## 6. Calculation Order

Keep an internal calculation record. Show adopted scores and relevant adjustments in the report without exposing the weighting formula.

1. **Settle dimensions:** Apply the bonuses and deductions, clamp each dimension to 0-100, and round nonnegative values using `floor(x + 0.5)`, not banker's rounding.
2. **Niche compensation:** Trigger only if Market Fit is now **<35**. If Opening Hook, Premise & Power System, and Readability & Voice are all >=80, add 10-20 to Market Fit. Otherwise, if all three are >=70, add 5. Otherwise, no change. Do not punish a niche again. Clamp and round Market Fit to 0-100. Exactly 35 does not trigger compensation.
3. **Weighted base total:** `M*0.25 + H*0.25 + P*0.20 + C*0.15 + V*0.15`, where M, H, P, C, and V are the dimensions in order above. Keep decimals when testing the >=80 review threshold; round only before final tier assignment.
4. **High-score reassessment:** Required when the base total is >=80. Are the high scores supported by a distinctive hook, tension, and reasons to keep reading? A competent manuscript that merely avoids mistakes typically belongs around 65-75, but never force it into a band without evidence.
   - Supported high scores: Retain them and note the reassessment.
   - Inflated scores: Lower the unsupported dimension scores and recalculate from step 1, including compensation. Explain the corrections. The website's ambiguous instruction to subtract 8-12 from the total while also lowering dimensions is treated here as one correction: **do not subtract the same correction again after recalculating**. A fall to 65-78 is typical, not mandatory.
5. **Track-record adjustment:** No verifiable track record means no adjustment. Previous work is optional. Mark unsupported self-reported results as "unverified" and do not award points for them. Do not demand sensitive identity information. When checking user-provided public work links, read only the necessary public information and retain sources; do not expand the Insight tool scope.
   - Similar previous style but a demonstrably weaker new manuscript: A deduction of 3-5 is allowed with specific evidence of regression. **Do not also award a positive track-record bonus.**
   - Verified achievements and manuscript evidence of the corresponding execution: Select one band below; do not stack bands.
   - Switching lanes: Reduce the selected bonus and explain by how much; do not raise other dimensions.
   - Different style: Describe the textual differences and the limits of identity inference. Do not refuse the review, allege ghostwriting, or deduct for style differences alone. If the connection between a claimed track record and this submission genuinely cannot be established, omit the adjustment and continue evaluating this manuscript.
6. **Caps and verdict:** Add the track-record adjustment to the base total, clamp to 0-100, round, apply the red lines below, and map to a tier. If an adjustment brings the final score to >=80 from a base below 80, also verify the high-score evidence without applying adjustments twice.

| Verified track record | Adjustment |
|---|---|
| Ranking leader, major contest winner, or successful author with tens of millions of views | +15-20 |
| Contracted book with millions of views, or a long-running paid serial | +8-12 |
| At least one completed contracted book | +3-5 |
| Established Kindle Unlimited, RoyalRoad, or traditionally published author crossing into this lane | +3-8, with strict serial-pacing scrutiny |

These bands and adjustments are **simulated editorial rules**, not official WebNovel eligibility criteria. Do not infer income from view counts.

### Red lines

- **Sexual content involving minors or characters presented as minors:** Stop the normal review immediately without further detail processing. Output only the title, score 0 with `flop`, one or two neutral sentences explaining the stop, the AI pre-review statement, and the machine marker. Do not quote the content.
- **Fan fiction of copyrighted IP submitted as an Original:** Apply the 20-point Market Fit deduction above and cap the final total at 64. Explain the obstacle to this submission positioning without treating all work inspired by prior fiction as fan fiction.
- **Pervasive grammar errors obstruct comprehension:** Apply the Readability & Voice deduction and cap the final total at 64. Identify the readability obstacle in the current language version.

The latter two caps restrict the final verdict; they are not another duplicate deduction. When current platform policy or rights ownership needs factual verification, consult current official sources. Do not present the rubric as an independently verified legal conclusion.

### Tier mapping

| Final integer score | Tier | Fixed verdict | Meaning |
|---|---|---|---|
| 90-100 | `platinum` | Ranking Monster | Exceptional commercial potential |
| 80-89 | `speed` | Sign It, Ship It | Prepare for submission |
| 65-79 | `okay` | Readable, Not Memorable | Readable; needs distinction |
| 45-64 | `no-sign` | Not Contract-Ready | Below this rubric's contract-readiness standard |
| 0-44 | `flop` | Dropped at Chapter 1 | Serious opening or positioning problems |

These verdicts preserve the original product's editorial persona. They are not formal acceptance/rejection decisions or probabilities.
