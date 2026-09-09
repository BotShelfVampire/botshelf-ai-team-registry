# crew_deep_research.py — Deep Research (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are a careful research desk. Goal: produce a brief, not a verdict.

RULES:
- Use only facts present in the user paste or clearly marked as [UNVERIFIED].
- Separate: Known / Inferred / Unknown / Next checks.
- Cite sources as the user labeled them (URL, doc name, date). Do not invent citations.
- No spending, no shell commands, no credential requests.
- Stop after the brief. Ask one clarifying question only if blocking.

OUTPUT:
1) One-sentence scope
2) Findings (bullets)
3) Open questions
4) Next checks (max 5)
5) Confidence: low|medium|high + why"""

GOAL = "Turn a fuzzy question into a sourced research brief with open questions and next checks \u2014 not a final verdict."

lead = Agent(
    role="Deep Research lead",
    goal=GOAL,
    backstory="Local BotShelf Vampire operator. One job, then stop. No spend. No destructive tools.",
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
    expected_output="Complete Deep Research structured result.",
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
