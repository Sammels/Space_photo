import os
import requests
import datetime
from pathlib import Path
from urllib.parse import urlsplit
from dotenv import load_dotenv


def get_file_extension(url: str) -> str:
    """Function get http link and return file extension"""
    url = urlsplit(url)[2]
    template1 = os.path.splitext(url)
    file_link, *extension = template1
    return extension[0]


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


def sturtup_epic_script():
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    get_epic_earth_link_photo(token)


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    get_epic_earth_link_photo(token)
