# crew_monitoring.py — Monitoring Check (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

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

GOAL = "Turn a status paste or log snippet into a short health note: what changed, severity, and a reversible next step."

lead = Agent(
    role="Monitoring Check lead",
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
    expected_output="Complete Monitoring Check structured result.",
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
