# Космический Телеграм

Проект скачивает фотографии используя API. Скачивание происходит с сайтов `NASA`, `SpaceX`.

---
## Файлы окружения

В файл `.env` нужно прописать
```commandline
TELEGRAM_API_TOKEN="Токен телеграма."
TELEGRAM_API_CHAT_ID=ID чата для отправки сообщений.
NASA_API_TOKEN="Токен с сайта НАСА"
DOWNLOAD_PATH="Путь к файлу."
```



---
## Описание функций в проекте.

----
### 1. download_nasa_apod_photo - Скачивает фото дня с сайта NASA.
1. `download_images` - Функция принимает список URL, переходит, скачивает файлы в папку.
2. `get_file_extension` - Принимает URL картинки, и возвращает расширение файла типа: `.jpg, .jpeg, .gif, .png`
3. `get_nasa_photo` - Принимает API-ключ, персональный токен, количество фоток. Возвращает список ссылок на фото. 
4. `sturtup_apod_script` - Функция написана, для того, чтобы скрипт мог быть вызван в других функциях.

Пример запуска:
```bash
python download_nasa_apod_photo.py

Output:
Function: download_images - Done
```

---
### 2. download_nasa_epic_photo - Скачивает ЭПИЧЕСКИЕ фотографии планеты, с сайта NASA.
1. `get_file_extension` - Аналогично из функции выше.
2. `get_epic_earth_link_photo` - Принимает токен, скачивает фото в папку.
3. `sturtup_epic_script` - Функция написана, для того, чтобы скрипт мог быть вызван в других функциях.

Пример запуска:
```bash
python download_nasa_epic_photo.py  

Output:
Function: get_epic_earth_link_photo - Done 
```

---
### 3. fetch_spacex_images - Используя токен, апи. Скачивает фото запуска ракеты в космос.
1. `fetch_spacex_last_launch` - Принимает API и ID запуска типа `5eb87d46ffd86e000604b388`
2. `sturtup_spcacex_script` -  Функция написана, для того, чтобы скрипт мог быть вызван в других функциях.

Пример запуска:
```bash
python fetch_spacex_images.py

Output:
Function: fetch_spacex_last_launch - Done
```

---

### 4. telegram_connect - Используется для отправки сообщений в телеграм.
Скрипт загружается из командной строки типа
```bash
python telegram_connect.py
```

Справка вызывается
```bash
python telegram_connect.py -h
```

1. `send_text` - Функция принимет текст, и отправляет его по chat_id
2. `send_image` - Принимает chat_id. после чего перебет рандомную фотографию из папки, и отправляет в телеграмм

По умолчанию временная задержка установлена на `пост картинки раз в 4 часа.`

---
### Как установить

Библиотеки которые необходимо установить

```
requests
python-telegram-bot==13
python-dotenv
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).