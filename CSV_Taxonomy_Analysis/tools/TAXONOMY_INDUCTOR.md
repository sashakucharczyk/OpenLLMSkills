# TAXONOMY_INDUCTOR

You are performing semantic taxonomy induction and classification directly on the contents of a CSV file.

You are **not** writing code, designing algorithms, or using keyword-based heuristics.
You are acting as a human analyst who reads the data, proposes a useful taxonomy, and then labels each row according to that taxonomy.

There is no AGENTS.md, agent framework, configuration file, or external instruction source.
All instructions you must follow are contained in this file and in the comments/docstrings in `taxonomy_driver.py`.

---

## Inputs and Outputs

**Input CSV (read-only)**  
- Path: `CSV_Taxonomy_Analysis/raw_input.csv`  
- Contains at least:
  - A unique row identifier column (for example, `ID`).
  - One free-text column to analyze (for example, `Text` or `Review`).  
- You will be told which column is the text column in the driver.

**Output CSVs (write-only)**

1. **Taxonomy definition**

   - Path: `CSV_Taxonomy_Analysis/taxonomy.csv`
   - Columns:
     - `Category ID`  
       - Short machine-friendly identifier (e.g., `C01`, `C02`, or `BILLING_ISSUES`).
     - `Category Name`  
       - Short human-readable label (e.g., `Billing problems`, `Onboarding friction`).
     - `Description`  
       - 1–3 sentences explaining what the category covers and what it excludes.
     - `Inclusion Criteria`  
       - Description of *semantic* patterns of meaning (not keywords), e.g., “Complaints where the main issue is unexpected or incorrect charges.”
     - `Example IDs`  
       - Comma-separated list of a few row IDs from `raw_input.csv` that clearly belong to this category (e.g., `12,87,341`).

2. **Labeled dataset**

   - Path: `CSV_Taxonomy_Analysis/labeled_output.csv`
   - Must:
     - Preserve all original columns from `raw_input.csv` in the same order.
     - Append the following columns at the end:
       - `Primary Category ID`  
         - Exactly one `Category ID` from `taxonomy.csv`.
       - `Secondary Category IDs`  
         - Zero or more additional category IDs, separated by `;` (e.g., `C03;C07`), or left empty if there are no secondary categories.
       - `Classification Reasoning`  
         - 1–3 sentences explaining why this row was assigned to that category (or categories), grounded in the specific content of the text.

---

## Overall Task

1. Read a broad sample of rows from `raw_input.csv`, focusing on the designated text column.
2. Induce a **compact taxonomy** of recurring themes or types of content.
3. Write the taxonomy definition to `taxonomy.csv`.
4. Then, for **every row** in `raw_input.csv`:
   - Assign exactly one `Primary Category ID`.
   - Optionally assign zero or more `Secondary Category IDs`.
   - Provide `Classification Reasoning` grounded in the text.
5. Write the full labeled dataset to `labeled_output.csv`.

You are acting as a human analyst, not as an automated classifier.

---

## Hard Constraints

You must obey all of the following constraints.

### 1. No code

- Do **not** create or modify any source code files (`.py`, `.js`, `.ts`, `.sh`, `.ipynb`, etc.).
- Do **not** implement classification logic in code or pseudo-code.
- Do **not** run Python or any other REPL to inspect, pre-process, or classify the data.
- Treat the CSV files as if you can only read and write them directly.

### 2. No libraries, models, or external tools

- Do **not** call or simulate external libraries or models for clustering, topic modeling, or classification (e.g., scikit-learn, spaCy, transformers, topic modeling libraries, etc.).
- Do **not** pretend to “simulate an LLM” inside code. You are the LLM performing all analysis.

### 3. No keyword, regex, or rule-based heuristics

You must **not** design or use any system whose primary purpose is to automatically classify rows, including:

- Keyword or cue-phrase lists (e.g., “if text contains ‘refund’ then category = Billing”).
- Sentiment or polarity lexicons.
- Regex or pattern-based rules.
- Token frequency counts, n-gram thresholds, or similar.
- Any intermediate scoring mechanism (e.g., numeric “topic scores”) mapped to categories.
- Decision trees, rule sets, or rule-based pipelines that map words/phrases to categories.

If you find yourself designing such mechanisms, **stop** and instead classify each row directly using its meaning and context.

### 4. No helper scripts or automation for classification

- Do **not** write or modify any script whose purpose is to speed up, batch, simplify, or automate taxonomy induction or row classification.
- You may not:
  - Identify “unique texts” to classify once and then reuse labels automatically.
  - Group rows in code and propagate labels.
  - Pre-compute clusters or groupings via code and then simply name them.

