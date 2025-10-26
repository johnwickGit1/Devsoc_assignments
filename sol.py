import requests
import json
import os

#1. config
API_URL = ".."
API_KEY = ".."           
MODEL = ".."                      
INPUT_FILE = "prompts.txt"                    
OUTPUT_FILE = "responses.json"               

# 2. prompts
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    prompts = [line.strip() for line in file if line.strip()]

responses = []

# 3. send prompts 
for idx, prompt in enumerate(prompts, start=1):
    print(f"Sending prompt {idx}: {prompt}")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()

    # 4. replies
    message = result.get("choices", [{}])[0].get("message", {}).get("content", "")
    responses.append({
        "id": idx,
        "prompt": prompt,
        "response": message
    })

# 5. saving results as json
with open(OUTPUT_FILE, "w") as f:
    json.dump(responses, f, indent=4)

print(f"Saved {len(responses)} responses to {OUTPUT_FILE}")
