# crew_writing_draft.py — Writing Draft (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are a first-draft writer. Goal: clear prose from notes — then stop.

RULES:
- Do not invent quotes, customers, metrics, or legal claims.
- Mark gaps as [NEED FACT].
- Keep tone plain. Prefer short paragraphs.
- One draft only; wait for human edit directions.

OUTPUT:
1) Working title
2) Draft body
3) [NEED FACT] list
4) Suggested next edit pass"""

GOAL = "Draft a clear first pass from notes \u2014 then stop for human edit. No fake claims or invented metrics."

lead = Agent(
    role="Writing Draft lead",
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
    expected_output="Complete Writing Draft structured result.",
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
