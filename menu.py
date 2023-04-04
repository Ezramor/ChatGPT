import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    keyboard = [[InlineKeyboardButton("Добывать руду", callback_data='start_mining')],
                [InlineKeyboardButton("Мои задания", callback_data='my_tasks')],
                [InlineKeyboardButton("Мои достижения", callback_data='my_achievements')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Добро пожаловать в Горный квест! Выберите действие:', reply_markup=reply_markup)

def main():
    updater = Updater(token='6189827721:AAHRGQmQXYzZMHp8TXuZX9M_9yBeo_O_DYs', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
