import json
import boto3

cfn = boto3.client("cloudformation", region_name="us-east-1")

try:
    response = cfn.describe_stacks(StackName="bug-report-tool-stack")
    outputs = {o["OutputKey"]: o["OutputValue"] for o in response["Stacks"][0].get("Outputs", [])}

    config = {
        "gateway_role_arn": outputs.get("GatewayRoleArn") or outputs.get("AgentCoreGatewayRoleArn") or outputs.get("LambdaExecutionRoleArn"),
        "harness_role_arn": outputs.get("HarnessRoleArn") or outputs.get("AgentCoreHarnessRoleArn") or outputs.get("BedrockEvalRoleArn"),
        "lambda_arn": outputs.get("LambdaFunctionArn") or outputs.get("CreateBugReportLambdaArn"),
    }

    with open("agentcore_config.json", "w") as f:
        json.dump(config, f, indent=2)

    print("\nSuccessfully updated agentcore_config.json:")
    print(json.dumps(config, indent=2))

except Exception as e:
    print(f"Error fetching stack outputs: {e}")