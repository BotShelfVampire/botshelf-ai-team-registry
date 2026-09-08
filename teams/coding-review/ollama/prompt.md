# Coding Review — Ollama

## How to run
1. Install Ollama and pull a base model you already trust (example: llama3.2).
2. Save the Modelfile above in an empty folder.
3. Run: ollama create botshelf-coding-review -f Modelfile
4. Run: ollama run botshelf-coding-review
5. Paste your input (see Example in). Expect the structured output; then stop.

## Example in

```
Review this Python snippet:
```
def pay(user, amount):
    charge(user.card, amount)
    send_receipt(user.email)
```
Context: internal tool, no retries yet.
```
