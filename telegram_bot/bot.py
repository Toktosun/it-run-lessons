from telebot import TeleBot  # это мы импортируем из скачанной нами библиотеки


TELEGRAM_TOKEN = '2141610501:AAHB0pfaVeiVG_2_vtHmtEk5yf7TsyY5dCI'

# TeleBot - класс
# bot - экземпляр или объект
bot = TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def react_to_start_command(message):
    bot.reply_to(message,
                 f'Приветствую мой {message.from_user.first_name}!'
                 f' Это я ваш первый бот.')


@bot.message_handler(content_types='text')  # обрабатывай все сообщения
def react_to_message_text(message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'И тебе привет.')
    elif message.text.lower() == 'пока':
        bot.reply_to(message, 'До свидания!!!')


@bot.message_handler(content_types='text')
def react_echo_message(message):
    bot.reply_to(message, f'{message.text}')



bot.polling()





