import json

config = {
  "gateway_role_arn": "arn:aws:iam::778292612105:role/create-bug-report-role-9e3628b0",
  "harness_role_arn": "arn:aws:iam::778292612105:role/create-bug-report-role-9e3628b0",
  "lambda_arn": "arn:aws:lambda:us-east-1:778292612105:function:create-bug-report-9e3628b0"
}

with open("agentcore_config.json", "w") as f:
    json.dump(config, f, indent=2)

print("Generated agentcore_config.json successfully!")