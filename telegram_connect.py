import os
import random
import argparse

import telegram
from dotenv import load_dotenv

from download_nasa_apod_photo import sturtup_apod_script
from download_nasa_epic_photo import sturtup_epic_script
from fetch_spacex_images import sturtup_spcacex_script


random_nubmer = random.randint(0,11)
chat_id = -1001838528455


parser = argparse.ArgumentParser(description="Программа скачивает файлы.")
parser.add_argument("-apod", "--nasa_apod", help="Скачивает с сайта NASA лучшие фото дня.")
parser.add_argument("-epic", "--nasa_epic", help="Скачивает ЭПИЧНЫХ маштабов фото")
parser.add_argument("-SpcX", "--spaceX", help="Скачивает фото запусков SpaceX")
args = parser.parse_args()

if args.nasa_apod == "NASA_APOD":
    sturtup_apod_script()
elif args.nasa_epic == "NASA_EPIC":
    sturtup_epic_script()
elif args.spaceX == "SPACEX":
    sturtup_spcacex_script()


def send_text(text: str) -> str:
    """Get text -> api telegram -> channel message"""
    bot.send_message(text=f'{text}', chat_id=chat_id)

def send_image(chats_id: int):
    """Get chat_id -> send docs to channels"""
    bot.send_document(chat_id=chats_id, document=open(f'images/ships_{random_nubmer}.jpeg', 'rb'))

if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_API_TOKEN']
    bot = telegram.Bot(token=telegram_token)
    updates = bot.get_updates()
    send_text_to_telegram = input("Текст который вы хотите отправить: ")
    send_text(send_text_to_telegram)
    send_image(chat_id)




