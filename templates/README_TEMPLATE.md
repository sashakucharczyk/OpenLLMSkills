Template for READMEs

### **`<SKILL_NAME>/README.md`**

# <Skill Name>

## Overview
Brief description of what this skill does.
Example:
“This skill performs joint normalization of entity names and noisy classification
labels (City, Company, Animal). It produces cleaned types and canonical names.”

## Folder Contents
Explain each file in the folder:
- `<skill>_driver.py` – meta-instructions for Codex
- `<skill>_SPEC.md` – strict behavioral rules
- `raw_input.csv` – example or working input
- `output_placeholder.csv` (optional)
- Any sample data

## Input Format
Describe the required columns in the input CSV.
Example:
- `ID`
- `Name`
- `Classification`

If the skill supports variable column names, describe how Codex is expected to
receive them (via invocation message).

## Output Format
Define the exact columns and order of the output CSV.

Example:
The skill produces a new CSV with these columns:
1. `ID`
2. `Name`
3. `Cleaned_Classification`
4. `Cleaned_Name`

Include notes about CSV hygiene if relevant.

## How to Invoke the Skill
Provide a ready-to-use instruction block.

Example:
```

Use the instructions in:

* <skill>_driver.py
* <skill>_SPEC.md
  …

```

## Hard Constraints
List the rules the worker must obey, including:
- no code creation
- no modifying other folders
- no PR summaries
- no heuristics or keyword-driven rules
- only write the one allowed CSV

## Skill Logic Summary
A human-readable explanation of how the skill works at a conceptual level.
One or two paragraphs max.

## Examples (optional)
Include 3–5 rows showing:
- raw inputs  
- expected cleaned classifications  
- expected cleaned names  

This massively stabilizes the worker’s behavior.





