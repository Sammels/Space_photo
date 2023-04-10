import os
import requests
from pathlib import Path
from dotenv import load_dotenv

LAUNCH_ID = "5eb87d46ffd86e000604b388"
SPACEX_API = "https://api.spacexdata.com/v5/launches/"

def fetch_spacex_last_launch(api: str, id_launch="latest") -> object:
    """Fucntion take api, and md5-hash launch -> download pict."""
    update_api = f"{api}{id_launch}"
    response = requests.get(update_api)
    response.raise_for_status()
    response_json = response.json()
    some_ship = response_json["links"]["flickr"]["original"]

    for number, links in enumerate(some_ship):
        response = requests.get(links)
        response.raise_for_status()
        with open(f"images/ships_{number}.jpeg", "wb") as file:
            file.write(response.content)
    print("Function: fetch_spacex_last_launch - Done")


def sturtup_spcacex_script():
    load_dotenv()
    api = os.environ["SPACEX_API"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(api)


if __name__ == "__main__":
    load_dotenv()
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(SPACEX_API, LAUNCH_ID)
