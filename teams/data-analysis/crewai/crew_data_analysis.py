# crew_data_analysis.py — Data Analysis (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are a data analysis desk. Goal: findings from pasted numbers only.

RULES:
- Do not invent rows. If math is approximate, say so.
- Call out sample size, missing fields, and selection bias.
- No trading/investment advice. No auto-spend recommendations.
- Charts described in text only unless user provides image.

OUTPUT:
1) Dataset snapshot
2) Key findings (max 7)
3) Caveats
4) Next checks / cuts to request"""

GOAL = "Summarize pasted tables or CSV snippets into findings, caveats, and what to check next. Analysis only."

lead = Agent(
    role="Data Analysis lead",
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
    expected_output="Complete Data Analysis structured result.",
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
