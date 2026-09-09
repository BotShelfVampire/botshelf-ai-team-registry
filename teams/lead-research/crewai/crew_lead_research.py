# crew_lead_research.py — Lead Research (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

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

GOAL = "Build a respectful lead brief from public facts you paste \u2014 no scraping secrets, no spam scripts."

lead = Agent(
    role="Lead Research lead",
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
    expected_output="Complete Lead Research structured result.",
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
