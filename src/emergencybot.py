from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is just a test")


def emergencia():
    # Notificar emergencia a personal de guardia
    # Solo puede ser activado por los administradores del grupo
    pass


def cuadrante():
    # Menu para la modificación y consulta del cuadrante
    pass


def modificarCuadrante():
    # Sección para modificar los horarios del cuadrante.
    pass


def consultarCuadrante():
    # Consulta o descarga de cuadrante actual
    pass


# Registro de los diferentes comandos del bot
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Comenzar actualizaciones del bot
updater.start_polling()
updater.idle()

