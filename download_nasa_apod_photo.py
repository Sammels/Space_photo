import logging
import os
import requests
import time

from pathlib import Path
from dotenv import load_dotenv

from python_utils import get_file_extension


API = "https://api.nasa.gov/planetary/apod"


def get_nasa_photo(api: str, token: str, count: int) -> list:
    """Take nasa token, API, count -> return links"""
    params = {"api_key": token, "count": count}
    response = requests.get(api, params=params)
    response.raise_for_status()
    photo_link = response.json()

    links = []
    for img_links in photo_link:
        links.append(img_links.get("hdurl"))
        if None in links:
            none_index = links.index(None)
            links.pop(none_index)
    return links


def download_images(url: str, number: int, extension: str) -> object:
    """Fucntion get url -> download img to path"""
    response = requests.get(url)
    response.raise_for_status()
    with open(f"images/nasa_apod_{number}{extension}", "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    start_time = time.time()
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    nasa_link = get_nasa_photo(API, token, 45)

    for number, link in enumerate(nasa_link):
        extension = get_file_extension(link)
        download_images(link, number, extension)
    logging.debug("Function: download_images - Done")
    end_time = time.time() - start_time
    print(end_time)