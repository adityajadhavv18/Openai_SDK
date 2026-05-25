# import os
# import asyncio
# import sendgrid

# from dotenv import load_dotenv

# from agents import (
#     Agent,
#     Runner,
#     trace,
#     function_tool
# )

# from sendgrid.helpers.mail import (
#     Mail,
#     Email,
#     To,
#     Content
# )

# # ─────────────────────────────────────────────────────────────
# # LOAD ENV VARIABLES
# # ─────────────────────────────────────────────────────────────

# load_dotenv(override=True)


# # ─────────────────────────────────────────────────────────────
# # EMAIL TOOL
# # ─────────────────────────────────────────────────────────────

# @function_tool
# def send_email(body: str):
#     """
#     Send out an email with the given body.
#     """

#     sg = sendgrid.SendGridAPIClient(
#         api_key=os.environ.get("SENDGRID_API_KEY")
#     )

#     from_email = Email("aadityaj.sas@gmail.com")
#     to_email = To("aditya.jadhav21@pccoepune.org")

#     content = Content("text/plain", body)

#     mail = Mail(
#         from_email,
#         to_email,
#         "Sales Email",
#         content
#     ).get()

#     response = sg.client.mail.send.post(
#         request_body=mail
#     )

#     return {
#         "status": "success",
#         "status_code": response.status_code
#     }


# # ─────────────────────────────────────────────────────────────
# # SALES AGENT INSTRUCTIONS
# # ─────────────────────────────────────────────────────────────

# instructions1 = """
# You are a professional sales agent working for ComplAI,
# a company that provides AI-powered SOC2 compliance software.

# You write professional and serious cold emails.
# """

# instructions2 = """
# You are a humorous and engaging sales agent working for ComplAI,
# a company that provides AI-powered SOC2 compliance software.

# You write witty and engaging cold emails.
# """

# instructions3 = """
# You are a concise sales agent working for ComplAI,
# a company that provides AI-powered SOC2 compliance software.

# You write short and direct cold emails.
# """


# # ─────────────────────────────────────────────────────────────
# # SALES AGENTS
# # ─────────────────────────────────────────────────────────────

# sales_agent1 = Agent(
#     name="Professional Sales Agent",
#     instructions=instructions1,
#     model="gpt-4o-mini"
# )

# sales_agent2 = Agent(
#     name="Engaging Sales Agent",
#     instructions=instructions2,
#     model="gpt-4o-mini"
# )

# sales_agent3 = Agent(
#     name="Busy Sales Agent",
#     instructions=instructions3,
#     model="gpt-4o-mini"
# )


# # ─────────────────────────────────────────────────────────────
# # CONVERT AGENTS TO TOOLS
# # ─────────────────────────────────────────────────────────────

# description = "Write a cold sales email for lighting mcqueen."

# tool1 = sales_agent1.as_tool(
#     tool_name="sales_agent1",
#     tool_description=description
# )

# tool2 = sales_agent2.as_tool(
#     tool_name="sales_agent2",
#     tool_description=description
# )

# tool3 = sales_agent3.as_tool(
#     tool_name="sales_agent3",
#     tool_description=description
# )


# # ─────────────────────────────────────────────────────────────
# # TOOL LIST
# # ─────────────────────────────────────────────────────────────

# tools = [
#     tool1,
#     tool2,
#     tool3,
#     send_email
# ]


# # ─────────────────────────────────────────────────────────────
# # MANAGER AGENT
# # ─────────────────────────────────────────────────────────────

# instructions = """
# You are a Sales Manager at ComplAI.

# Your goal is to find the single best cold sales email.

# Follow these steps carefully:

# 1. Use all three sales_agent tools
# to generate three email drafts.

# 2. Compare the drafts carefully.

# 3. Choose the single best email.

# 4. Use the send_email tool
# to send ONLY the best email.

# Rules:
# - Do not write emails yourself.
# - Always use the sales agent tools.
# - Send only ONE email.
# """

# sales_manager = Agent(
#     name="Sales Manager",
#     instructions=instructions,
#     tools=tools,
#     model="gpt-4o-mini"
# )


# # ─────────────────────────────────────────────────────────────
# # MAIN EXECUTION
# # ─────────────────────────────────────────────────────────────

# async def main():

#     message = (
#         "Send a cold sales email addressed to "
#         "'Dear CEO'"
#     )

#     with trace("Sales manager workflow"):

#         result = await Runner.run(
#             sales_manager,
#             message
#         )

#     print("\n===== FINAL RESULT =====\n")

#     print(result.final_output)


