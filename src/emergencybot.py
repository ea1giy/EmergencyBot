from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is just a test")


def emergencia(update, context):
    # Notificar emergencia a personal de guardia
    # Solo puede ser activado por los administradores del grupo
    context.bot.send_message(chat_id=update.effective_chat.id, text="Emergencia")


def cuadrante(update, context):
    # Menu para la modificación y consulta del cuadrante
    context.bot.send_message(chat_id=update.effective_chat.id, text="Cuadrante")


def modificar_cuadrante(update, context):
    # Sección para modificar los horarios del cuadrante.
    context.bot.send_message(chat_id=update.effective_chat.id, text="modificar cuadrante")


def consultar_cuadrante(update, context):
    # Consulta o descarga de cuadrante actual
    context.bot.send_message(chat_id=update.effective_chat.id, text="consultar cuadrante")


def main():
    updater = Updater(token='token', use_context=True)
    dp = updater.dispatcher

    # Registro de los diferentes comandos del bot.
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('emergencia', emergencia))
    dp.add_handler(CommandHandler('cuadrante', cuadrante))
    dp.add_handler(CommandHandler('Modificar', modificar_cuadrante))
    dp.add_handler(CommandHandler('Consultar', consultar_cuadrante))

    # Iniciar bot en modo temporizado
    updater.start_polling()
    updater.idle()

    # Iniciar bot en modo Webhooks


if __name__ == "__main__":
    main()
