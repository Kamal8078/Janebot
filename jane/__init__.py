from telethon import TelegramClient 
import logging
import time


openai_key= "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"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6264622656:AAGKBnT2mpnElZlQeQlIfu4WfkQC_WKlaeg"




bot = TelegramClient("jane",api_id,api_hash).start(bot_token = bot_token)