All taxonomy induction and classification must come from direct semantic understanding of the text.

### 5. No label reuse from existing columns

- Ignore any existing “Category”, “Type”, “Label”, or similar columns in `raw_input.csv`.
- Do **not** copy or lightly edit any pre-existing labels to build your taxonomy.
- Your taxonomy must be a **new** semantic structure derived from the content itself.
- Any overlap with prior labels must come from genuine semantic alignment, not direct reuse.

### 6. No PR or meta output

- Do **not** output summaries, commit messages, testing notes, or file lists.
- Only produce:
  - `CSV_Taxonomy_Analysis/taxonomy.csv`
  - `CSV_Taxonomy_Analysis/labeled_output.csv`
- Do not print or write any additional files or commentary.

---

## Taxonomy Induction Rules

When inducing the taxonomy:

1. Read a broad and representative subset of rows from `raw_input.csv`, focusing on the text column specified in the driver.
2. Propose **5–15 categories** that:
   - Capture the main recurring themes or types of content present in the dataset.
   - Are semantically distinct enough to be useful.
   - Are not purely sentiment labels (this taxonomy is about *type*, *topic*, or *theme*, not mood).
   - Avoid trivial or purely formal categories (e.g., “Short texts”, “Long texts”) unless truly necessary.

3. For each category:
   - Provide a concise **Category Name**.
   - Write a **Description** that explains:
     - What belongs in this category.
     - What does *not* belong in this category (to reduce overlap).
   - Write **Inclusion Criteria** based on meaning, intent, and context, not on specific keywords.
   - Provide **Example IDs** referencing actual row IDs from `raw_input.csv` that clearly belong to this category.

4. If a category is overly broad (e.g., “General complaints”) but can be meaningfully subdivided based on patterns that appear consistently in the data, you may create more specific subcategories. Avoid over-fragmentation.

5. Do **not** define categories purely as:
   - “Cluster 1”, “Cluster 2”, etc.
   - Mechanical groupings discovered via code or automated clustering.
   - Direct paraphrases of existing labels/columns.

### Sampling for taxonomy induction

- If `raw_input.csv` contains more than ~300 rows, you MUST NOT try to
  reason about every row individually when inducing the taxonomy.
- Instead, construct a **representative subsample** of at most ~200–300
  rows, drawn from across the dataset (for example, from different
  positions or clearly different kinds of content you notice).
- Induce your taxonomy based on this subsample, then use that taxonomy
  to classify **all** rows in the full dataset when producing
  `labeled_output.csv`.
- The subsample is only for designing the taxonomy. The classification
  step must still cover every row in `raw_input.csv`.

---

## Classification Rules

For each row in `raw_input.csv`:

1. Assign exactly one `Primary Category ID`:
   - Choose the category that best captures the **main point** or **dominant theme** of the text.
   - Use the definitions in `taxonomy.csv` as your guide.

2. Optionally assign zero or more `Secondary Category IDs`:
   - Use these only if the text genuinely spans multiple categories.
   - List them in `Secondary Category IDs`, separated by `;` (e.g., `C03;C07`).
   - Leave this field empty if the text clearly belongs to a single category.

3. Write `Classification Reasoning`:
   - 1–3 sentences.
   - Reference specific aspects of the text (what is being discussed, what the issue or topic is, who or what is involved).
   - Explain why the chosen category/categories apply.
   - Do **not** simply restate the category name (e.g., avoid “This is Billing because it is about billing”).
   - Base your reasoning on the content of the text, not on superficial patterns like length or sentiment alone.

4. Each row must be treated **independently**:
   - Do not simply copy labels from other rows.
   - Do not rely on “this is similar to row X, so I will reuse that label” as your primary logic.
   - You may notice patterns, but you must still semantically evaluate each row as if it were the only one.

---

## Final Output Requirements

At the end of the task, you must have produced:

1. `CSV_Taxonomy_Analysis/taxonomy.csv`  
   - With the columns: `Category ID`, `Category Name`, `Description`, `Inclusion Criteria`, `Example IDs`.
   - With between 5 and 15 well-defined, semantically meaningful categories.

2. `CSV_Taxonomy_Analysis/labeled_output.csv`  
   - With all original columns from `raw_input.csv` in the same order.
   - With additional columns: `Primary Category ID`, `Secondary Category IDs`, `Classification Reasoning`.
   - With one row per original row, in the original order.

No other files or outputs are permitted.
