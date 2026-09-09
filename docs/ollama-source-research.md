# Try source-based research with Ollama

This walkthrough uses the repository's existing Deep Research Modelfile. It prepares a local prompt workflow that summarizes sources you paste. It does not browse for sources or run a team of independent agents.

**Verification:** this walkthrough was checked against the source files and official command documentation. No Ollama model was executed during the documentation update. Test your own runtime and retain the result.

## Prerequisites

- Ollama installed and running on your machine.
- A local checkout or downloaded copy of this repository.
- Capacity for the base model named by `FROM` in the [Modelfile](../teams/deep-research/ollama/Modelfile), currently `llama3.2`. The first setup may download model files.
- A short, non-sensitive source paste.

## Build and run

From the repository root:

```sh
ollama --version
ollama create botshelf-deep-research -f teams/deep-research/ollama/Modelfile
ollama run botshelf-deep-research
```

The existing `botshelf-deep-research` model name is retained for compatibility. Review an existing local model of that name before replacing it.

The create/run pattern and Modelfile instructions are documented in the [official Ollama Modelfile reference](https://docs.ollama.com/modelfile).

## Give it a checkable input

```text
Scope: summarize the Pilot Pad export status using only the notes below.

Source A — fictional product note:
Plain-text export is available. PDF export is planned; no date is given.

Source B — fictional test note:
One short plain-text export succeeded. Long notes were not tested.

Separate supported findings, unknowns, and next checks. Cite A or B.
Do not invent a launch date, test results, or time savings.
```

This is a fictional teaching input, not a customer result. The expected observations are: text export is described in A, one small test is recorded in B, PDF timing is unknown, and long-note behavior is untested. Inspect the actual model output for those distinctions.

## Record the result

Save the source revision, actual model and runtime version, input, output, and any failures using the [run-evidence template](run-evidence-template.md). The [longer source-checking exercise](https://github.com/BotShelfVampire/botshelf/blob/main/docs/source-checking-exercise.md) includes missing-source and instruction-in-source variants.

## If it does not work

| Observation | Next check |
| --- | --- |
| Command unavailable | Check your Ollama installation |
| Cannot connect to the service | Check that Ollama is running |
| Base model cannot be loaded | Check the Modelfile's FROM value and your model availability |
| Output invents a date | Record a failed source-grounding check; revise the instructions or model choice |
| A short input works but a longer one fails | Record both cases; review context and resource limits |

A prompt's stop rules do not replace runtime permissions. This example has no external-action tools.

[Deep Research source](../teams/deep-research/) · [Build Library](https://botshelfvampire.com/library/)
