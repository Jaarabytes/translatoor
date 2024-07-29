import os   
import re
import telebot 
from deep_translator import GoogleTranslator
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')
print(f'your api key is {API_KEY}')
# Assume you've loaded your API key
bot = telebot.TeleBot(API_KEY, parse_mode=None)

# Fetch ISO 639-1 language codes
def fetch_language_codes():
    url = "https://gist.githubusercontent.com/piraveen/fafd0d984b2236e809d03a0e306c8a4d/raw/4258894f85de7752b78537a4aa66e027090c27ad/languages.json"
    response = requests.get(url)
    if response.status_code == 200:
        return {lang['name'].lower(): lang['code'] for lang in response.json()}
    else:
        return {}

LANGUAGE_CODES = fetch_language_codes()

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    # Regular expression to match @{language} {text}
    match = re.match(r'@(\w+)\s+(.*)', message.text, re.DOTALL)
    
    if not match:
        bot.reply_to(message, "Please use the format: @{language} {text to translate} eg @english Habari yako")
        return

    target_language = match.group(1).lower()
    text_to_translate = match.group(2)

    # Find the language code
    target_code = None
    for lang, code in LANGUAGE_CODES.items():
        if target_language in lang:
            target_code = code
            break

    if not target_code:
        bot.reply_to(message, f"Sorry, I couldn't find a language code for '{target_language}'")
        return

    try:
        translator = GoogleTranslator(source='auto', target=target_code)
        translated_text = translator.translate(text_to_translate)
        bot.reply_to(message, translated_text)
    except Exception as e:
        bot.reply_to(message, f"Translation error: {str(e)}")

bot.infinity_polling()
