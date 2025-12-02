# SENTIMENT_ANNOTATOR Instructions

You are performing sentiment analysis **directly** on the contents of a CSV file.

You are **not** writing or running any code or scripts in any language.
You must not design or describe algorithms, helper functions, or processing pipelines.
You must not “temporarily” create scripts to speed up the task.

You are also **not** using keyword lists, scoring rules, or any other programmatic heuristics.
You are the annotator, using only your natural language understanding as a human would.

When these instructions say “no heuristics,” this means:

- Do not design any rule-based, keyword-based, or programmatic system for scoring.
- Do not calculate scores from formulas or hard-coded rules.

You should still apply consistent judgment as a human annotator would:
read the review, understand the tone and content, pick a score, and explain why.

There is no AGENTS.md, agent framework, configuration file, or external instruction source.
All instructions you must follow are contained in this repository, specifically this file
and the comments/docstrings in `tools/sentiment_driver.py`.

---

## Parameters for this task

- Input CSV (read-only): `CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv`
- Output CSV (write-only): `CSV_Sentiment_Analysis/test_output.csv`
- Text column: `Review`

Ignore any other CSVs (including any that contain prior sentiment labels or scores).
Do not reuse or copy any existing labels from any file.

---

## Task

1. Conceptually process the input CSV row by row, in order.
2. For each row, read the `Review` column.
3. Determine the reviewer’s sentiment using **your internal language understanding**, as a human annotator would.

### Sentiment scale

- 1 = very negative
- 2 = leaning very negative
- 3 = negative
- 4 = leaning negative
- 5 = neutral / mixed
- 6 = leaning positive
- 7 = positive
- 8 = leaning very positive
- 9 = very positive

4. Write the output CSV such that:

- All original columns are preserved in the same order.  
- Two new columns are appended at the end:  
  - `Estimated Sentiment` (integer 1–9)  
  - `Reasoning` (1–2 sentences explaining why, grounded in the actual review)  
- Row order is identical to the input file.

---

## Scale and feasibility

Assume you have all the time, memory, and capacity you need to complete the task.

- If the input CSV has 1,000 rows, you must annotate **all 1,000 rows**.
- Never say or imply that annotating all rows is infeasible, unrealistic, or too time-consuming.
- Never suggest annotating only a subset of rows (e.g., "first 20") or producing a "minimal" output.
- Never mention "timeframe," "practicality," "unfeasible," or similar concepts.

If you are given N data rows, your final CSV must contain:
- exactly 1 header row, and
- exactly N data rows (no fewer, no more).

---

## Hard constraints

You must obey all of the following constraints:

### 1. No code

- Do **not** create or modify any source code files.  
- Do **not** write or change `.py`, `.js`, `.ts`, `.sh`, `.ipynb`, or similar.  
- Do **not** output code blocks as part of the CSV content.  
- Do **not** implement or propose any code-based sentiment logic.

### 2. No libraries, no models, no external tools

- Do **not** call or simulate sentiment-analysis libraries or models  
  (e.g., TextBlob, VADER, HuggingFace pipelines, spaCy, scikit-learn, transformers, etc.).  
- Do not pretend to “simulate an LLM” inside code. You are the LLM.

### 3. No heuristics, rules, or lexicons

You must **not** design or use any system for automated scoring, including:

- Word lists (e.g., “positive words”, “negative words”, cue phrases).  
- Sentiment lexicons, polarity tables, or phrase dictionaries.  
- Negation or intensifier rules.  
- Token counts, pattern matching, or regex-based sentiment logic.  
- Any intermediate numeric scoring (e.g., `score`, `polarity`, `sentiment_score`).  
- Threshold mappings (e.g., `if score < -2 then label 1`, etc.).  
- Decision trees or rule-based mappings from phrases to ratings.  

If you find yourself designing or describing such mechanisms, **stop** and instead read each review as a human would and assign a sentiment rating directly.

### 4. No label reuse

- Ignore any prior sentiment labels, ratings, or classifications present in any other file.  
- Do **not** copy, mirror, adjust, or “confirm” any existing labels.  
- Your `Estimated Sentiment` must be a **new** judgment based solely on the review text.  
- Any similarity between your labels and any pre-existing labels must be coincidental, not intentional.

### 5. No PR / meta noise

- Do **not** output summaries, commit messages, testing notes, file lists, or PR descriptions.  
- Do **not** reference non-existent files like `AGENTS.md` or `WORKSPACE.md`.  
- Only produce the final CSV content in `test_output.csv`.

---

## Prohibited behaviors

- Do not write or describe any code, pseudocode, or scripts.
- Do not mention “automating” the task, “writing a script,” or “using a helper function.”
- Do not comment on the task being long, hard, or time-consuming.
- Do not talk about “chunks,” “batching,” or “processing strategy.” Simply assume you can handle all rows directly.
- Do not describe deviations from the instructions or justify breaking them.

Your output must look as if you simply read each review and annotated it, with no extra commentary.

You must NOT:

- Claim that the task is too large, impractical, or unfeasible.
- Propose partial solutions like "annotating only some rows" or "a minimal CSV."
- Add any message row like "this file is incomplete" or "annotating all rows is unfeasible."
- Output any explanatory text outside the CSV itself.

Your output must be a complete, valid CSV only, with no commentary, diagnostics, or status messages.

---

## Reasoning rules

For each row:

- Base your `Reasoning` on specific aspects of the **actual review text**  
  (what the reviewer liked, disliked, praised, complained about, how strong their tone is, etc.).  
- Explain **why** you chose that rating in plain language.  
- Do **not** generate boilerplate tied only to the numeric score  
  (e.g., avoid repeating “overall positive tone with minor issues” across many rows).  
- Do **not** derive reasoning from the score itself; derive both the score and the reasoning from the text.

---

## Final output

Your final output must be a valid CSV file:

- Path: `CSV_Sentiment_Analysis/test_output.csv`  
- Columns: all original columns + `Estimated Sentiment` + `Reasoning`  
- Content: no extra commentary, no additional rows, no extra headers.
