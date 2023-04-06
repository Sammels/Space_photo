import os
import requests
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv


def download_images(url) -> object:
    """Fucntion get url -> download img to path"""
    list_url = url
    for number, links in enumerate(list_url):
        response = requests.get(links)
        response.raise_for_status()
        extension = get_file_extension(links)
        with open(f"images/nasa_apod_{number}{extension}", "wb") as file:
            file.write(response.content)
    print("Download data = ok.")


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

    link_list = []
    for img_links in linked:
        link_list.append(img_links.get("hdurl"))
        if None in link_list:
            none_index = link_list.index(None)
            link_list.pop(none_index)
    return link_list


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    nasa_api = os.environ["APOD_NASA_API"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    nasa_link = get_nasa_photo(nasa_api, token, 20)
    download_images(nasa_link)
