import smtplib

import pytz
from django.core.mail import send_mail
from django.core.management import BaseCommand
from config import settings
from datetime import datetime as dt

class Command(BaseCommand):

    def handle(self, *args, **options):
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
                    settings.EMAIL_HOST_USER,
                    client_emails,
                )
            except smtplib.SMTPException as e:
                print(f'Непредвиденная ошибка{e}')
                pass