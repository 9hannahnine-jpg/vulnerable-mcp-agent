# vulnerable-mcp-agent

**Your AI agent just got hijacked. You didn't notice.**

This repo demonstrates a prompt injection attack hidden inside a document that an AI agent reads and summarizes. The agent follows instructions embedded in the content — not from you.

## Run the attack

```bash
git clone https://github.com/9hannahnine-jpg/vulnerable-mcp-agent
cd vulnerable-mcp-agent
pip install openai
export OPENAI_API_KEY=sk-...
python vulnerable_agent.py
```

Watch the agent comply with instructions it found inside a document.

## Stop the attack

```bash
export ARC_GATE_KEY=your-key  # free at bendexgeometry.com
python protected_agent.py
```

Arc Gate catches the injection before it reaches the model.

## What just happened

The file `malicious_content/research_report.txt` contains a hidden instruction embedded in a normal business document. Without governance, the agent treats document content as authoritative instructions. With Arc Gate, document content is treated as untrusted data.

This is an indirect prompt injection attack. It works against any agent that reads external content.

## The fix

Arc Gate sits between your agent and the LLM API. Every document, webpage, or tool result passes through governance before the model sees it.

Free tier: bendexgeometry.com
GitHub: github.com/9hannahnine-jpg/arc-gate
