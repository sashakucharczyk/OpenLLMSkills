# Instructions to give to Codex

## Purpose
Take a set of reviews and rank them on sentiment. Provide a reasoning. This analysis uses simple reviews.

## Known Issue
The reasoning seems to default to set string based on the scoring. The scoring looks to be related to a keyword analysis. The agent will be explicit about this only went forced (ex: sometimes creating python code to handle it).

## Instructions
 You are performing sentiment analysis directly on the contents of a CSV file, *not* implementing a rule-based or keyword-based sentiment engine.

 **Files**

 * Input (read-only): `CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv`
 * Output (write-only): `CSV_Sentiment_Analysis/simple_output.csv`

 **Task**

 1. Process the input CSV **row by row**, in order.
 2. For each row, read the value in the `"Review"` column.
 3. Infer the author’s sentiment using your general understanding of language and context, not explicit rules or word lists.

    * Sentiment scale:

      * 1 = very negative
      * 2 = negative
      * 3 = neutral / mixed
      * 4 = positive
      * 5 = very positive
 4. Produce an output CSV that:

    * Preserves all original columns and their order.
    * Appends **two new columns at the end**:

      * `"Estimated Sentiment"` (integer 1–5)
      * `"Reasoning"` (a short explanation of why you chose that rating, 1–2 sentences max).
    * Preserves row order exactly.

 **Hard constraints**

 * **Do NOT create any new source code files** (no `.py`, `.js`, etc.).
 * **Do NOT modify any existing source code files.**
 * **Do NOT output any summary, testing notes, file lists, or commentary.** Only produce the final `simple_output.csv` content.
 * **Do NOT implement or rely on any explicit sentiment or polarity lexicon.**

   * Do not define lists or sets of “positive words” or “negative words.”
   * Do not implement custom scoring rules, negate windows, or intensifier rules.
   * Do not design a heuristic algorithm for sentiment.
 * **Do NOT use keyword-based scoring or pattern matching.**

   * Do not base sentiment primarily on the presence/absence of specific tokens or regex matches.

 Instead:

 * For each review, read it as natural language and judge sentiment the way a human would.
 * Use your internal language understanding to assign the 1–5 score and write a brief natural-language reasoning.

 The final result must be a valid CSV with the original columns plus the two new columns, and nothing else.

 If you find yourself defining word lists, numerical scores, or rule-based logic to determine sentiment, stop and instead directly read each review and rate it using natural language understanding.

 ** Reasoning Rules **

 * Your reasoning for each review should be based on a contextual analysis of the review.
 * Your reasoning should tell a reader why your scored a review a specific way.
 * Your reasoning should NOT be directly based on the sentiment score you assign.


