# crewai — Writing Draft — CrewAI

## How to run
- Create a venv; install CrewAI (pin versions yourself).
- Configure a local OpenAI-compatible base URL when possible.
- Save crew_writing_draft.py and run: python crew_writing_draft.py
- Replace PASTE_EXAMPLE_IN with your real input.
- Read Pass/Fail gate output before trusting the draft.

## Notes

Two-agent crew (produce + gate). Keep tools disabled unless you add read-only tools on purpose.

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/writing-draft/
- Implementation: https://botshelfvampire.com/library/crewai/writing-draft/
- Registry: https://botshelfvampire.com/library/registry.json

## Model configuration

The accompanying script does not explicitly bind a local model provider. Configure the LLM you intend to use before running it; the word local in a comment does not select an endpoint or prevent provider charges. Record the actual model, dependencies, input, and output when testing.
