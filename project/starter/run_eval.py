import subprocess

eval_command = [
    "python",
    "generate-eval-dataset.py",
    "--tests-json", "flow-tests.json",
    "--flow-id", "D3MYMJVDRZ",
    "--flow-alias-id", "TSTALIASID",
    "--model-identifier", "eval_dataset.jsonl",
    "--out-jsonl", "eval_dataset.jsonl"
]

print("Running evaluation dataset generation...")
subprocess.run(eval_command)