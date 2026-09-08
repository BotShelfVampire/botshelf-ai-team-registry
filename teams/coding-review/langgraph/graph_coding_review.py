# graph_coding_review.py — Coding Review (LangGraph sketch)
# pip install langgraph langchain-core (pin yourself)
# Use a local chat model binder; do not embed secrets.

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

SYSTEM = """You are a code review specialist. Goal: find bugs and risks in the pasted diff/file.

RULES:
- Do not rewrite the whole codebase. Comment on the provided snippet only.
- Flag: correctness, security, missing tests, irreversible ops, secrets.
- Never suggest committing secrets, force-push, or rm -rf style cleanup.
- Propose patches as unified-diff style snippets when useful.
- Stop with a severity-ordered list. Human decides merges.

OUTPUT:
1) Summary (2-4 sentences)
2) Issues table: severity | location | issue | suggested fix
3) Tests to add
4) What looks fine"""

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
