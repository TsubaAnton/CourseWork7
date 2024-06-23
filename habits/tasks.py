from celery import shared_task
from .models import Habit
import requests
from config import settings
import datetime
import json


@shared_task
def send_telegram_message():
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/"
    now = datetime.datetime.now()
    habits = Habit.objects.all()
    for habit in habits:
        if now.time() <= habits.time:
            print("Телеграм бот запущен")
            data1 = requests.get(url + "getupdates")
            data2 = json.loads(data1.content)
            chat_id = data2["result"][0]["message"]["chat"]["id"]
            requests.post(url+"sendMessage",
                          data={"chat_id": chat_id,
                                "text": f'В {habit.time} часов вы должны {habit.action} в {habit.place}'}
                          )
