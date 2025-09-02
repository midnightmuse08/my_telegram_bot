import telebot
from telebot import types

bot = telebot.TeleBot('7384494559:AAHff_7XSi3HA8Vifr3ZWJbOWvM5lkpvpmU')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '/start\n/help')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url='https://www.pinterest.com/'))
    bot.reply_to(message, "Какое красивое фото 😊. Давай предложу еще варианты: ", reply_markup=markup)

if __name__ == "__main__":
    bot.polling(non_stop=True)   # еще можно использовать infinity_polling