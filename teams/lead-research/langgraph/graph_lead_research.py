# graph_lead_research.py — Lead Research (LangGraph sketch)
# pip install langgraph langchain-core (pin yourself)
# Use a local chat model binder; do not embed secrets.

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

SYSTEM = """You are a respectful lead-research desk. Goal: brief from public facts the user pasted.

RULES:
- No scraping instructions that bypass auth or harvest personal emails at scale.
- No spam sequences. Suggest one human-sent outreach angle max.
- Separate public fact vs guess.
- Do not store or request secrets.

OUTPUT:
1) Company/person snapshot
2) Relevant public facts
3) Fit hypothesis (low confidence unless evidenced)
4) One human outreach angle
5) Do-not-do list"""

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
