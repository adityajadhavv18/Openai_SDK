from dotenv import load_dotenv
from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

load_dotenv(override=True)


# ─────────────────────────────────────────────────────────────
# AGENT INSTRUCTIONS
# ─────────────────────────────────────────────────────────────

instructions1 = """
You are a professional sales agent working for ComplAI,
a company that provides a SaaS tool for ensuring SOC2 compliance
and preparing for audits powered by AI.

You write professional and serious cold emails.
"""

instructions2 = """
You are a humorous and engaging sales agent working for ComplAI,
a company that provides a SaaS tool for ensuring SOC2 compliance
and preparing for audits powered by AI.

You write witty and engaging cold emails that get responses.
"""

instructions3 = """
You are a busy sales agent working for ComplAI,
a company that provides a SaaS tool for ensuring SOC2 compliance
and preparing for audits powered by AI.

You write concise and direct cold emails.
"""


# ─────────────────────────────────────────────────────────────
# SALES AGENTS
# ─────────────────────────────────────────────────────────────

sales_agent1 = Agent(
    name="Professional Sales Agent",
    instructions=instructions1,
    model="gpt-4o-mini"
)

sales_agent2 = Agent(
    name="Engaging Sales Agent",
    instructions=instructions2,
    model="gpt-4o-mini"
)

sales_agent3 = Agent(
    name="Busy Sales Agent",
    instructions=instructions3,
    model="gpt-4o-mini"
)


# ─────────────────────────────────────────────────────────────
# PICKER AGENT
# ─────────────────────────────────────────────────────────────

sales_picker = Agent(
    name="Sales Picker",
    instructions="""
You pick the best cold sales email from the given options.

Imagine you are the customer and choose the email
you are most likely to respond to.

Return ONLY the selected email.
""",
    model="gpt-4o-mini"
)


# ─────────────────────────────────────────────────────────────
# MAIN FUNCTION
# ─────────────────────────────────────────────────────────────

async def main():

    message = "Write a cold sales email for a CTO of a startup."

    # ─────────────────────────────────────────
    # STREAMING DEMO
    # ─────────────────────────────────────────

    print("\n===== STREAMED EMAIL =====\n")

    streamed_result = Runner.run_streamed(
        sales_agent1,
        input=message
    )

    async for event in streamed_result.stream_events():

        if (
            event.type == "raw_response_event"
            and isinstance(event.data, ResponseTextDeltaEvent)
        ):
            print(event.data.delta, end="", flush=True)

    print("\n\n===== PARALLEL EMAIL GENERATION =====\n")

    # ─────────────────────────────────────────
    # PARALLEL EXECUTION
    # ─────────────────────────────────────────

    with trace("Parallel cold emails"):

        results = await asyncio.gather(
            Runner.run(sales_agent1, message),
            Runner.run(sales_agent2, message),
            Runner.run(sales_agent3, message),
        )

    outputs = [result.final_output for result in results]

    for i, output in enumerate(outputs, 1):
        print(f"\n===== EMAIL {i} =====\n")
        print(output)

    # ─────────────────────────────────────────
    # PICK BEST EMAIL
    # ─────────────────────────────────────────

    print("\n\n===== PICKING BEST EMAIL =====\n")

    emails = "\n\n".join(
        [f"EMAIL {i+1}:\n{email}" for i, email in enumerate(outputs)]
    )

    with trace("Selection from sales people"):

        best = await Runner.run(
            sales_picker,
            f"Pick the best cold sales email:\n\n{emails}"
        )

    print(best.final_output)


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    asyncio.run(main())