import logging
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

LAUNCH_ID = "5eb87d46ffd86e000604b388"
API_SPACEX_LAUNCHES = "https://api.spacexdata.com/v5/launches/"


def fetch_spacex_last_launch(id_launch="latest") -> object:
    """Fucntion take api, and md5-hash launch -> download pict."""
    api_adress = f"{API_SPACEX_LAUNCHES}{id_launch}"
    response = requests.get(api_adress)
    response.raise_for_status()
    response = response.json()
    some_ship = response["links"]["flickr"]["original"]

    for number, link in enumerate(some_ship):
        response = requests.get(link)
        response.raise_for_status()
        with open(f"images/ships_{number}.jpeg", "wb") as file:
            file.write(response.content)
    logging.debug("Function: fetch_spacex_last_launch - Done")


if __name__ == "__main__":
    load_dotenv()
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(LAUNCH_ID)
