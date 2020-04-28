import time
import os
from bot.bot import Bot
from dotenv import load_dotenv
from bot.handler import MessageHandler

load_dotenv()


def message_cb(bot, event):
    while True:
        bot.send_text(chat_id=event.from_chat, text='Выпрями спину и помой руки.')
        time.sleep(3600)


def main():
    bot = Bot(token=os.getenv("TOKEN"))
    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
