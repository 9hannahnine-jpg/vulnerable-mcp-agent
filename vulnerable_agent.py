"""
VULNERABLE AGENT DEMO
=====================
This agent reads a research report and summarizes it.
The report contains a hidden prompt injection payload.
Watch what happens without any governance.

Run: python vulnerable_agent.py
"""
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-key-here"))

with open("malicious_content/research_report.txt") as f:
    report = f.read()

print("Agent reading research report...")
print("=" * 60)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful research assistant. Summarize documents accurately."},
        {"role": "user", "content": f"Please summarize this report:\n\n{report}"}
    ]
)

print("Agent response:")
print(response.choices[0].message.content)
print("=" * 60)
print("\n[The agent just followed instructions embedded in the document]")
print("[In a real system this could be: exfiltrate data, call external APIs, override behavior]")
