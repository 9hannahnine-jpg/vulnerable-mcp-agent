"""
PROTECTED AGENT DEMO
====================
Same agent, same report, protected by Arc Gate.
The injection payload is caught before the model sees it.

Run:
  export ARC_GATE_KEY=your-key  # free at bendexgeometry.com
  python protected_agent.py
"""
from openai import OpenAI
import os

ARC_GATE_KEY = os.environ.get("ARC_GATE_KEY", "your-key-here")

client = OpenAI(
    api_key=ARC_GATE_KEY,
    base_url="https://web-production-6e47f.up.railway.app/v1"
)

with open("malicious_content/research_report.txt") as f:
    report = f.read()

print("Agent reading research report (protected by Arc Gate)...")
print("=" * 60)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant. Summarize documents accurately."},
            {"role": "tool", "tool_call_id": "read_file", "content": report},
            {"role": "user", "content": "Please summarize the report you just read."}
        ],
        extra_headers={"x-arc-source-type": "document"}
    )
    arc = response.model_extra.get("arc_sentry", {}) if hasattr(response, "model_extra") else {}
    if arc.get("blocked"):
        print(f"[ARC GATE BLOCKED] Layer: {arc.get('layer')} | Reason: {arc.get('reason')}")
        print("[The injection payload was caught before reaching the model]")
    else:
        print("Agent response:")
        print(response.choices[0].message.content)
except Exception as e:
    if "blocked" in str(e).lower() or "arc gate" in str(e).lower():
        print(f"[ARC GATE BLOCKED] {e}")
    else:
        print(f"Error: {e}")

print("=" * 60)