# # ─────────────────────────────────────────────────────────────
# # ENTRY POINT
# # ─────────────────────────────────────────────────────────────

# if __name__ == "__main__":
#     asyncio.run(main())


# import os
# import asyncio
# import sendgrid

# from dotenv import load_dotenv

# from agents import (
#     Agent,
#     Runner,
#     trace,
#     function_tool
# )

# from sendgrid.helpers.mail import (
#     Mail,
#     Email,
#     To,
#     Content
# )

# # ─────────────────────────────────────────────────────────────
# # LOAD ENV
# # ─────────────────────────────────────────────────────────────

# load_dotenv(override=True)


# # ─────────────────────────────────────────────────────────────
# # EMAIL TOOL
# # ─────────────────────────────────────────────────────────────

# @function_tool
# def send_email(body: str):
#     """
#     Send ONLY the final selected email.
#     """

#     print("\n\n===== EMAIL BEING SENT =====\n")
#     print(body)

#     sg = sendgrid.SendGridAPIClient(
#         api_key=os.environ.get("SENDGRID_API_KEY")
#     )

#     from_email = Email("aadityaj.sas@gmail.com")
#     to_email = To("aditya.jadhav21@pccoepune.org")

#     content = Content("text/plain", body)

#     mail = Mail(
#         from_email,
#         to_email,
#         "Sales Email",
#         content
#     ).get()

#     response = sg.client.mail.send.post(
#         request_body=mail
#     )

#     return {
#         "status": "success",
#         "status_code": response.status_code
#     }


# # ─────────────────────────────────────────────────────────────
# # SALES AGENTS
# # ─────────────────────────────────────────────────────────────

# instructions1 = """
# You are AGENT_1.

# You are a professional sales agent working for ComplAI.

# IMPORTANT:
# - Start the email EXACTLY with: AGENT_1
# - Never use humor
# - Be formal and professional
# """

# instructions2 = """
# You are AGENT_2.

# You are a humorous and engaging sales agent working for ComplAI.

# IMPORTANT:
# - Start the email EXACTLY with: AGENT_2
# - Use humor and personality
# """

# instructions3 = """
# You are AGENT_3.

# You are a concise sales agent working for ComplAI.

# IMPORTANT:
# - Start the email EXACTLY with: AGENT_3
# - Keep the email short and direct
# """


# sales_agent1 = Agent(
#     name="Professional Sales Agent",
#     instructions=instructions1,
#     model="gpt-4o-mini"
# )

# sales_agent2 = Agent(
#     name="Engaging Sales Agent",
#     instructions=instructions2,
#     model="gpt-4o-mini"
# )

# sales_agent3 = Agent(
#     name="Busy Sales Agent",
#     instructions=instructions3,
#     model="gpt-4o-mini"
# )


# # ─────────────────────────────────────────────────────────────
# # WRAPPER TOOLS
# # (IMPORTANT FOR DEBUGGING)
# # ─────────────────────────────────────────────────────────────

# @function_tool
# async def generate_professional_email(prompt: str):
#     """
#     Generate a professional cold email.
#     """

#     result = await Runner.run(
#         sales_agent1,
#         prompt
#     )

#     print("\n\n===== AGENT 1 OUTPUT =====\n")
#     print(result.final_output)

#     return result.final_output


# @function_tool
# async def generate_funny_email(prompt: str):
#     """
#     Generate a humorous cold email.
#     """

#     result = await Runner.run(
#         sales_agent2,
#         prompt
#     )

#     print("\n\n===== AGENT 2 OUTPUT =====\n")
#     print(result.final_output)

#     return result.final_output


# @function_tool
# async def generate_short_email(prompt: str):
#     """
#     Generate a concise cold email.
#     """

#     result = await Runner.run(
#         sales_agent3,
#         prompt
#     )

#     print("\n\n===== AGENT 3 OUTPUT =====\n")
#     print(result.final_output)

#     return result.final_output


# # ─────────────────────────────────────────────────────────────
# # TOOLS
# # ─────────────────────────────────────────────────────────────

# tools = [
#     generate_professional_email,
#     generate_funny_email,
#     generate_short_email,
#     send_email
# ]


# # ─────────────────────────────────────────────────────────────
# # MANAGER AGENT
# # ─────────────────────────────────────────────────────────────

# manager_instructions = """
# You are a Sales Manager at ComplAI.

# Your job is STRICTLY to:
# 1. Generate 3 drafts using the tools
# 2. Pick ONE best draft
# 3. Send ONLY that draft

