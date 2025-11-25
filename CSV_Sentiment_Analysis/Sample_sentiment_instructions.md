# Instructions to give to Codex

## Purpose
Take a set of reviews and rank them on sentiment. Provide a reasoning. This analysis uses simple reviews.

## Known Issue
File has labels which might create a problem.

## Instructions
You are performing sentiment analysis on each row of a CSV file.

Your **input file** is: `CSV_Sentiment_Analysis/reviews_1000_increased_random.csv` (read-only).
Your **output file** is: `CSV_Sentiment_Analysis/simple_output.csv` (write-only).

Your task:

1. Process the CSV **row by row** in order.
2. Read only the value in the column **"Review"**.
3. Infer the author’s sentiment using **overall meaning and tone**, not keyword matching or heuristics.

   * Sentiment scale: **1 = very negative**, **5 = very positive**.
4. Add two new columns to the output file:

   * **Estimated Sentiment** (integer 1 to 5)
   * **Reasoning** (short explanation of why you assigned that score)
5. Copy all original columns into the output file unchanged, and append the two new columns at the end.
6. Do not alter row order, field names, punctuation, or formatting.
7. The input file must remain unmodified.

Clarifications:

* “No keyword matching” means: evaluate the human meaning, tone, and context of the review. Do not assign sentiment based on the presence or absence of specific words alone.
* The output must remain valid CSV with no additional commentary, headers, or formatting beyond the two new columns.
