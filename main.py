from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


TOKEN = '1630917550:AAHGRtXdVE9j5WANyEulzqOEn4aZY6DqV5A'


def main():
    updater = Updater(token=TOKEN)    # объект, который ловит сообщения из телеграм

    dispatcher = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)   # отфильтровываем сообщения: теперь устройство должно реагировать
    start_handler = CommandHandler('start',do_start)
    help_handler = CommandHandler('help',do_help)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
    updater.help_polling()

def do_echo(update, context):
    update.message.reply_text(text='ААААА!')

def do_start(update, context):
    update.message.reply_text(text="Я - бот") #  ответ на сообщение

def do_help(update: Update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    update.message.reply_text(text=f'Привет, {name}!\nТвой user_id: {user_id}.\nЧем тебе помочь?')

main()
