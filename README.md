<h1> Telegram parse members and add to your group with asyncio </h1>


# Как установить проект 
### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Dreamseller4u/TelegramParser.git
```
### Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
### Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### Запустить скрапинг пользоватлей:
```
python get_members_from_group.py
```
### Запустить добавление пользователей:
```
python add_membres_multi_sessions.py

```
### Добавить свои данные:
```
api_hash = ''
api_id = ''
phone = '' or main_account = ''
```
## Стек технологий: Python 3, Asyncio, Selenium, Telethon
## Автор проекта - Кочевых Никита