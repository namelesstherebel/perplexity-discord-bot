import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# Basic validation
if not DISCORD_TOKEN:
    print("⚠️  WARNING: DISCORD_TOKEN not found in environment!")
if not PERPLEXITY_API_KEY:
    print("⚠️  WARNING: PERPLEXITY_API_KEY not found in environment!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Perplexity API is OpenAI-compatible
perplexity_client = AsyncOpenAI(
    api_key=PERPLEXITY_API_KEY,
    base_url="https://api.perplexity.ai"
)

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.tree.command(name="ask", description="Ask Perplexity AI anything")
@app_commands.describe(query="Your question")
async def ask(interaction: discord.Interaction, query: str):
    await interaction.response.defer(thinking=True)
    
    try:
        response = await perplexity_client.chat.completions.create(
            model="sonar-pro",
            messages=[{"role": "user", "content": query}]
        )
        
        answer = response.choices[0].message.content
        
        # Discord has a 2000 character limit per message
        if len(answer) > 2000:
            chunks = [answer[i:i+1900] for i in range(0, len(answer), 1900)]
            for chunk in chunks:
                await interaction.followup.send(chunk)
        else:
            await interaction.followup.send(answer)
        
    except Exception as e:
        await interaction.followup.send(f"❌ Error: {str(e)}")

@bot.tree.command(name="research", description="Deep research on a topic (takes longer)")
@app_commands.describe(topic="Topic to research")
async def research(interaction: discord.Interaction, topic: str):
    await interaction.response.defer(thinking=True)
    
    try:
        response = await perplexity_client.chat.completions.create(
            model="sonar-deep-research",
            messages=[{"role": "user", "content": f"Conduct detailed research on: {topic}"}]
        )
        
        answer = response.choices[0].message.content
        
        if len(answer) > 2000:
            chunks = [answer[i:i+1900] for i in range(0, len(answer), 1900)]
            for chunk in chunks:
                await interaction.followup.send(chunk)
        else:
            await interaction.followup.send(answer)
        
    except Exception as e:
        await interaction.followup.send(f"❌ Error: {str(e)}")

if DISCORD_TOKEN:
    bot.run(DISCORD_TOKEN)
else:
    print("❌ Cannot run bot: DISCORD_TOKEN is missing.")
