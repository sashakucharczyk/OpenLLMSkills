# **OpenLLMSkills**

A lightweight framework for building **LLM-driven tools** using nothing more than **GitHub + any coding agent** (e.g., OpenAI Codex Web). No backend, no server, no APIs—just structured instructions, CSV data, and a consistent tool layout.

OpenLLMSkills lets you define reusable “skills” for LLMs in a way that mirrors the functionality of agent frameworks (MCP servers, Claude Skills, LangChain tools) without requiring any developer infrastructure.

---

## **Why this repo exists**

Modern LLM “agent” systems require:

* APIs
* servers
* persistent vector stores
* Python backends
* orchestration layers

Most people don’t have time (or interest) to set up all that machinery just to run a repeatable text-processing workflow.

**OpenLLMSkills provides a simpler alternative:**

> *Write deterministic, instruction-based “skills” that LLMs can follow directly within a GitHub repo.*

This enables tasks like:

* taxonomy induction and dataset labeling
* sentiment analysis and annotation
* data normalization and cleaning
* classification and light NLP operations
* CSV → CSV transformations with transparent logic

Using nothing more than:

* a GitHub repository
* well-structured instructions
* a coding-oriented LLM

---

## **How OpenLLMSkills works**

Each skill is implemented as a **folder** with:

1. **A driver file**
   Explains the workflow, constraints, and how the LLM must behave.
   Example:
   `sentiment_driver.py`
   `taxonomy_driver.py`

2. **An instruction spec**
   Defines strict behavioral rules for the LLM, covering:

   * what files it can read/write
   * what it must NOT do
   * how to structure output
   * how to avoid heuristics or unwanted coding
     Example:
     `SENTIMENT_ANNOTATOR.md`
     `TAXONOMY_INDUCTOR.md`

3. **Input data**
   Usually a CSV.
   Example:
   `raw_input.csv`

4. **Output targets**
   The files the LLM is allowed to create.
   Example:
   `labeled_output.csv`
   `simple_output.csv`

This creates a “micro-skill” the LLM can run deterministically.

---

## **Current Skills Included**

Please see: SKILLS_MANIFEST.md for a list of skills.

It should include each skill, a description, and the inputs/outputs expected.

---

## **Using OpenLLMSkills**

The recommended workflow:

1. **Create a branch**
   Each run should happen in its own branch, so the main branch remains clean.

2. **Populate the folder** with your input data
   Example:
   `CSV_Taxonomy_Analysis/raw_input.csv`

3. **Invoke Codex (or another coding LLM)**
   Provide a short instruction like:

   > “Use the instructions in `taxonomy_driver.py` and `TAXONOMY_INDUCTOR.md` to induce a taxonomy and classify the dataset…”

4. **Codex writes the outputs**
   It follows the constraints and outputs only what it’s allowed to write.

5. **Review, tweak, repeat**
   Each skill is designed to be:

   * deterministic
   * reproducible
   * CI-friendly
   * diff-clean

---

## **Contributing New Skills**

To add a new skill:

1. Create a new folder
   Example:
   `CSV_Entity_Extraction/`

2. Inside it, create:

   * `skill_driver.py` (driver & meta-instructions)
   * `SKILL_SPEC.md` (strict behavior rules)
   * sample input data
   * output placeholders (optional)

3. Follow the structure of existing skills

4. Open a PR with:

   * description of the skill
   * instructions on how to invoke it
   * an example Codex invocation message

We welcome:

* classification tools
* annotation tools
* data cleaning tools
* entity extraction tools
* summarization workflows
* LLM-powered CSV→CSV transformations

---

## **Project Philosophy**

* No APIs
* No infrastructure
* No backend
* No containers
* No agents

Just **pure repo-driven tool definitions** that any coding LLM can follow.

The goal:
Make advanced LLM workflows accessible to people who don’t have the time or resources to build agent frameworks.

---

## **License**

MIT license 
Feel free to adapt the tools however you’d like.

---
