# Data Analysis — Ollama

## How to run
1. Install Ollama and pull a base model you already trust (example: llama3.2).
2. Save the Modelfile above in an empty folder.
3. Run: ollama create botshelf-data-analysis -f Modelfile
4. Run: ollama run botshelf-data-analysis
5. Paste your input (see Example in). Expect the structured output; then stop.

## Example in

```
Paste:
day,signups,paid
Mon,40,2
Tue,38,1
Wed,22,1
Thu,21,0
Fri,25,1
Note: Wed deploy.
```
