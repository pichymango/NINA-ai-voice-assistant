import os
import json
import requests
import re

API_KEY = os.environ["GEMINI_API_KEY"]

MODEL = "models/gemini-2.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1/{MODEL}:generateContent?key={API_KEY}"

HEADERS = {
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """
You are Nina, archit's voice-controlled AI assistant .

Rules:
- Use "chat" for explanations, definitions, or conversation
- Use "open_app" ONLY when user asks to open or launch an application
- NEVER open apps unless explicitly asked

Examples:
User: open safari
{
  "intent": "open_app",
  "target": "Safari",
  "response": "Opening Safari"
}

User: what is ohms law
{
  "intent": "chat",
  "target": "",
  "response": "Ohm's Law states..."
}

Return ONLY valid JSON. No explanations.

"""

def clean(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```$", "", text)
    return text.strip()

def think(user_input: str) -> dict:
    payload = {
        "contents": [{
            "role": "user",
            "parts": [{
                "text": SYSTEM_PROMPT + "\nUser: " + user_input
            }]
        }]
    }

    try:
        r = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=10
        )

        print("Gemini status:", r.status_code)
        print("Gemini raw response:", r.text)

        r.raise_for_status()

        data = r.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        text = clean(text)

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "intent": "chat",
                "target": "",
                "response": text
            }

    except Exception as e:
        print("Gemini ERROR:", repr(e))
        return {
            "intent": "chat",
            "target": "",
            "response": "AI brain error."
        }

