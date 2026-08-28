# AWS Bedrock Customer Support Chatbot & Evaluation Pipeline

This repository contains the setup, flow invocation logic, and automated evaluation workflow for an AWS Bedrock agentic chatbot built for customer support operations.

---

## Technical Architecture Overview

The application routes incoming customer prompts through an AWS Bedrock Flow (`Online_Shop`) designed to evaluate queries, trigger function nodes, and return responses. 

* **Bedrock Flow ID:** `D3MYMJVDRZ`
* **Flow Alias ID:** `TSTALIASID` (working draft alias)
* **Input Node Name:** `FlowInputNode`
* **Evaluator Model:** `amazon.nova-pro-v1:0`

---

## File Structure

```text
├── flow-tests.json           # Input evaluation test cases and expected outputs
├── generate-eval-dataset.py # Script invoking Bedrock Flow and generating BYOI JSONL dataset
├── run_eval.py               # Wrapper script executing dataset generation pipeline
├── eval_dataset.jsonl        # Generated evaluation dataset formatted for Bedrock Model Evaluation
├── env.sh                    # Environment setup script for AWS credentials
└── README.md                 # Project documentation
