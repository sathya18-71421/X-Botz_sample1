from pyrogram import client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "12490395"
API_HASH = "0fbaeeaa316d86ca04cbdb4e99a8ed89"
BOT_TOKEN = "8910912567:AAHMrG9ggZlMFs-mVzlp26HYRrW1nTNkyuE"

XpressBotz = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


START_BUTTONS = [[
    InlineKeyboardButton("JOIN MAIN CHANNEL TO CONTINUE", url="https://t.me/Xpressbotz_18")
]]


@XpressBotz.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://graph.org/file/9307a0d78149aab078f68-eb1387c03ebb4a1e35.jpg",
        caption="Hi💥,This is an active and powerful Bot and ready to assist you")







printf("Bot was Started")

XpressBotz.run()
