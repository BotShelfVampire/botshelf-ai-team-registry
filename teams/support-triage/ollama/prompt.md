# Support Triage — Ollama

## How to run
1. Install Ollama and pull a base model you already trust (example: llama3.2).
2. Save the Modelfile above in an empty folder.
3. Run: ollama create botshelf-support-triage -f Modelfile
4. Run: ollama run botshelf-support-triage
5. Paste your input (see Example in). Expect the structured output; then stop.

## Example in

```
From: user@example.com
Subject: charged twice?
Body: I see two USDT sends. Order #1842. Need help.
```
