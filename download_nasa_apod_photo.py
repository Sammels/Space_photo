import os
import requests
import time
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv

API = "https://api.nasa.gov/planetary/apod"


def get_file_extension(url: str) -> str:
    """Function get http link and return file extension"""
    url = urlsplit(url)[2]
    template1 = os.path.splitext(url)
    file_link, *extension = template1
    return extension[0]


def get_nasa_photo(api: str, token: str, count: int) -> list:
    """Take nasa token, API, count -> return links"""
    params = {"api_key": f"{token}", "count": f"{count}"}
    response = requests.get(api, params=params)
    response.raise_for_status()
    linked = response.json()

    links = []
    for img_links in linked:
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


def sturtup_apod_script():
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    nasa_link = get_nasa_photo(API, token, 30)

    for number, link in enumerate(nasa_link):
        extension = get_file_extension(link)
        download_images(link, number, extension)
    print("Function: download_images - Done")


if __name__ == "__main__":
    load_dotenv()
    start_time = time.time()

    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    nasa_link = get_nasa_photo(API, token, 30)

    for number, link in enumerate(nasa_link):
        extension = get_file_extension(link)
        download_images(link, number, extension)
    print("Function: download_images - Done")

    end_time = time.time() - start_time
    print(end_time)
