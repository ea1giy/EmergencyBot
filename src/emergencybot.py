from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is just a test")


# Registro de los diferentes comandos del bot
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Comenzar actualizaciones del bot
updater.start_polling()

