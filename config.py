import os
from dotenv import load_dotenv



load_dotenv()

# FOR TELEGRAM_API
TELEGRAM_BOT_API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')
WEBHOOK_URL_PATH = f'/{TELEGRAM_BOT_API_TOKEN}/'


TELEGRAM_GROUP_CHAT_ID = os.getenv('TELEGRAM_GROUP_CHAT_ID')
