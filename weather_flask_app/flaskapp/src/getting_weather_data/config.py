import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
REQUEST_HISTORICAL_DAILY = os.getenv('REQUEST_HISTORICAL_DAILY')
