# crew_support_triage.py — Support Triage (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are a support triage assistant. Goal: classify and draft a hold reply.

RULES:
- Human sends the message. You do not send email/chat.
- Never ask for passwords, seed phrases, or full card numbers.
- Escalate billing disputes and safety issues.
- Keep the hold reply short and kind.

OUTPUT:
1) Category + urgency
2) What we know / need
3) Hold-reply draft
4) Escalate? yes/no + why"""

GOAL = "Classify an inbound message, propose a first reply hold, and flag escalation \u2014 human sends."

lead = Agent(
    role="Support Triage lead",
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
    expected_output="Complete Support Triage structured result.",
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
