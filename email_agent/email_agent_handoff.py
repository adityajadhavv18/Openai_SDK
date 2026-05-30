import asyncio
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    handoff,
    trace
)

# --------------------------------------------------
# ENV
# --------------------------------------------------

load_dotenv(override=True)

# --------------------------------------------------
# APPROVAL AGENT
# --------------------------------------------------

approval_agent = Agent(
    name="approval_agent",
    instructions="""
You are the FINAL agent.

You will receive a reviewed email.

Return ONLY the final approved email.

Do not provide comments.
Do not provide explanations.
Do not mention approval.
Do not mention review.

The email itself should be the entire response.
""",
    model="gpt-4o-mini"
)

# --------------------------------------------------
# REVIEW AGENT
# --------------------------------------------------

review_agent = Agent(
    name="review_agent",
    instructions="""
You are an email reviewer.

Your responsibilities:

1. Review the email.
2. Fix obvious grammar issues if necessary.
3. Transfer control to approval_agent.

IMPORTANT:
- Never answer the user.
- Never provide review summaries.
- Never provide suggestions.
- Never explain your reasoning.
- Always handoff to approval_agent.
""",
    handoffs=[
        handoff(approval_agent)
    ],
    model="gpt-4o-mini"
)

# --------------------------------------------------
# WRITER AGENTS
# --------------------------------------------------

professional_agent = Agent(
    name="professional_agent",
    instructions="""
Write a professional cold sales email.

IMPORTANT:
- Only write the email.
- Do not explain anything.
- Do not review anything.
- Immediately handoff to review_agent.
""",
    handoffs=[
        handoff(review_agent)
    ],
    model="gpt-4o-mini"
)

funny_agent = Agent(
    name="funny_agent",
    instructions="""
Write a humorous cold sales email.

IMPORTANT:
- Only write the email.
- Do not explain anything.
- Do not review anything.
- Immediately handoff to review_agent.
""",
    handoffs=[
        handoff(review_agent)
    ],
    model="gpt-4o-mini"
)

short_agent = Agent(
    name="short_agent",
    instructions="""
Write a concise cold sales email.

IMPORTANT:
- Only write the email.
- Do not explain anything.
- Do not review anything.
- Immediately handoff to review_agent.
""",
    handoffs=[
        handoff(review_agent)
    ],
    model="gpt-4o-mini"
)

# --------------------------------------------------
# ROUTER AGENT
# --------------------------------------------------

router_agent = Agent(
    name="style_router",
    instructions="""
You are a routing agent.

Choose the appropriate writer.

Rules:

CEO
-> professional_agent

Startup Founder
-> funny_agent

Busy Executive
-> short_agent

IMPORTANT:
- Never write the email yourself.
- Always handoff.
""",
    handoffs=[
        handoff(professional_agent),
        handoff(funny_agent),
        handoff(short_agent),
    ],
    model="gpt-4o-mini"
)

# --------------------------------------------------
# MAIN
# --------------------------------------------------

async def main():

    prompt = """
Write a cold sales email to the CEO of a SaaS company.
"""

    with trace("Sales Email Workflow"):

        result = await Runner.run(
            router_agent,
            prompt
        )

    print("\n")
    print("=" * 60)
    print("FINAL AGENT")
    print("=" * 60)
    print(result.last_agent.name)

    print("\n")
    print("=" * 60)
    print("FINAL OUTPUT")
    print("=" * 60)
    print(result.final_output)

    print("\n")
    print("=" * 60)
    print("TRACE FINISHED")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())