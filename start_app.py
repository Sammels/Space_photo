"""
Задача.
1. запускается скрипт
2. Принимает параметры
"""
import argparse

parser = argparse.ArgumentParser(description="Программа скачивает файлы.")
parser.add_argument("--nasa_apod", help="Скачивает с сайта NASA лучшие фото дня.")
args = parser.parse_args()
print(args)


if __name__ =="__main__":
    print("hi")