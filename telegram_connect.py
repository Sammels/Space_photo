import os
import argparse
import random
import time

import telegram
from dotenv import load_dotenv


def walk_dir(path: str):
    """Use OS.Walk to take info about dir"""
    for root, dirs, files in os.walk(f"{path}"):
        dir_files = files
    file_choice = random.choice(dir_files)
    return file_choice


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_API_TOKEN']
    path = os.environ['DOWNLOAD_PATH']
    chat_id = os.environ['TELEGRAM_API_CHAT_ID']

    file = walk_dir(path)

    parser = argparse.ArgumentParser(description="Программа скачивает файлы.")
    parser.add_argument("-t", "--time", help="Пауза в отправке сообщений (час)",
                        type=int, default=4)
    args = parser.parse_args()

    while True:
        bot = telegram.Bot(token=telegram_token)
        updates = bot.get_updates()

        with open(f'images/{file}', 'rb') as f:
            bot.send_document(chat_id=chat_id, document=f)

        timeout = (args.time * 60) * 60
        time.sleep(timeout)
