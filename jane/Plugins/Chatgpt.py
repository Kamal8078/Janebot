from telethon import events
from .. import bot
from .. import openai_key
import asyncio
import openai

openai.api_key = openai_key


@bot.on(events.NewMessage(incoming=True,
  pattern="(?i)/ask"))
async def _chatgpt(event):
 if event.sender_id==int(5651553879):
  await event.reply("Hello! you are my devloper you developed me very well") 
 else:
   await event.reply("you are user: Nice to meet you")