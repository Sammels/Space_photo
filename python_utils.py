import os
from urllib.parse import urlsplit


def get_file_extension(url: str) -> str:
    """Function get http link and return file extension"""
    url = urlsplit(url)[2]
    template1 = os.path.splitext(url)
    file_link, *extension = template1
    return extension[0]
