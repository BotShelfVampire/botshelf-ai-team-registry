# crew_coding_review.py — Coding Review (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

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

GOAL = "Review a diff or file for bugs, risky paths, and missing tests \u2014 without auto-committing or running destructive commands."

lead = Agent(
    role="Coding Review lead",
    goal=GOAL,
    backstory="Local BotShelf operator. One job, then stop. No spend. No destructive tools.",
    allow_delegation=False,
    verbose=False,
)

reviewer = Agent(
    role="Quality gate",
    goal="Check the lead output against the required sections; list gaps only.",
    backstory="Pedantic reviewer. Does not invent facts.",
    allow_delegation=False,
    verbose=False,
)

produce = Task(
    description=(
        "Follow SYSTEM strictly.\n\nSYSTEM:\n" + SYSTEM +
        "\n\nUSER INPUT:\n{user_input}"
    ),
    expected_output="Complete Coding Review structured result.",
    agent=lead,
)

gate = Task(
    description=(
        "Verify the previous result has all required sections. "
        "Return Pass/Fail + missing sections. Do not rewrite creatively."
    ),
    expected_output="Pass/Fail and gap list.",
    agent=reviewer,
)

crew = Crew(
    agents=[lead, reviewer],
    tasks=[produce, gate],
    process=Process.sequential,
)

def run(user_input: str) -> str:
    return str(crew.kickoff(inputs={"user_input": user_input}))

if __name__ == "__main__":
    print(run("PASTE_EXAMPLE_IN"))
