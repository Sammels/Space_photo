import logging
import os
import requests
import datetime
from pathlib import Path
from dotenv import load_dotenv



def get_epic_earth_link_photo(token: str) -> str:
    """Take token, them return foto from nasa api"""
    epic_nasa_api = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": token}
    response = requests.get(epic_nasa_api, params=params)
    response.raise_for_status()
    url_links = response.json
    print(url_links)

    # for number, link in enumerate(url_links):
    #     image_name = link.get("image")
    #     image_create_date = link.get("date")
    #     image_create_date = datetime.datetime.fromisoformat(image_create_date).date()
    #     year = image_create_date.year
    #     month = image_create_date.month
    #     day = image_create_date.day
    #     return_link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
    #     epic_response = requests.get(return_link, params=params)
    #     response.raise_for_status()
    #     with open(f"images/{image_name}_{number}.png", "wb") as file:
    #         file.write(epic_response.content)
    # logging.debug("Function: download_images - Done")


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    download_path = os.getenv("DOWNLOAD_PATH")
    Path(download_path).mkdir(parents=True, exist_ok=True)
    get_epic_earth_link_photo(token)