# CRITICAL RULES:
# - NEVER rewrite
# - NEVER paraphrase
# - NEVER summarize
# - NEVER modify any email
# - Return EXACTLY one of the generated drafts
# - Preserve every character exactly
# - The selected email MUST still contain:
#   AGENT_1 OR AGENT_2 OR AGENT_3

# You are ONLY allowed to select.
# """


# sales_manager = Agent(
#     name="Sales Manager",
#     instructions=manager_instructions,
#     tools=tools,
#     model="gpt-4o-mini"
# )


# # ─────────────────────────────────────────────────────────────
# # MAIN
# # ─────────────────────────────────────────────────────────────

# async def main():

#     message = (
#         "Write a cold sales email "
#         "addressed to Dear CEO"
#     )

#     with trace("Sales Manager Debug Workflow"):

#         result = await Runner.run(
#             sales_manager,
#             message
#         )

#     print("\n\n===== FINAL MANAGER OUTPUT =====\n")
#     print(result.final_output)


# # ─────────────────────────────────────────────────────────────
# # ENTRY POINT
# # ─────────────────────────────────────────────────────────────

# if __name__ == "__main__":
#     asyncio.run(main())


import os
import asyncio
import sendgrid

from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    trace
)

from sendgrid.helpers.mail import (
    Mail,
    Email,
    To,
    Content
)

load_dotenv(override=True)


# ─────────────────────────────────────────────
# SALES AGENTS
# ─────────────────────────────────────────────

agent1 = Agent(
    name="Professional Agent",
    instructions="""
You are AGENT_1.

Write professional cold emails.
Always start with AGENT_1.
""",
    model="gpt-4o-mini"
)

agent2 = Agent(
    name="Funny Agent",
    instructions="""
You are AGENT_2.

Write funny engaging cold emails.
Always start with AGENT_2.
""",
    model="gpt-4o-mini"
)

agent3 = Agent(
    name="Short Agent",
    instructions="""
You are AGENT_3.

Write concise cold emails.
Always start with AGENT_3.
""",
    model="gpt-4o-mini"
)


# ─────────────────────────────────────────────
# MANAGER AGENT
# ─────────────────────────────────────────────

manager = Agent(
    name="Sales Manager",
    instructions="""
You are a sales manager.

You will receive 3 email drafts.

Your task:
- choose the SINGLE best draft
- DO NOT rewrite anything
- DO NOT modify anything
- return the EXACT winning email only
""",
    model="gpt-4o-mini"
)


# ─────────────────────────────────────────────
# SEND EMAIL
# ─────────────────────────────────────────────

def send_email(body: str):

    sg = sendgrid.SendGridAPIClient(
        api_key=os.getenv("SENDGRID_API_KEY")
    )

    from_email = Email("aadityaj.sas@gmail.com")
    to_email = To("aditya.jadhav21@pccoepune.org")

    content = Content("text/plain", body)

    mail = Mail(
        from_email,
        to_email,
        "Sales Email",
        content
    ).get()

    response = sg.client.mail.send.post(
        request_body=mail
    )

    print("\n===== EMAIL SENT =====\n")
    print(body)

    return response.status_code


# ─────────────────────────────────────────────
# MAIN WORKFLOW
# ─────────────────────────────────────────────

async def main():

    prompt = "Write a cold sales email to a CEO."

    # ─────────────────────────────────
    # Generate drafts in parallel
    # ─────────────────────────────────

    with trace("Generate Drafts"):

        results = await asyncio.gather(
            Runner.run(agent1, prompt),
            Runner.run(agent2, prompt),
            Runner.run(agent3, prompt),
        )

    drafts = [r.final_output for r in results]

    print("\n===== GENERATED DRAFTS =====\n")

    for draft in drafts:
        print(draft)
        print("\n---------------------\n")

    # ─────────────────────────────────
    # Manager selects best draft
    # ─────────────────────────────────

    combined = "\n\n".join(drafts)

    manager_prompt = f"""
Select the best email from these drafts.

IMPORTANT:
Return EXACTLY one draft unchanged.

DRAFTS:
{combined}
"""

    with trace("Select Best Draft"):

        result = await Runner.run(
            manager,
            manager_prompt
        )

    best_email = result.final_output

    print("\n===== SELECTED EMAIL =====\n")
    print(best_email)

    # ─────────────────────────────────
    # Validation Layer
    # ─────────────────────────────────

    valid_agents = [
        "AGENT_1",
        "AGENT_2",
        "AGENT_3"
    ]

    if not any(agent in best_email for agent in valid_agents):
        raise Exception(
            "Manager returned invalid email."
        )

    # ─────────────────────────────────
    # Deterministic Execution
    # ─────────────────────────────────

    send_email(best_email)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    asyncio.run(main())