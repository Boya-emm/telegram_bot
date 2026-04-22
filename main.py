import os
import asyncio
from telethon import TelegramClient, events

# 🔐 Get API from Environment (Render)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# 👉 Create client
client = TelegramClient("session", API_ID, API_HASH)

# 👉 Store last message
last_messages = {}

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # 👉 Only private chat
    if event.is_private and not event.is_group:
        user_id = event.sender_id

        # Save message id
        last_messages[user_id] = event.id

        # Wait 60 seconds
        await asyncio.sleep(60)

        # If user didn't reply
        if last_messages.get(user_id) == event.id:
            await event.reply("⏰ អ្នកមិនទាន់ reply ទេ")

# 👉 Run bot
async def main():
    await client.start()
    print("🤖 Bot is running 24/7...")
    await client.run_until_disconnected()

# 👉 Start program
asyncio.run(main())