from groq import Groq
import json
from tools import classify_issue, create_ticket
from config import GROQ_API_KEY, MODEL

client = Groq(api_key=GROQ_API_KEY)


def agent(user_input: str):
    print("\n[User Input]:", user_input)

    # Step 1: classify
    issue_type = classify_issue(user_input)

    # Step 2: LLM extraction
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an IT ticket creation assistant. Always return valid JSON."},
            {"role": "user", "content": f"""
Extract ticket details from:
{user_input}

Return JSON:
title, description, priority (Low/Medium/High)
"""}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        extracted_data = json.loads(content)
    except:
        print("⚠️ Parsing failed, using fallback")
        extracted_data = {
            "title": user_input[:50],
            "description": user_input,
            "priority": "Medium"
        }

    extracted_data["type"] = issue_type

    # Step 3: create ticket
    ticket = create_ticket(extracted_data)

    print("\n[Generated Ticket]:")
    print(json.dumps(ticket, indent=2))


if __name__ == "__main__":
    while True:
        user_input = input("\nEnter issue (or 'exit'): ")
        if user_input.lower() == "exit":
            break
        agent(user_input)
