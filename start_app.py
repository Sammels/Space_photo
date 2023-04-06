import argparse

from download_nasa_apod_photo import sturtup_apod_script
from download_nasa_epic_photo import sturtup_epic_script
from fetch_spacex_images import sturtup_spcacex_script

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
