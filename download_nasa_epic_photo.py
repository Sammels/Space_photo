import os
import requests
from pathlib import Path
from dotenv import load_dotenv

from python_utils import get_file_extension


def get_epic_earth_link_photo(token: str) -> str:
    """Take token, them return foto from nasa api"""
    params = {"api_key": token}

    GET_AVAILABLE_EPIC_URL = "https://api.nasa.gov/EPIC/api/natural/available"
    response = requests.get(GET_AVAILABLE_EPIC_URL, params=params)
    response.raise_for_status()
    available_date = response.json()[-1]

    API_NASA_EPIC_LINK = f"https://api.nasa.gov/EPIC/api/natural/date/{available_date}"
    response = requests.get(API_NASA_EPIC_LINK, params=params)
    response.raise_for_status()
    url_links = response.json()

    for number, link in enumerate(url_links):
        image_name = link.get("image")
        image_create_date = link.get("date")
        year = image_create_date[:4]
        month = image_create_date[5:7]
        day = image_create_date[8:10]

        link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
        epic_response = requests.get(link, params=params)
        ext = get_file_extension(link)
        with open(f"images/{image_name}_{number}{ext}", "wb") as f:
            f.write(epic_response.content)


if __name__ == "__main__":
    load_dotenv()
    ships_name = "Nasa_EPIC"
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    get_epic_earth_link_photo(token)
