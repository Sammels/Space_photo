import os
from urllib.parse import urlsplit

import requests

def get_file_extension(url: str) -> str:
    """Function get http link and return file extension"""
    url = urlsplit(url)[2]
    template1 = os.path.splitext(url)
    file_link, *extension = template1
    return extension[0]

def download_image(url: str, name: str, number: int, extension: str) -> object:
    """Fucntion get url -> download img to path"""
    response = requests.get(url)
    response.raise_for_status()
    with open(f"images/{name}_{number}{extension}", "wb") as file:
        file.write(response.content)
