from pyrogram import client, filters


API_ID = "12490395"
API_HASH = "0fbaeeaa316d86ca04cbdb4e99a8ed89"
BOT_TOKEN = "8910912567:AAHMrG9ggZlMFs-mVzlp26HYRrW1nTNkyuE"

XpressBotz = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@XpressBotz.on_message(filters.command("start"))
async def start_cmd(client, message):
    print("START Command")


@XpressBotx.on_message(filters.command("help"))
async def help_cmd(client, message):
    print("HELP Command")


printf("Bot was Started")

XpressBotz.run()
