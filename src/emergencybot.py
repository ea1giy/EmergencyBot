from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is just a test")


def emergencia():
    # Notificar emergencia a personal de guardia
    # Solo puede ser activado por los administradores del grupo
    pass


def cuadrante():
    # Menu para la modificación y consulta del cuadrante
    pass


def modificar_cuadrante():
    # Sección para modificar los horarios del cuadrante.
    pass


def consultar_cuadrante():
    # Consulta o descarga de cuadrante actual
    pass


def main():
    updater = Updater(token='TOKEN', use_context=True)
    dp = updater.dispatcher

    # Registro de los diferentes comandos del bot.
    dp.add_handler(CommandHandler('start', start))

    # Iniciar bot en modo temporizado
    updater.start_polling()
    updater.idle()

    # Iniciar bot en modo Webhooks


if __name__ == "__main__":
    main()
