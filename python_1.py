import telebot 
import requests


token = "1303784307:AAGlce7csEvLoP6OiRPaWU9iDqCs07q8rPw"
bot = telebot.TeleBot(token)
@bot.message_handler(regexp="Hello")
def say_hello(massage):
    
    bot.send_message(massage.chat.id, f"Hello, {massage.from_user.first_name}. Could you print /start for beginnig?")

@bot.message_handler(commands=["start"])
def start_bot(massage):
    msg = "Some voluts -> /valute \nWeather -> /weather"
    bot.send_message(massage.chat.id, f"Welcome. It's my first telegram bot.\n{msg}")
@bot.message_handler(commands=["valute"])
def get_valute(massage):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    currency = requests.get(url).json()
    usd = currency['Valute']['USD']["Value"]
    eur = currency['Valute']['EUR']["Value"]
    bot.send_message(massage.chat.id, f"Dollar: {usd}, Euro {eur}.")

@bot.message_handler(regexp="стикер")
def send_sticker(massage):
    id = 'CAACAgIAAxkBAAEBHMNfIFzETWHWGIkAAdaTYQABA7k_46PUAAKbDQACoKYKCpCuyIkxXtA7GgQ'
    bot.send_sticker(massage.chat.id, id)

@bot.message_handler(commands='weather')
def get_city(massage):
    msg = bot.send_message(massage.chat.id, "City?")
    bot.register_next_step_handler(msg, get_weather)

def get_weather(massage):
    city = massage.text
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c476f22a5b257b9d84b96dbf18ad854'
    data = requests.get(url).json()
    bot.send_message(massage.chat.id, f"{city} - {(data['main']['temp'] - 273.15) // 1 }")




bot.polling()
