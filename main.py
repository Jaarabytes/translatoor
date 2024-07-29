# yes, i'm building a telegram bot; bye!
import os
from dotenv import load_dotenv
import telebot
from deep_translator import GoogleTranslator
load_dotenv()

# Obtain your api key from botfather
API_KEY = os.getenv('API_KEY')
print(f'Api key is {API_KEY}')
bot = telebot.TeleBot(API_KEY, parse_mode=None)
# It's just an API call dummy
translator = GoogleTranslator(source='auto', target='en')

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    original_text = message.text   
    try:
        translated = translator.translate(original_text)
        bot.reply_to(message, translated)
    except Exception as e:
        bot.reply_to(message, f"Translation error: {str(e)}")

bot.infinity_polling()
