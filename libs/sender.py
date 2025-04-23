import requests

from core import settings


def send_tg_message(message: str):
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML',
    }
    response = requests.post(url, data=data)
    return response