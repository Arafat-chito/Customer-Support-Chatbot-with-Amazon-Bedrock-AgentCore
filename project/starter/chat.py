import boto3
import json

# Load system prompt and config
with open("system_prompt.txt") as f:
    system_prompt = f.read()

with open("online_shop_faq.md") as f:
    faq_content = f.read()

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

messages = []
print("--- Customer Support Chatbot Online (type 'exit' to quit) ---")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        break
        
    messages.append({"role": "user", "content": [{"text": user_input}]})
    
    # Model call using Amazon Nova Pro model pinned for this project
    response = bedrock.converse(
        modelId="us.amazon.nova-pro-v1:0",
        messages=messages,
        system=[{"text": f"{system_prompt}\n\nStore Knowledge FAQ:\n{faq_content}"}]
    )
    
    reply = response["output"]["message"]["content"][0]["text"]
    messages.append({"role": "assistant", "content": [{"text": reply}]})
    print(f"\nBot: {reply}")