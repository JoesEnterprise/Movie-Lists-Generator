import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Database connection
def get_random_movie():
    """Fetch a random movie from the database"""
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM movies")
        count = cursor.fetchone()[0]
        
        if count == 0:
            return None
        
        random_id = random.randint(1, count)
        cursor.execute("SELECT * FROM movies WHERE id = ?", (random_id,))
        movie = cursor.fetchone()
        conn.close()
        return movie
    except Exception as e:
        print(f"Database error: {e}")
        return None

@bot.event
async def on_ready():
    """Called when the bot is ready"""
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="suggest", description="Get a random movie suggestion")
async def suggest(interaction: discord.Interaction):
    """Slash command to get a random movie suggestion"""
    movie = get_random_movie()
    
    if not movie:
        await interaction.response.send_message("No movies in the database! Add some movies first.")
        return
    
    movie_id, title, description, genre, year, rating = movie
    
    # Create an embed for better formatting
    embed = discord.Embed(
        title="🎬 Movie Suggestion",
        description=description,
        color=discord.Color.purple()
    )
    embed.add_field(name="Title", value=title, inline=False)
    embed.add_field(name="Genre", value=genre, inline=True)
    embed.add_field(name="Year", value=year, inline=True)
    embed.add_field(name="Rating", value=f"⭐ {rating}/10", inline=True)
    
    await interaction.response.send_message(embed=embed)

if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        print("ERROR: DISCORD_TOKEN not found in .env file!")
        exit(1)
    bot.run(TOKEN)
