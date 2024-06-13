import smtplib

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime as dt
import pytz
from django.conf import settings
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def sending_messages():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = dt.now(zone)
    from mailings.models import Mailing
    mailings = Mailing.objects.filter(status='запущена')
    print(f'\nКоличество рассылок для отправки: {mailings.count()}')
    print(f'Сейчас - {current_datetime}')
    for mailing in mailings:
        clients = mailing.clients.all()
        client_emails = [client.email for client in clients]
        print(f'Клиенты получатели - {client_emails}')
        try:
            send_mail(
                mailing.message.theme,
                mailing.message.body,
                EMAIL_HOST_USER,
                client_emails,
            )
        except smtplib.SMTPException as e:
            print(f'Непредвиденная ошибка{e}')
            pass


def start_apscheduler():
    print('Starting scheduler...')
    scheduler = BackgroundScheduler()
    if not scheduler.running:
        scheduler.add_job(sending_messages, 'interval', seconds=10)
        scheduler.start()
        print('Scheduler запущен успешно')


