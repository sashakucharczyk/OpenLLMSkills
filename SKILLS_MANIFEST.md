---
# SKILLS_MANIFEST: This YAML block defines the available tools for the LLM agent.
# The agent or LLM should read this block first to determine which skill is appropriate.
skills:

  - name: "csv-sentiment-analysis"
    path: "skills/CSV_Sentiment_Analysis"
    description: >
      Analyzes an input CSV file containing text and assigns a structured, human-like
      sentiment score (1-5) and a grounded reasoning explanation for each row.
      Avoids rule-based/heuristic matching.
    inputs:
      - file: "raw_input.csv"
        type: "CSV"
        required_columns: ["review_text"]
    outputs:
      - file: "labeled_output.csv"
        type: "CSV"
        columns_added: ["sentiment_score", "reasoning_text"]
    driver: "sentiment_driver.py"

  - name: "csv-name-normalization"
    path: "skills/CSV_Name_Normalization"
    description: >
      Cleans and normalizes unstructured name entries (e.g., product names, user names)
      to canonical forms. Identifies spelling variants and near-duplicates.
    inputs:
      - file: "raw_input.csv"
        type: "CSV"
        required_columns: ["unstructured_name"]
    outputs:
      - file: "normalized_output.csv"
        type: "CSV"
        columns_added: ["canonical_name", "group_id"]
    driver: "normalization_driver.py"

  - name: "csv-taxonomy-induction"
    path: "skills/CSV_Taxonomy_Analysis"
    description: >
      Induces a hierarchical classification taxonomy from a sample of raw text data.
      Classifies all rows according to the induced taxonomy and provides the criteria
      for inclusion/exclusion in the classification system.
    inputs:
      - file: "raw_input.csv"
        type: "CSV"
        required_columns: ["data_sample"]
    outputs:
      - file: "taxonomy_output.csv"
        type: "CSV"
        columns_added: ["taxonomy_class", "classification_reason"]
    driver: "taxonomy_driver.py"
---
