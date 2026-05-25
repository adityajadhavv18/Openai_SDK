import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace, set_default_openai_api

load_dotenv()

set_default_openai_api("responses")

agent = Agent(
    name="Jokster",
    instructions="You are a joke teller.",
    model="gpt-4o-mini"
)

async def main():
    with trace("Telling a joke"):
        result = await Runner.run(
            agent,
            "Tell me a joke about cricketers"
        )

        print(result.final_output)

asyncio.run(main())