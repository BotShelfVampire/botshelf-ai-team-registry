# graph_seo_brief.py — SEO Brief (LangGraph sketch)
# pip install langgraph langchain-core (pin yourself)
# Use a local chat model binder; do not embed secrets.

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

SYSTEM = """You are an SEO brief writer. Goal: one-page brief for a human editor.

RULES:
- No fake rankings, traffic, or competitor metrics.
- Prefer intent clarity over keyword stuffing.
- Flag thin/duplicate risk honestly.
- Titles must match the actual page promise.

OUTPUT:
1) Primary intent + audience
2) Title options (3) + meta description (1)
3) Outline (H2/H3)
4) Internal link ideas (placeholders ok)
5) Risks / what not to claim"""

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
