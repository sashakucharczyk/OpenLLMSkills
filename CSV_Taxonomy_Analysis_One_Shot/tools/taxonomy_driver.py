"""
Driver scaffold for taxonomy induction and classification.

This file is NOT meant to be executed as real Python in this environment.
It exists to give structure to how the model should think about the task.

The actual taxonomy induction and row-level classification are performed manually
by the model, using natural language understanding and following the rules defined in:

    CSV_Taxonomy_Analysis/tools/TAXONOMY_INDUCTOR.md

No code-based taxonomy logic, clustering, or classification is allowed.
"""

INPUT_PATH = "CSV_Taxonomy_Analysis/raw_input.csv"
TAXONOMY_PATH = "CSV_Taxonomy_Analysis/taxonomy.csv"
LABELED_OUTPUT_PATH = "CSV_Taxonomy_Analysis/labeled_output.csv"

# Conceptual maximum chunk size for row-wise work. This is for mental structure only.
CHUNK_SIZE = 50


def induce_taxonomy(csv_sample: str) -> str:
    """
    MODEL INSTRUCTIONS (READ CAREFULLY):

    This function is NOT real Python logic. Its body will not be executed.
    Instead, you (the model) must conceptually "execute" this function by
    directly producing the contents of TAXONOMY_PATH as CSV text.

    Input:
        - csv_sample: a representative sample of rows from INPUT_PATH as CSV text,
          including the header row and **no more than ~200–300 data rows**,
          even if INPUT_PATH contains many more rows.

    Behavior:
        - You are NOT allowed to write or modify any code here.
        - You are NOT allowed to design or use keyword-based heuristics, rule-based
          classifiers, clustering algorithms, or helper scripts.
        - You must follow ALL rules from TAXONOMY_INDUCTOR.md under:
            - "Hard Constraints"
            - "Taxonomy Induction Rules"

    Task inside this function:
        1. Read the csv_sample, focusing on the designated text column (as specified
           in the surrounding instructions).
        2. Induce a compact taxonomy of recurring themes (5–15 categories).
        3. For each category, produce:
            - Category ID
            - Category Name
            - Description
            - Inclusion Criteria
            - Example IDs (row IDs from INPUT_PATH that clearly belong to this category)
        4. Return a CSV string representing the full taxonomy with the header:
               Category ID,Category Name,Description,Inclusion Criteria,Example IDs

    Absolutely forbidden inside this function:
        - Defining keyword or cue-phrase lists as classification logic.
        - Implementing clustering or automated grouping algorithms.
        - Using existing label columns as the basis for categories.
        - Generating code or pseudo-code.

    Notes:
        - For large datasets (more than ~300 rows), you MUST conceptually use a
          subsample for taxonomy induction rather than trying to reason about
          every row individually at this stage.
        - The taxonomy you induce from this sample will then be applied to the
          entire dataset during classification.


    You must "replace" the conceptual body of this function with the final taxonomy
    CSV content when mentally executing it.
    """
    raise NotImplementedError


def classify_chunk(csv_chunk: str, taxonomy_csv: str) -> str:
    """
    MODEL INSTRUCTIONS (READ CAREFULLY):

    This function is NOT real Python logic. Its body will not be executed.
    Instead, you (the model) must conceptually "execute" this function by
    directly producing annotated CSV content for a small chunk of rows.

    Input:
        - csv_chunk: a small CSV segment as text, including the header row and
          up to CHUNK_SIZE data rows from INPUT_PATH.
        - taxonomy_csv: the complete taxonomy definition as CSV text, exactly as
          written to TAXONOMY_PATH by induce_taxonomy().

    Behavior:
        - You are NOT allowed to write or modify any code here.
        - You are NOT allowed to design or use keyword-based heuristics, rule-based
          classifiers, clustering algorithms, or helper scripts.
        - You must follow ALL rules from TAXONOMY_INDUCTOR.md under:
            - "Hard Constraints"
            - "Classification Rules"

    Task inside this function:
        1. For each data row in csv_chunk, read the text column specified in the
           surrounding instructions (e.g., "Text" or "Review").
        2. Using taxonomy_csv as the reference, determine:
           - A single Primary Category ID for the row.
           - Zero or more Secondary Category IDs, if genuinely applicable.
        3. For each row, append:
           - Primary Category ID (exactly one)
           - Secondary Category IDs (semicolon-separated, or empty)
           - Classification Reasoning (1–3 sentences grounded in the text)
        4. Preserve:
           - The original header columns, in order.
           - The row order within this chunk.
        5. Return a CSV string that:
           - Includes the header row.
           - Includes all original columns plus the three new ones.
           - Contains ONLY the rows from this chunk.

    Absolutely forbidden inside this function:
        - Defining or using keyword lists or regexes to drive classification.
        - Implementing scoring formulas, token counts, or automated rules.
        - Grouping rows via code and reusing labels automatically.
        - Reusing any pre-existing labels from other columns as the classification result.
        - Generating code or pseudo-code.

    You must "replace" the conceptual body of this function with the final annotated
    CSV text for the chunk when mentally executing it.
    """
    raise NotImplementedError


def main():
    """
    Conceptual driver:

    If this were executable, it would:

        1. Read INPUT_PATH as a CSV.
        2. Extract a representative sample of rows and call:
               taxonomy_csv = induce_taxonomy(sample_csv_text)
        3. Write taxonomy_csv to TAXONOMY_PATH.
        4. Split all rows from INPUT_PATH into chunks of at most CHUNK_SIZE rows each.
        5. For each chunk:
               annotated_chunk = classify_chunk(chunk_csv_text, taxonomy_csv)
        6. Concatenate all annotated chunks (minus duplicate headers) in order.
        7. Write the combined result to LABELED_OUTPUT_PATH.

    In this environment, you (the model) must directly produce the final contents of
    TAXONOMY_PATH and LABELED_OUTPUT_PATH as if this process had been executed exactly
    according to TAXONOMY_INDUCTOR.md and the rules in induce_taxonomy() and
    classify_chunk().

    You MUST NOT actually implement this logic as executable Python.
    Instead, you must write out the final CSV files that would be the result of this
    conceptual process.

    No other files or outputs are allowed.
    """
    pass


if __name__ == "__main__":
    main()
