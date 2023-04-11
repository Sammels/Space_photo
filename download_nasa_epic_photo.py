import logging
import os
import requests
import datetime
from pathlib import Path
from dotenv import load_dotenv

from python_utils import get_file_extension


def get_epic_earth_link_photo(token: str) -> str:
    """Take token, them return foto from nasa api"""
    epic_nasa_api = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": token}
    response = requests.get(epic_nasa_api, params=params)
    response.raise_for_status()
    url_links = response.json()

    for number, link in enumerate(url_links):
        image_name = link.get("image")
        image_create_date = link.get("date")
        image_create_date = str(datetime.datetime.fromisoformat(image_create_date).date()).split(sep="-")
        return_link = f"https://api.nasa.gov/EPIC/archive/natural/{image_create_date[0]}/{image_create_date[1]}/{image_create_date[2]}/png/{image_name}.png"
        extension = get_file_extension(return_link)
        response = requests.get(return_link, params=params)
        response.raise_for_status()
        with open(f"images/{image_name}_{number}{extension}", "wb") as file:
            file.write(response.content)
    logging.debug("Function: download_images - Done")


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    get_epic_earth_link_photo(token)
