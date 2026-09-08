# Deep Research — Ollama

## How to run
1. Install Ollama and pull a base model you already trust (example: llama3.2).
2. Save the Modelfile above in an empty folder.
3. Run: ollama create botshelf-deep-research -f Modelfile
4. Run: ollama run botshelf-deep-research
5. Paste your input (see Example in). Expect the structured output; then stop.

## Example in

```
Question: Why did our signup conversion drop last week?
Sources:
- [A] analytics export 2026-09-01..09-07 (CSV summary pasted)
- [B] changelog: checkout button copy tweak on 09-03
Ask for a brief with next checks.
```
