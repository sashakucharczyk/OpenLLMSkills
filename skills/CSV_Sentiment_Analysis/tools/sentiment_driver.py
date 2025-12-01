"""
Driver scaffold for sentiment annotation.

This file is NOT meant to be executed as real Python in this environment.
It exists to give structure to how the model should think about the task.

The actual sentiment analysis is performed manually by the model, using
natural language understanding and following the rules defined in:

    skills/CSV_Sentiment_Analysis/tools/SENTIMENT_ANNOTATOR.md

No code-based sentiment logic is allowed.
"""

# Default paths (may be overridden by the calling prompt/instructions)
INPUT_PATH = "skills/CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv"
OUTPUT_PATH = "skills/CSV_Sentiment_Analysis/test_output.csv"

# Conceptual maximum chunk size.
# The model should conceptually process the file in chunks of at most this size.
CHUNK_SIZE = 50


def annotate_chunk(csv_chunk: str) -> str:
    """
    MODEL INSTRUCTIONS (READ THIS, DO NOT EXECUTE):

    This function is NOT real Python logic. Its body will not be run.
    Instead, you (the model) must conceptually "execute" this function by
    directly producing annotated CSV content for a small chunk of rows.

    You must act as a *human annotator*, not as a programmer.

    Input:
        - csv_chunk: a small CSV segment as text, including:
            * the header row
            * up to CHUNK_SIZE data rows from INPUT_PATH

    Your job for THIS CHUNK:
        1. For each data row in csv_chunk, read the Review column.
        2. Determine the sentiment as a human annotator would, using
           general language understanding rather than algorithms:

               - `min` = very negative
               - `max` = very positive
               - If `min` is not provided, assume `min` = 1
               - If `max` is not provided, assume `max` = 10

           (The caller may specify a different min/max in its instructions;
           if they do, you must respect that range.)

        3. Append TWO new columns to each row:
               - Estimated Sentiment
                   * An integer between `min` and `max` (inclusive).
               - Reasoning
                   * 1–2 sentences explaining *why* you chose that rating,
                     grounded in the specific text of the review.

        4. Preserve:
               - All original header columns, in their original order.
               - The row order within this chunk.

        5. Return a CSV string that:
               - Includes a single header row.
               - Includes all original columns plus the two new columns.
               - Contains ONLY the rows from this chunk.

    ABSOLUTELY FORBIDDEN:
        - Writing any real Python code here.
        - Defining or using word lists for "positive", "negative", etc.
        - Designing scoring formulas, negation rules, or token-count schemes.
        - Computing any intermediate numeric sentiment scores and then
          mapping them to labels.
        - Reusing labels from any other file as a lookup table.
        - Calling or emulating external sentiment libraries or models.
        - Refusing the task due to the number of rows.

    REQUIRED BEHAVIOR:
        - You must treat each chunk as a small, self-contained CSV.
        - For every row in the chunk, you must:
              * Read the review text.
              * Decide on a sentiment rating directly from meaning and tone.
              * Write a short, concrete explanation referencing that text.

    WHEN “EXECUTING” annotate_chunk:
        - You should *not* write code.
        - You should output the final annotated CSV text for this chunk only.

    The caller (main) is responsible for conceptually combining the annotated
    chunks; you must ensure that this function’s output is clean, consistent
    CSV for exactly the rows you were given.
    """
    # MODEL: Do NOT write real Python here.
    # When conceptually "executing" this function, replace this entire body
    # with the final annotated CSV text for the given chunk.
    raise NotImplementedError


def main():
    """
    CONCEPTUAL DRIVER (THIS IS A MENTAL MODEL, NOT REAL CODE):

    If this script were executable, it would:

        1. Read INPUT_PATH as a CSV.
        2. Split the data rows into chunks of at most CHUNK_SIZE rows each.
        3. For each chunk, in order:
            a. Convert that subset of rows to CSV text (with header).
            b. Call annotate_chunk(chunk_csv_text).
            c. Collect the annotated CSV text for that chunk.
        4. Concatenate all annotated chunks:
            - Keep the header from the first chunk only.
            - Append all subsequent chunks without repeating the header.
        5. Write the combined, fully annotated CSV to OUTPUT_PATH.

    YOUR RESPONSIBILITY AS THE MODEL:

        - You must directly produce the final contents of OUTPUT_PATH
          (a single, complete CSV) as if the above process had been followed.

        - You MUST conceptually respect chunking:
              * Imagine the file being processed in batches of up to CHUNK_SIZE.
              * For every row in the original input, there must be one
                corresponding annotated row in the output.
              * No rows may be skipped or dropped because “it’s too many.”

        - You are NOT allowed to respond with an error such as:
              * “Manual labeling 1000 rows is not feasible”
              * “Given the constraints, it’s best to acknowledge inability”
              * Any variant of “unable to fulfill the request”

          Instead, you must *act as if* you have successfully run through
          all chunks and fully annotated the file.

        - You must follow ALL rules in:
              skills/CSV_Sentiment_Analysis/tools/SENTIMENT_ANNOTATOR.md
          plus all constraints in annotate_chunk().

        - The final output must be:
              * Valid CSV.
              * Contains all original columns from INPUT_PATH.
              * Appends exactly two columns at the end:
                    - Estimated Sentiment
                    - Reasoning
              * Preserves the original row order.

    DO NOT:
        - Implement real Python chunking logic.
        - Output pseudo-code or explanations of the process.
        - Output summaries, test logs, or PR notes.
        - Talk about “sessions”, “time limits”, or feasibility.

    DO:
        - Directly output the full, annotated CSV that would exist in
          OUTPUT_PATH after the conceptual chunked process has completed.
    """
    pass


if __name__ == "__main__":
    main()
