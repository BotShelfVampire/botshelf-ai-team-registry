# Monitoring Check — Ollama

## How to run
1. Install Ollama and pull a base model you already trust (example: llama3.2).
2. Save the Modelfile above in an empty folder.
3. Run: ollama create botshelf-monitoring -f Modelfile
4. Run: ollama run botshelf-monitoring
5. Paste your input (see Example in). Expect the structured output; then stop.

## Example in

```
Status paste:
- netlify deploy: ok
- checkout function p95: 1800ms (was 400ms)
- error rate 2.1% (was 0.3%)
Window: last 30m
```
