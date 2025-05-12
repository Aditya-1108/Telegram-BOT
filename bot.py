import telebot
import random
import math

bot = telebot.TeleBot('6525263853:AAEymeyvP04P-fJe0noQro-P8Xhe_gkgtwE')

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Hi! I'm your smart bot 🤖\nType /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help(msg):
    bot.reply_to(msg, """
Available commands:
/start - Start the bot
/help - List commands
/joke - Get a joke
/fact - Get a fact
/quote - Get a quote
/weather cityname - Mock weather info
/calculate [expression] - Simple calculator (e.g., 2+2)
/math [expression] - Advanced math operations (e.g., sqrt(16))
""")

@bot.message_handler(commands=['joke'])
def joke(msg):
    jokes = [
        "Why did the developer go broke? Because he used up all his cache.",
        "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'",
        "Why do Python devs wear glasses? Because they can't C."
    ]
    bot.reply_to(msg, random.choice(jokes))

@bot.message_handler(commands=['fact'])
def fact(msg):
    facts = [
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than a year on Venus."
    ]
    bot.reply_to(msg, random.choice(facts))

@bot.message_handler(commands=['quote'])
def quote(msg):
    quotes = [
        "Dream big. Work hard. Stay focused.",
        "The best way to predict the future is to invent it.",
        "Push yourself, because no one else is going to do it for you."
    ]
    bot.reply_to(msg, random.choice(quotes))

@bot.message_handler(commands=['weather'])
def weather(msg):
    try:
        city = msg.text.split(" ", 1)[1]
        bot.reply_to(msg, f"The weather in {city} is 25°C, sunny. ☀️ (mock)")
    except:
        bot.reply_to(msg, "Usage: /weather cityname")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(msg):
    text = msg.text
    if "calculate" in text.lower():
        try:
            expression = text.split(" ", 1)[1]
            result = eval(expression)
            bot.reply_to(msg, f"The result of {expression} is: {result}")
        except Exception as e:
            bot.reply_to(msg, f"Error: {str(e)}")
    
    elif "math" in text.lower() or any(op in text for op in ["sqrt", "**", "/", "+", "-", "*", "%"]):
        try:
            expression = text.replace("sqrt", "math.sqrt")  # Handle square root
            result = eval(expression)
            bot.reply_to(msg, f"The result of {expression} is: {result}")
        except Exception as e:
            bot.reply_to(msg, f"Error: {str(e)}")

bot.polling()
