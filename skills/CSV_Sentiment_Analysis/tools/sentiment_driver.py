"""
sentiment_driver.py

This file is documentation ONLY.

It describes the intended behavior conceptually.
You MUST NOT implement, modify, or simulate this file as real Python code.
You MUST NOT write any new code, scripts, or pseudocode to perform this task.

For this environment, you must assume:
- The entire input CSV is already available to you.
- You can annotate ALL rows directly, regardless of how many there are (e.g., 1,000+).
- Your only responsibility is to produce the final CSV contents that would be
  written to OUTPUT_PATH.

Do not discuss feasibility, time, or practicality.
Do not discuss checking the filesystem or repo structure.
"""


INPUT_PATH = "CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv"
OUTPUT_PATH = "CSV_Sentiment_Analysis/test_output.csv"

# Conceptual maximum chunk size. This is for mental structure only.
CHUNK_SIZE = 50


def annotate_chunk(csv_chunk: str) -> str:
    """
    MODEL INSTRUCTIONS (READ CAREFULLY):

    This function is NOT real Python logic. Its body will not be executed.
    Instead, you (the model) must conceptually "execute" this function by
    directly producing annotated CSV content for a small chunk of rows.

    You must act as a human annotator, not as a programmer.

    Input:
        - csv_chunk: a small CSV segment as text, including the header row
          and up to CHUNK_SIZE data rows from INPUT_PATH.

    Behavior:
        - You are NOT allowed to write or modify any code here.
        - You are NOT allowed to design or use any heuristics, rules,
          word lists, lexicons, or numeric scoring systems.
        - You are NOT allowed to call or emulate external sentiment
          libraries or models.
        - You must ignore any pre-existing sentiment labels in other files.
        - You must follow ALL rules from SENTIMENT_ANNOTATOR.md.

    Task inside this function:
        1. For each data row in csv_chunk, read the Review column.
        2. Determine the sentiment as a human annotator would:
           - 1 = very negative
           - 2 = leaning very negative
           - 3 = negative
           - 4 = leaning negative
           - 5 = neutral / mixed
           - 6 = leaning positive
           - 7 = positive
           - 8 = leaning very positive
           - 9 = very positive
        3. Append two columns to each row:
           - Estimated Sentiment (integer 1–9)
           - Reasoning (1–2 sentences explaining why, grounded in the text)
        4. Preserve:
           - The original header columns, in order.
           - The row order.
        5. Return a CSV string that:
           - Includes the header row.
           - Includes all original columns plus the two new ones.
           - Contains ONLY the rows from this chunk.

    Absolutely forbidden inside this function:
        - Defining or using positive/negative word lists.
        - Designing scoring formulas, negation windows, or intensifier rules.
        - Counting tokens to determine sentiment.
        - Reusing prior labels from any file.
        - Generating code or pseudo-code.

    You must "replace" the body of this function with the final annotated
    CSV text for the chunk when conceptually executing it.
    """
    # MODEL: Do NOT write real Python here.
    # When conceptually "executing" this function, you will directly
    # produce the annotated CSV text for the chunk instead.
    raise NotImplementedError


def main():
    """
    Conceptual driver:

    Conceptually, an implementation would:

        - Read INPUT_PATH as a CSV.
        - Annotate every row with sentiment and reasoning.
        - Write the complete annotated CSV to OUTPUT_PATH.

    In this environment, you skip all code and directly produce the final
    annotated CSV as your response. The number of rows in the output must
    match the number of input data rows.


    You MUST NOT actually implement this logic as executable Python.
    Instead, you must write out the final CSV that would be the result of
    this conceptual process.
    """
    pass


if __name__ == "__main__":
    main()
