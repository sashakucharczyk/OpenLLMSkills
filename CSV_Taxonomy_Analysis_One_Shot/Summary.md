## 0. Preface ##
Trying to get the Taxonomy to work in a single shot.

## 1. Goal: ##
Given a CSV with a free-text column, the model should:

1. **Induce a small taxonomy of categories** based on the content of that column.
2. **Describe each category** clearly (what belongs, what doesn’t).
3. **Assign one or more categories** to each row, with short reasoning grounded in the text.

Think: human analyst reading a big dataset, inventing buckets, then tagging every row.

---

## 2. Output spec

Two outputs:

### **Output A: Taxonomy definition**

Separate file, e.g.:

* `CSV_Taxonomy_Analysis/taxonomy.csv`
  or
* `CSV_Taxonomy_Analysis/taxonomy.md`

Pick one. CSV is easier for tooling; Markdown is nicer for eyeballs. Assuming CSV for this document.

**`taxonomy.csv` columns:**

1. `Category ID`

   * Short machine-friendly identifier, e.g. `C01`, `C02`, or `ONBOARDING_ISSUES`.
2. `Category Name`

   * Human-readable label, short, e.g. “Billing problems”, “Positive product feedback”.
3. `Description`

   * 1–3 sentences explaining what this category covers and *what it excludes*.
4. `Inclusion Criteria`

   * Bullet-style or sentence-level description of patterns of meaning, not keywords. E.g. “Complaints where the main issue is being overcharged or charged unexpectedly, regardless of exact wording.”
5. `Example IDs`

   * Comma-separated list of a few row IDs from the main CSV that clearly belong here (e.g. `12,87,341`).

**Cardinality / size constraints:**

* Aim for **5–15 categories** total.
* Avoid “other/misc” unless absolutely necessary; if used, define it clearly.

---

### **Output B: Labeled dataset**

Same pattern as the sentiment annotator:

* Input: original CSV, e.g. `CSV_Taxonomy_Analysis/raw_input.csv`
* Output: `CSV_Taxonomy_Analysis/labeled_output.csv`

**`labeled_output.csv` should:**

* Preserve **all original columns** and order.
* Append at the end:

  1. `Primary Category ID`

     * Exactly one `Category ID` from `taxonomy.csv`.
  2. `Secondary Category IDs`

     * Zero or more category IDs (`C03;C07` style or comma-separated).
     * Can be empty if only one category fits.
  3. `Classification Reasoning`

     * 1–3 sentences explaining **why** this row was assigned to those categories, referencing the actual text.

**Rules:**

* Every row **must** have exactly one `Primary Category ID`.
* Secondary categories are optional but allowed if the text genuinely spans multiple themes.
* Reasoning must mention content, intention, or context, not just label paraphrasing.

---

## 3. Constraints to avoid heuristics / cheap shortcuts

Here’s the “don’t be a lazy classifier” section - try to force the LLM from "cheating"

Want to explicitly block:

* keyword lists as classification logic
* regex/pattern triggers
* “if text contains X → category Y” pipelines
* clustering by identical phrases
* blindly reusing column names as labels

Use language like this in `TAXONOMY_INDUCTOR.md`:

### **Hard constraints**

1. **No code-based classification**

* Do **not** create or modify any source code files (`.py`, `.js`, `.ts`, etc.).
* Do **not** implement classification logic in code, pseudo-code, or REPL.
* Do **not** run scripts to “help” group or assign categories.

2. **No keyword / regex heuristics**

* Do **not** design or use rules such as:

  * “If the text contains ‘refund’, label as Billing.”
  * “If sentiment words are negative, label as Complaint.”
* Do **not** create positive/negative term lists, cue phrases, or n-gram triggers.
* Do **not** rely on regex, token frequency, or simple patterns as the primary way to assign categories.

3. **No automatic clustering / pattern bucket hacks**

* Do **not** group rows solely by textual similarity or identical phrasing.
* Do **not** infer categories by first clustering and then naming clusters.

  * You may mentally notice patterns, but **each category must be defined semantically**, not as “cluster 3”.
* Do **not** create categories that are just paraphrases of column names or field values.

4. **No label reuse from existing columns**

* Ignore any existing “category,” “type,” “label,” or similar columns in the input.
* Do **not** copy or mirror existing labels; you are defining a **new** taxonomy.
* Any similarity to prior labels must come from genuine semantic overlap, not reuse.

5. **No PR / meta-output**

* Do **not** output summaries, file lists, commit messages, or test notes.
* Only produce:

  * `taxonomy.csv`
  * `labeled_output.csv`
  * and nothing else.

---

## 4. Rules for **inducing** the taxonomy

The LLM should build categories in a sane, human way instead of hallucinating nonsense.

Therefore, need to include:

### **Taxonomy induction rules**

* Read a **broad sample** of rows (not just the first 20) before finalizing categories.

* Propose **5–15 categories** that:

  * capture the main recurring themes / types of content,
  * are mutually *distinct enough* to be useful,
  * are not just sentiment labels (this is about *type*, not *mood*),
  * avoid trivial categories like “Short reviews” / “Long reviews”.

* For each category:

  * Give it a clear, human-readable name.
  * Define what belongs and what does *not* belong.
  * Provide **at least 2 example row IDs** from the dataset that are clearly in-scope.

* Categories should be based on:

  * the **subject** (what the text is about),
  * the **type of issue/idea**,
  * the **role** or **context** (e.g. onboarding vs billing vs product usage),
    not on superficial token patterns.

* If a category is too broad (“general complaints”), split it into more specific subtypes only if they actually appear consistently in the data.

---

## 5. Rules for **classification** (per row)

This is the row-level analogue of the Anthropic-style reasoning rules.

Add:

### **Classification rules**

For each row:

* Assign exactly **one** `Primary Category ID` from `taxonomy.csv`.

  * Choose the category that best captures the *main point* or *dominant theme* of the text.
* Optionally assign **0–3** `Secondary Category IDs` if:

  * the text genuinely spans multiple categories, not just tangential mentions.
* Write `Classification Reasoning` that:

  * references specific ideas or phrases from the text,
  * explains why the chosen category/categories fit,
  * does **not** just restate the category name (“This belongs to Billing because it is about billing”).

Avoid:

* generic templates like “Overall, this review fits the [Category] category because it discusses that topic.”
* labeling based on **one keyword** when the overall meaning is different.
* using sentiment alone to pick categories (“negative → complaint category”) unless the category itself is about complaints.

---