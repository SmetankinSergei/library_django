from library_test_work.celery import app
from library.service import send_greeting


@app.task
def send_greeting_email(user_email):
    send_greeting(user_email)
