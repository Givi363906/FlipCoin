from colorama import Fore, Back, Style
import telebot
from random import randint
import config
import sys
import locale

print(sys.getfilesystemencoding())
print(locale.getpreferredencoding())

print(Fore.RED + 'Starting bot')

bot = telebot.TeleBot(config.TOKEN)

print(Fore.GREEN + 'Done')


# client
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуй, просто напиши мне /flip!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '/flip':
        bot.send_video(message.chat.id, 'https://i.gifer.com/789z.mp4')

        result = randint(1, 100)
        print("Вывод случайного целого числа ", result)

        send_result(message, result)

def send_result(message, result):
    if result <= 50:
        bot.send_message(message.chat.id, 'Орёл')
    elif result >= 50:
        bot.send_message(message.chat.id, 'Решка')


bot.polling()