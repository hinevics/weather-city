import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
PATH_DATASET = os.getenv('PATH_DATASET')
PATH_WEATHER_DATA = os.getenv('PATH_WEATHER_DATA')