import telebot
import openai
from Keys import KEY, telegram_token


telegram_key = telegram_token
openai.api_key = KEY
bot = telebot.TeleBot(telegram_key)


@bot.message_handler(commands=['start'])
def Hello(message):
    bot.send_message(message.chat.id, 'Привет, я Виртуальный помощник Grace.')


@bot.message_handler(content_types=['text'])
def main(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt = message.text,
        max_tokens = 500,
        temperature = 0.5,
        n = 1,
        stop = None
    )

    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = 'Что то пошло не так'

    bot.send_message(message.chat.id, reply)


bot.polling(none_stop=True)


