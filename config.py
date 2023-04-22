import os

import redis
from dotenv import load_dotenv

load_dotenv()

# FOR TELEGRAM_API
TELEGRAM_BOT_API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')
WEBHOOK_URL_PATH = f'/{TELEGRAM_BOT_API_TOKEN}/'

TELEGRAM_GROUP_CHAT_ID = os.getenv('TELEGRAM_GROUP_CHAT_ID')
PASSWORD_FOR_ADMIN = os.getenv('PASSWORD_FOR_ADMIN')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REDIS = redis.Redis(host='localhost', port=6379, db=0)
