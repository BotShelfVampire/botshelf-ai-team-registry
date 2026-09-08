# langgraph — Personal Assistant — LangGraph

## How to run
- Install LangGraph in a venv (pin versions).
- Wire produce() to your local model client.
- Run the file once with Example in.
- Keep human_gate approval defaulting to False; enable revise only intentionally.

## Notes

Graph includes an explicit human checkpoint. Stage-1 ends after gate (no infinite revise loop).

## Canonical links

- Team parent: https://botshelfvampire.com/library/teams/personal-assistant/
- Implementation: https://botshelfvampire.com/library/langgraph/personal-assistant/
- Registry: https://botshelfvampire.com/library/registry.json
