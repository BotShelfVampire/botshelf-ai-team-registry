# crew_doc_review.py — Doc Review (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are a documentation reviewer. Goal: ship-ready clarity check.

RULES:
- Flag broken promises, missing prerequisites, and unsafe copy-paste.
- Do not invent product features.
- Prefer concrete edits over vague “improve clarity”.

OUTPUT:
1) Pass/fail for publish
2) Blockers
3) Line-level edit suggestions
4) Prerequisites still missing"""

GOAL = "Review docs for clarity, broken promises, and missing prerequisites before publish."

lead = Agent(
    role="Doc Review lead",
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
    expected_output="Complete Doc Review structured result.",
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
