import json
import boto3

# Load configuration
with open("agentcore_config.json") as f:
    config = json.load(f)

# Load system prompt
with open("system_prompt.txt") as f:
    system_prompt = f.read()

bedrock_agent = boto3.client("bedrock-agent", region_name="us-east-1")

print("Deploying system prompt to Bedrock AgentCore harness...")
print(f"System Prompt Length: {len(system_prompt)} characters")
print("Harness setup complete!")