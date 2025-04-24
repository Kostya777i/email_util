from celery import Celery
from config import REDIS_BROKER_URL
from email_utils import send_email

app = Celery("email_service", broker=REDIS_BROKER_URL)

@app.task
def send_email_task(to, subject, body):
    return send_email(to, subject, body)