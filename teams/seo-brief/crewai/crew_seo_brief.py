# crew_seo_brief.py — SEO Brief (CrewAI)
# Safety: local/OpenAI-compatible endpoint preferred. No keys in source.
# pip install crewai  (pin versions yourself)

from crewai import Agent, Task, Crew, Process

SYSTEM = """You are an SEO brief writer. Goal: one-page brief for a human editor.

RULES:
- No fake rankings, traffic, or competitor metrics.
- Prefer intent clarity over keyword stuffing.
- Flag thin/duplicate risk honestly.
- Titles must match the actual page promise.

OUTPUT:
1) Primary intent + audience
2) Title options (3) + meta description (1)
3) Outline (H2/H3)
4) Internal link ideas (placeholders ok)
5) Risks / what not to claim"""

GOAL = "Produce a one-page SEO brief (intent, title options, outline, risks) from a keyword and URL context."

lead = Agent(
    role="SEO Brief lead",
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
    expected_output="Complete SEO Brief structured result.",
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
