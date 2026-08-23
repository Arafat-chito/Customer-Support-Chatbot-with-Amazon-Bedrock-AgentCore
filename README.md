# AI Customer Support & Bug Reporting Agent

## Overview
This project implements an AI customer support agent integrated with AWS services. The agent automatically processes user inquiries, handles shipping FAQ requests, identifies out-of-scope interactions, and dynamically logs technical bug reports directly into an AWS DynamoDB table.

---

## Project Structure

* **`system_prompt.txt`**: Defines system behavior, tool invocation rules, and scope boundaries. (##Went with direct system prompt, instead of Flows)
* **`agentcore_config.json`**: Agent configuration and tool definitions.
* **`flow-tests.json`**: Test cases covering bug reporting, FAQ lookup, and out-of-scope queries.
* **`seed_db.py`**: Utility script to seed the DynamoDB table (`BugReports-9e3628b0`) with initial ticket data.
* **`run_eval.py`**: Executes evaluation dataset generation across test scenarios.
* **`eval_dataset.jsonl`**: Output dataset containing test prompts and reference responses for model evaluation.
* **`chat.py`**: Command-line interface for multi-turn testing.

---

## Workflow & Implementation

### 1. Database Seeding & Verification
- **Execution**: Ran `seed_db.py` to write bug report items to the DynamoDB table `BugReports-9e3628b0`.
- **Validation**: Verified data persistence by performing a scan on the DynamoDB console, confirming successful creation of ticket `BUG-05238d68` with all required attributes (`ticketId`, `description`, `environment`, and `stepsToReproduce`).

### 2. Multi-Turn Interactive Testing
- Tested conversation flows via `chat.py` to ensure smooth tool switching, context retention across turns, and fallback mechanisms for out-of-scope queries.

### 3. Dataset Evaluation Pipeline
- Updated `flow-tests.json` with structured test inputs and input node parameters.
- Executed `run_eval.py` to generate `eval_dataset.jsonl` containing structured evaluations for:
  - **Bug Reporting:** Verifying correct extraction of environment and steps before DynamoDB insertion.
  - **Shipping FAQ:** Direct context-based resolution.
  - **Out-of-Scope:** Routing non-support queries to human customer support channels.

---

## Evaluation Observations

* **Tool Calling Accuracy:** The agent consistently triggered `create_bug_report` when presented with technical crash details while remaining within safety guardrails for out-of-scope prompts.
* **Data Consistency:** DynamoDB scans confirmed 100% attribute alignment between extracted prompt entities and stored record keys.
* **Flow Execution:** Successfully generated all 3 test lines into `eval_dataset.jsonl` without node validation errors.

---

## Submission Artifacts

1. **DynamoDB Scan Screenshot:** Demonstrating persisted item `BUG-05238d68`.
2. **Terminal Chat Screenshot:** Interactive multi-turn log (`chat.py`).
3. **Evaluation Screenshot:** `eval_dataset.jsonl` output generation.
