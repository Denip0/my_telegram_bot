import telebot 
import requests


token = "1303784307:AAGlce7csEvLoP6OiRPaWU9iDqCs07q8rPw"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_bot(massage):
    msg = "Some voluts -> /valute \nWeather -> /weather"
    bot.send_message(massage.chat.id, f"Welcome {massage.from_user.first_name}. It's my first telegram bot.\n{msg}")

@bot.message_handler(commands=["valute"])
def get_valute(message):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    currency = requests.get(url).json()
    usd = currency['Valute']['USD']["Value"]
    eur = currency['Valute']['EUR']["Value"]
    bot.send_message(message.chat.id, f"Dollar: {usd}, Euro {eur}.")

@bot.message_handler(regexp="стикер")   
def send_sticker(message):
    id = 'CAACAgIAAxkBAAEBHMNfIFzETWHWGIkAAdaTYQABA7k_46PUAAKbDQACoKYKCpCuyIkxXtA7GgQ'
    bot.send_sticker(message.chat.id, id)
data = ['hello', 'hi', 'привет', 'йоу', 'здравствуйте']

@bot.message_handler(commands=['weather'])
def get_city(message):
    msg = bot.send_message(message.chat.id, "City?")
    bot.register_next_step_handler(msg, get_weather)


def get_weather(message):
    city = message.text
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c476f22a5b257b9d84b96dbf18ad854'
    data = requests.get(url).json()
    bot.send_message(message.chat.id, f"{city} - {(data['main']['temp'] - 273.15) // 1 }")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text.lower() in data: 
            bot.send_message(message.chat.id, 'Hi.')
        else:
            bot.send_message(message.chat.id, f'{message.text}? What is that?')
bot.polling()
