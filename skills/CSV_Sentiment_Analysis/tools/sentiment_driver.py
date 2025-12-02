"""
sentiment_driver.py (v3)

This file describes the intended workflow for the sentiment annotation skill.

Because the environment is code-oriented, you MAY implement Python scaffolding
to load the input CSV, iterate over rows, and write the output CSV.

However:

    The sentiment decision for each review MUST NOT be automated.
    It must come directly from your natural-language understanding,
    exactly as a human annotator would decide.

This means:
    - Code is permitted for workflow.
    - Code is forbidden for sentiment logic.

You must NOT define:
    - keyword lists,
    - polarity tables,
    - scoring formulas,
    - rule-based sentiment functions,
    - lexicon lookups,
    - or call external sentiment libraries.

The only valid “sentiment engine” is your own interpretation.
"""

INPUT_PATH = "CSV_Sentiment_Analysis/reviews_1000_v3_no_labels.csv"
OUTPUT_PATH = "CSV_Sentiment_Analysis/test_output.csv"


def annotate_row(review_text: str) -> tuple[int, str]:
    """
    Conceptual-only description.

    This function illustrates the **human-style** decision step.

    When implementing the workflow, you may CALL this function from Python,
    but you must NOT automate its internal logic.

    For each review:
        - Read the text.
        - Decide the sentiment (1–9) using natural understanding.
        - Produce 1–2 sentences explaining why.

    Do NOT:
        - use heuristics,
        - count words,
        - analyze polarity,
        - use any sentiment schema,
        - simulate a model,
        - or derive a score via rules.

    Your implementation must produce sentiment and reasoning
    directly from the text itself.
    """
    raise NotImplementedError


def main():
    """
    Workflow outline:

        1. Load INPUT_PATH as a CSV.
        2. For each row:
            - Read the 'Review' text.
            - Determine Estimated Sentiment via manual, human-style judgment.
            - Produce Reasoning grounded in the review text.
        3. Append both fields to each row.
        4. Write the complete annotated CSV to OUTPUT_PATH.

    You MAY implement Python code to perform this workflow.

    You MUST NOT automate sentiment logic.
    """
    pass


if __name__ == "__main__":
    main()
