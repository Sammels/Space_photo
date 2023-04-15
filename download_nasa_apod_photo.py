import logging
import os
import requests
import time

from pathlib import Path
from dotenv import load_dotenv

from python_utils import get_file_extension, download_image


API_NASA_APOD_PHOTO = "https://api.nasa.gov/planetary/apod"


def get_nasa_photos(api: str, token: str, count: int) -> list:
    """Take nasa token, API, count -> return links"""

    params = {"api_key": token, "count": count}
    response = requests.get(api, params=params)
    response.raise_for_status()
    link_photos = response.json()

    links = []
    for images_links in link_photos:
        if None in links:
            none_index = links.index(None)
            links.pop(none_index)
        links.append(images_links.get("hdurl"))
    return links


if __name__ == "__main__":
    load_dotenv()
    ships_name = "Nasa_APOD"
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    nasa_link = get_nasa_photos(API_NASA_APOD_PHOTO, token, 10)

    for number, link in enumerate(nasa_link):
        extension = get_file_extension(link)
        download_image(link, ships_name, number, extension)
    logging.debug("Function: download_images - Done")
