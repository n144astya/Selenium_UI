import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER_EMAIL = os.getenv("VALID_USER_EMAIL")
    USER_PASSWORD = os.getenv("VALID_USER_PASSWORD")

    if not USER_EMAIL:
        raise ValueError("ВНИМАНИЕ: USER_EMAIL не задан в переменных окружения или .env файле!")
    if not USER_PASSWORD:
        raise ValueError("ВНИМАНИЕ: VALID_USER_PASSWORD не задан в переменных окружения или .env файле!")