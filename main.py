from pyrogram import client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

XpressBotz = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


printf("Bot was Started")

XpressBotz.run()
