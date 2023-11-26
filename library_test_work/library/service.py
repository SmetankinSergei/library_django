from django.core.mail import send_mail


def send_greeting(user_email):
    send_mail("new letter", "Greeting!!!", "library@gmail.com", [user_email], fail_silently=False)
