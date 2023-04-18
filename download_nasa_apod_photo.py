import logging
import os
import requests

from pathlib import Path
from dotenv import load_dotenv

from python_utils import get_file_extension, download_image


API_NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"


def get_nasa_photos(api_url: str, token: str, count: int) -> list:
    """Take nasa token, API, count -> return links"""

    params = {"api_key": token, "count": count}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    photo_links = response.json()

    links = []
    for images_links in photo_links:
        if images_links.get("hdurl"):
            links.append(images_links.get("hdurl"))
    return links


if __name__ == "__main__":
    load_dotenv()
    ships_name = "Nasa_APOD"
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    nasa_links = get_nasa_photos(API_NASA_APOD_URL, token, 20)

    for number, link in enumerate(nasa_links):
        extension = get_file_extension(link)
        download_image(link, ships_name, number, extension)
    logging.debug("Function: download_images - Done")
