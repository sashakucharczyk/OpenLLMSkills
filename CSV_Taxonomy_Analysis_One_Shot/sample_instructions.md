## Purpose ##

## Known Issues ##
Sampling too large of a subset for the taxonomy causes Codex to crash. Unsure about other CLIs. Works well when breaking into 2 steps (taxonomy creation and then classification using a subsample of less than 200 for class creation).

Reasoning output (explaination) looks to be generic. 
No use of secondary categories - may need to force.

## Instructions ##
You are being given two activities to do that should be completed in series. `Activity 1` needs to be completed first before you start `Activity 2`.

# `Activity 1` #
Use the instructions in `CSV_Taxonomy_Analysis_One_Shot/tools/taxonomy_driver.py` 
and `CSV_Taxonomy_Analysis_One_Shot/tools/TAXONOMY_INDUCTOR.md` to perform 
ONLY the taxonomy induction step for `raw_input.csv`.

You must:
1. Use a representative subsample of at most ~200 rows from `CSV_Taxonomy_Analysis_One_Shot/raw_input.csv`.
2. Induce a compact taxonomy (5–15 categories) following the rules in TAXONOMY_INDUCTOR.md.
3. Write the taxonomy definition to `CSV_Taxonomy_Analysis_One_Shot/taxonomy.csv`.

Do NOT classify any rows.
Do NOT create or modify any code files.
Do NOT create `labeled_output.csv`.
Do NOT output any summaries, PR notes, or test logs.

Only produce:
- `CSV_Taxonomy_Analysis_One_Shot/taxonomy.csv`

# `Activity 2` #
A taxonomy has already been induced and saved in:
`CSV_Taxonomy_Analysis_One_Shot/taxonomy.csv`

Do NOT modify `taxonomy.csv`.

Using the instructions in:
- `CSV_Taxonomy_Analysis_One_Shot/tools/taxonomy_driver.py`
- `CSV_Taxonomy_Analysis_One_Shot/tools/TAXONOMY_INDUCTOR.md`

classify ALL rows from `CSV_Taxonomy_Analysis_One_Shot/raw_input.csv` using the existing taxonomy.

You must:
1. Read `CSV_Taxonomy_Analysis_One_Shot/raw_input.csv`.
2. For each row, assign:
   - exactly one Primary Category ID from `taxonomy.csv`
   - zero or more Secondary Category IDs
   - Classification Reasoning that is **exactly 1 sentence**, grounded in the row’s text
3. Preserve all original columns and their order.
4. Append the three new columns at the end:
   - `Primary Category ID`
   - `Secondary Category IDs`
   - `Classification Reasoning`
5. Write the complete result to:
   `CSV_Taxonomy_Analysis_One_Shot/labeled_output.csv`

Hard rules:
- Do NOT create or modify any code files.
- Do NOT change `CSV_Taxonomy_Analysis_One_Shot/taxonomy.csv`.
- Do NOT output summaries, test logs, PR notes, or file lists.

Only produce:
- `CSV_Taxonomy_Analysis_One_Shot/labeled_output.csv`
