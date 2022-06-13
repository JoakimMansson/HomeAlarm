import linecache
import re
import telepot

bot_token = re.sub("\n", "",linecache.getline("credentials", 11))

bot = telepot.Bot(bot_token)
bot.sendMessage(chat_id, "hej")
#bot.sendPhoto(chat_id, photo=open("Images/Active.png", "rb"))
bot.sendVideo(chat_id, video=open("videoplayback.mp4", "rb"))