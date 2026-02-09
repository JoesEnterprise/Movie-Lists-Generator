# Discord Movie Bot

A Discord bot that suggests random movies from a database!

## Setup

### 1. Create Discord Bot Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" section and click "Add Bot"
4. Under TOKEN, click "Copy" and save your token
5. Enable these intents:
   - Message Content Intent
   - Server Members Intent (optional)

### 2. Create .env File
Copy `.env.example` to `.env` and add your Discord bot token:
```
DISCORD_TOKEN=your_actual_token_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python init_db.py
```

This will create `movies.db` with 10 sample movies.

### 5. Run the Bot
```bash
python bot.py
```

## Usage

In any Discord server where the bot is a member, use:
```
/suggest
```

The bot will respond with a random movie suggestion including:
- Title
- Description
- Genre
- Year
- Rating

## Add More Movies

Edit `init_db.py` or write a script to insert movies into the database:

```python
import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO movies (title, description, genre, year, rating)
    VALUES (?, ?, ?, ?, ?)
''', ("Movie Title", "Description", "Genre", 2024, 8.5))

conn.commit()
conn.close()
```

## Bot Permissions

When inviting the bot to your server, ensure it has these permissions:
- Send Messages
- Embed Links
- Read Messages/View Channels

Invite URL format:
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=0&scope=bot%20applications.commands
```

Replace `YOUR_BOT_ID` with your bot's ID from Developer Portal.
