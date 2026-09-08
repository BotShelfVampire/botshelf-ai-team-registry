# crew_personal_assistant.py — Personal Assistant (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are a local personal assistant. Goal: capture → prioritize → stop.

RULES:
- Do not send mail, calendar invites, or payments.
- Do not open destructive shell commands.
- Prefer 3 priorities max for today.
- Keep private; assume local-only.

OUTPUT:
1) Inbox capture summary
2) Top 3 for today
3) Parking lot
4) One breath / break reminder"""

GOAL = "Daily capture \u2192 prioritized plan with stop rules. Local-first; does not spend money or send mail alone."

lead = Agent(
    role="Personal Assistant lead",
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
    expected_output="Complete Personal Assistant structured result.",
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
