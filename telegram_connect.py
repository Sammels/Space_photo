import os
import telegram
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.environ['TELEGRAM_API_TOKEN']
bot = telegram.Bot(token=telegram_token)
chat_id = -1001838528455

print(bot.get_me())
updates = bot.get_updates()
bot.send_message(text='Hi John!', chat_id=chat_id)

bot.send_document(chat_id=chat_id, document=open('images/ships_1.jpeg', 'rb'))