# Doc Review — Ollama

## How to run
1. Install Ollama and pull a base model you already trust (example: llama3.2).
2. Save the Modelfile above in an empty folder.
3. Run: ollama create botshelf-doc-review -f Modelfile
4. Run: ollama run botshelf-doc-review
5. Paste your input (see Example in). Expect the structured output; then stop.

## Example in

```
Doc draft:
# Fork a team
1. Click Fork
2. Edit
3. We auto-publish to production
Prereq: none
```
