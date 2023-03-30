import os
import requests
import datetime
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv

FILENAME = "hubble.jpeg"
LAUNCH_ID = "5eb87d46ffd86e000604b388"
HUBBLE_LINK = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"


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


def fetch_spacex_last_launch(api: str, id_launch: str) -> object:
    """Fucntion take api, and md5-hash launch -> download pict."""
    payload = {"": f"{id_launch}"}
    response = requests.get(api, params=payload)
    response.raise_for_status()
    response_json = response.json()
    response_json = response_json[20]
    some_ship = response_json["links"]["flickr"]["original"]

    for number, links in enumerate(some_ship):
        response = requests.get(links)
        with open(f"images/ships_{number}.jpeg", "wb") as file:
            file.write(response.content)
    print("Download ok")


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

    return link_list


def get_epic_earth_link_photo(token: str) -> str:
    """Take token, them return foto from nasa api"""
    epic_nasa_api = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": f"{token}"}
    response = requests.get(epic_nasa_api, params=params)
    response.raise_for_status()
    link = response.json()

    for number, links in enumerate(link):
        image_name = links.get("image")
        image_create_date = links.get("date")
        image_create_date = str(datetime.datetime.fromisoformat(image_create_date).date()).split(sep="-")
        return_link = f"https://api.nasa.gov/EPIC/archive/natural/{image_create_date[0]}/{image_create_date[1]}/{image_create_date[2]}/png/{image_name}.png"
        extension = get_file_extension(return_link)
        response = requests.get(return_link, params=params)
        response.raise_for_status()
        with open(f"images/{image_name}_{number}{extension}", "wb") as file:
            file.write(response.content)
    print("Function: get_epic_earth_link_photo - Done ")


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    nasa_api = os.environ["NASA_API"]
    api = os.environ["API"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    download_images(get_nasa_photo(nasa_api, token, 20))
    get_epic_earth_link_photo(token)
