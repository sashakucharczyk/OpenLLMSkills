# CSV Clean Class - BEING UPDATED

## Overview
This skill normalizes noisy text labels in a CSV file. It resolves misspellings,
punctuation differences, inconsistent spacing, and variant forms of a label
into a canonical known form. The skill is useful for cleaning data sets where the
desired output is known, but the inputs have various permutations.

## Folder Contents
- `skills/CSV_NLP_Data_Cleaning/tools/CLASS_AND_NAME_NORMALIZER.md` – Specification and behavioral rules for the cleaning task.
- `clean_driver.py` – Driver instructions used by Codex to run the skill.
- `test_names_1000.csv` – Example input dataset.
- `clean_test_names_classification.csv` – Output produced by the skill (example).

## Input Format
The input CSV must contain at least:
- `ID`
- `Name` (or equivalent free-text field)
- `Classification` (which may be noisy)

The skill supports configurable column names via the invocation message.

## Output Format
The generated CSV will contain exactly:
1. All original columns preserved.
2. An appended column:
   - `Cleaned_Classification`

If extra commas exist due to malformed fields, they must be cleaned so the file
imports as a valid three-column CSV.

## How to Invoke the Skill
Example invocation via Codex:

* ensure you are in a branch/fork that you can add files to
* add your target input file to the directory
* use the instructions found in instructions.md (tested on Codex Web)
* update the instructions to point to your input file
* update the instructions to reflect any class/grouping changes you want
* provide the instructions to your agent/worker that is connected to GitHub

## Skill Logic Summary
The model interprets text labels using semantic understanding rather than
explicit rules. It standardizes the classification field by resolving
inconsistencies and mapping each entry to one of the canonical categories
supplied in the invocation context. Reasoning is internal; only the cleaned
column is written.

## Examples
Input:

ID,Name,Classification
42,Mettropolis,Compny
43,feta inc.,Comapny
44,Meta,company

Output:
ID,Name,Classification,Cleaned_Classification
42,Mettropolis,Company,Metropolis
43,feta inc.,Company,Meta
44,Meta,Company,Meta
