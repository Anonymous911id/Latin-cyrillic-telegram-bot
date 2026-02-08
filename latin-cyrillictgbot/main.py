from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = 'Your TOKEN'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply = "Hello, Welcome!\nEnter text"
    bot.reply_to(message, reply)


@bot.message_handler(func=lambda message: True)
def transli(message):
    msg = message.text
    reply = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, reply(msg))

bot.polling()
