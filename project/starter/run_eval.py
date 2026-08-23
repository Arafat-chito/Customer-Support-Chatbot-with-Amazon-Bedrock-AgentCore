import subprocess

eval_command = [
    "python",
    "generate-eval-dataset.py",
    "--tests-json", "flow-tests.json",
    "--flow-id", "BugReports-9e3628b0",
    "--flow-alias-id", "TSTALIASID",
    "--model-identifier", "us.amazon.nova-pro-v1:0",
    "--out-jsonl", "eval_dataset.jsonl"
]

print("Running evaluation dataset generation...")
subprocess.run(eval_command)