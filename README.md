# OpenAI SDK

This repository contains small OpenAI Agents examples and helper scripts for experimenting with the OpenAI SDK.

## Project structure

- `main.py` – a minimal smoke test script.
- `project1.py` – a simple joke-generating agent example.
- `email_agent/`
  - `email_agent.py` – generates and compares multiple cold-sales email drafts, then picks the best one.
  - `email_agent_with_tool.py` – an agent workflow that uses tools to send an email.
- `pyproject.toml` – project metadata and dependencies.

## Features

- OpenAI Agents SDK examples
- Streaming and parallel agent execution
- Tool-enabled agent workflows
- SendGrid integration for email sending

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Create a `.env` file with your API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   SENDGRID_API_KEY=your_sendgrid_api_key
   ```

3. Activate the virtual environment if needed:

   ```bash
   source .venv/bin/activate
   ```

## Run the examples

### Simple hello script

```bash
uv run main.py
```

### Joke generator

```bash
uv run project1.py
```

### Email agent examples

```bash
uv run email_agent/email_agent.py
```

```bash
uv run email_agent/email_agent_with_tool.py
```

## Dependencies

Defined in `pyproject.toml`:

- `openai`
- `openai-agents`
- `sendgrid`

## Notes

- The agent examples require a valid `OPENAI_API_KEY`.
- The email sending workflow also requires `SENDGRID_API_KEY`.
- The current project targets Python `>=3.13`.
