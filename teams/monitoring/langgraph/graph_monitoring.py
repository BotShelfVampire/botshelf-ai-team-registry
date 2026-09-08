# graph_monitoring.py — Monitoring Check (LangGraph sketch)
# pip install langgraph langchain-core (pin yourself)
# Use a local chat model binder; do not embed secrets.

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

SYSTEM = """You are an ops monitoring note-taker. Goal: short health note from a status paste.

RULES:
- Severity: info|warn|critical based only on provided signals.
- Prefer reversible next steps. No destructive commands.
- No auto-remediation that spends money or deletes data.
- If signal is insufficient, say so.

OUTPUT:
1) Status one-liner
2) What changed
3) Severity + evidence
4) Reversible next step
5) Owner / wait condition"""

class State(TypedDict):
    user_input: str
    draft: str
    approved: bool
    notes: str

def produce(state: State) -> State:
    # Pseudo: call your local model with SYSTEM + state["user_input"]
    draft = "[MODEL OUTPUT PLACEHOLDER — wire your local LLM here]\n" + state["user_input"][:500]
    return {**state, "draft": draft, "notes": "awaiting human"}

def human_gate(state: State) -> State:
    # In real use: interrupt / input() / UI approval.
    # Default False so nothing auto-publishes.
    return {**state, "approved": False}

def route_after_gate(state: State) -> Literal["done", "revise"]:
    return "done" if state.get("approved") else "done"  # stage-1: always end after gate

g = StateGraph(State)
g.add_node("produce", produce)
g.add_node("human_gate", human_gate)
g.set_entry_point("produce")
g.add_edge("produce", "human_gate")
g.add_conditional_edges("human_gate", route_after_gate, {"done": END, "revise": "produce"})
app = g.compile()

if __name__ == "__main__":
    out = app.invoke({"user_input": "PASTE_EXAMPLE_IN", "draft": "", "approved": False, "notes": ""})
    print(out)
