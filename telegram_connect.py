import os
import argparse
import random
import time

import telegram
from dotenv import load_dotenv


load_dotenv()
path = os.environ['DOWNLOAD_PATH']
chat_id = os.environ['TELEGRAM_API_CHAT_ID']
telegram_token = os.environ['TELEGRAM_API_TOKEN']
bot = telegram.Bot(token=telegram_token)
updates = bot.get_updates()


while True:
    parser = argparse.ArgumentParser(description="Программа скачивает файлы.")
    parser.add_argument("-t", "--time", help="Временной промежуток для отправки сообщений (в часах).",
                        type=int, default=4)
    args = parser.parse_args()
    pause_time = (args.time * 60)*60

    for root, dirs, files in os.walk(f"{path}"):
        dir_files = files
    file = random.choice(dir_files)

    def send_text(text: str) -> str:
        """Get text -> api telegram -> channel message"""
        bot.send_message(text=f'{text}', chat_id=chat_id)

    def send_image(chat_id: int) -> str:
        """Get chat_id -> send docs to channels"""
        bot.send_document(chat_id=chat_id, document=open(f'images/{file}', 'rb'))

    send_image(chat_id)
    time.sleep(pause_time)


if __name__ == "__main__":
    load_dotenv()
    send_text_to_telegram = input("Текст который вы хотите отправить: ")
    telegram_token = os.environ['TELEGRAM_API_TOKEN']
    path = os.environ['DOWNLOAD_PATH']
    chat_id = os.environ['TELEGRAM_API_CHAT_ID']
    bot = telegram.Bot(token=telegram_token)
    updates = bot.get_updates()
    send_text(send_text_to_telegram)
    send_image(chat_id)
