import logging
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

from python_utils import get_file_extension, download_image

LAUNCH_ID = "5eb87d46ffd86e000604b388"
API_SPACEX_LAUNCHES = "https://api.spacexdata.com/v5/launches/"


def fetch_spacex_last_launch(launch_id="latest") -> object:
    """Fucntion take api, and md5-hash launch -> download pict."""
    ships_name = "SpaceX"
    api_address = f"{API_SPACEX_LAUNCHES}{launch_id}"
    response = requests.get(api_address)
    response.raise_for_status()
    response = response.json()
    some_ship = response["links"]["flickr"]["original"]


    for number, link in enumerate(some_ship):
        ext = get_file_extension(link)
        download_image(link, ships_name, number, ext)
    logging.debug("Function: fetch_spacex_last_launch - Done")


if __name__ == "__main__":
    load_dotenv()
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(LAUNCH_ID)
