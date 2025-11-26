# Task: Normalize similar names in a CSV column

## Variable Inputs (provided at runtime)

- **FILENAME:** `{{FILENAME}}`
- **TARGET_COLUMN:** `{{COLUMN}}`

Codex Web will receive these values separately from the file itself. Treat them as authoritative.

---

## Objective

Analyze the CSV file specified by **FILENAME**.  
Within the column **TARGET_COLUMN**, identify all entries that refer to the same underlying name even when they differ due to:

- Typos or misspellings  
- Missing/extra punctuation  
- Spacing inconsistencies  
- Capitalization differences  
- Minor abbreviation differences (e.g., “Co.” vs “Company”)  

For each row, assign a **canonical/common name** in a new column named:

- **`{{COLUMN}}_Normalized`**

Do not modify the original column.

---

## Requirements

### 1. Process the entire file
- Read every row.
- Evaluate every value in **TARGET_COLUMN** individually.
- Produce a **`{{COLUMN}}_Normalized`** value for every row.

### 2. Identify similar names without keyword matching
You must **not** rely on:
- Predefined keyword lists,
- Hard-coded mapping tables,
- “If value contains X then …” rules,
- Exact substring matching heuristics.

Instead, use robust similarity techniques such as:
- Case normalization,
- Whitespace normalization,
- Punctuation stripping/standardization,
- Edit-distance or fuzzy similarity scoring,
- Clustering based on similarity across the whole dataset.

The decision to cluster names must come from **string similarity**, not lexical keyword presence.

### 3. Group (cluster) equivalent names
Entries that clearly represent the same entity must be placed in the same similarity cluster, even if:

- Spellings differ  
- Punctuation differs  
- Abbreviations differ  
- Formatting differs  

Examples of values that should cluster together:  
`Acme Corp`, `Acme Corporation`, `ACME CORP.`, `Acme corp`, `A.C.M.E Corp`

### 4. Determine a canonical/common name for each group
For each similarity cluster, select one canonical representation by applying this hierarchy:

1. Prefer the most complete / descriptive version (e.g., `Acme Corporation` rather than `Acme`).  
2. Prefer the variant with the clearest spelling.  
3. If tied, choose the most frequently occurring variant in the dataset.  
4. If still tied, choose the lexicographically earliest version.

Assign this canonical value to **every row** in **`{{COLUMN}}_Normalized`**.

### 5. Output behavior
- Keep all original data.  
- Add a new column: **`{{COLUMN}}_Normalized`**.  
- Write the canonical name for each row.  
- Ensure the output is deterministic: identical input yields identical normalized output.

---

## Implementation Guidance (non-binding but recommended)

1. **Preprocessing**
   - Lowercase
   - Trim/standardize spacing
   - Remove or normalize punctuation
   - Optional: expand common abbreviations only when confidently deducible from similarity context

2. **Similarity Computation**
   - Compute similarity scores across all unique values in **TARGET_COLUMN**
   - Build clusters using a similarity threshold that reasonably groups clear variants
   - Do not over-collapse unrelated names

3. **Canonical Selection**
   - Inspect original variants in each cluster (not just the normalized ones)
   - Apply the canonical-selection rules above

4. **Write Output**
   - Preserve CSV structure and row order
   - Add the final **`{{COLUMN}}_Normalized`** column

---

## Acceptance Criteria
A run is successful when:

- Every row receives a value in **`{{COLUMN}}_Normalized`**  
- Obvious variants cluster together and share the same canonical name  
- No keyword-based decisions were used  
- The output is stable and reproducible  

