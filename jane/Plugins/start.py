from .. import bot,openai_key
from telethon import events
import asyncio
import openai


openai.my_api_key= "openapi_key"

@bot.on(events.NewMessage(incoming= True,pattern="/start"))
async def start(event):
  await event.reply("Hello this is jane bot")
  
  
@bot.on(events.NewMessage(incoming= True,pattern="/get"))
async def start(event):
  a=await event.reply("Hello this is get command")
  await asyncio.sleep(3)
  await a.edit("this is edited a msg")
  
  
@bot.on(events.NewMessage(incoming= True,pattern="/eval"))
async def start(event):
  await event.reply("Hello this is eval command") 
  
  
  