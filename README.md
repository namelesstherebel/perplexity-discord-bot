# Perplexity Discord Bot

A Discord bot that integrates with Perplexity AI to answer questions and conduct deep research directly within Discord.

## Features

- **/ask [query]**: Ask Perplexity AI anything (uses `sonar-pro` model).
- **/research [topic]**: Conduct deep research on a topic (uses `sonar-deep-research` model).
- **Smart Chunking**: Automatically splits long responses into multiple messages to fit Discord's character limit.

## Prerequisites

- Python 3.8+
- A Discord Bot Token
- A Perplexity API Key

## Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Perplexity-Discord-Bot
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    - Rename `.env.example` to `.env` (or create a new `.env` file).
    - Add your API keys:
      ```env
      DISCORD_TOKEN=your_discord_token
      PERPLEXITY_API_KEY=your_perplexity_api_key
      ```

5.  **Run the bot:**
    ```bash
    python perplexity-bot.py
    ```

## Deployment on Render

This project is configured for easy deployment on [Render](https://render.com).

1.  Push this code to a GitHub/GitLab repository.
2.  In Render, create a new **Blueprint** instance.
3.  Connect your repository.
4.  Render will automatically detect the `render.yaml` configuration.
5.  **Important:** You must manually set the environment variables in the Render dashboard for your service:
    - `DISCORD_TOKEN`
    - `PERPLEXITY_API_KEY`

## Technologies

- [discord.py](https://discordpy.readthedocs.io/)
- [OpenAI Python Library](https://github.com/openai/openai-python) (compatible with Perplexity API)
- [Render](https://render.com/) for hosting
