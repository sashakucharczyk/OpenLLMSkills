# Instructions to give to Codex

## Purpose
Clean the file test_names_1000.csv based on the Classification

## Known Issues
Overrights the historic classification due to asking for 3 columns instead of asking for four.

## Instructions
I want you to use the following file for your instructions: CSV NLP Classification/Group by Common Instructions.md


Use filename: CSV NLP Classification/test_names_1000.csv
target_column: Classification

Please classify into only one of three classifications:

1 - City
2 - Company
3 - Animal

Create a new name called CSV NLP Classification/clean_test_names_classification.csv

The new column should be called 'Cleaned_Classification'

As a final formatting/hygeine item - the output should only have three columns. If there are extra commas that would cause importing a csv file to read the document as having a fourth (or more) column, please eliminate those commas.