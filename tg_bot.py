import telebot
import main


bot = telebot.TeleBot('1565307869:AAFrtBKlHQ9YUElL93Iw8LflqqkVD__7Nmo')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');