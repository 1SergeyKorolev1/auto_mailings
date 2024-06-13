import smtplib
from datetime import datetime as dt

import pytz
from django.core.mail import send_mail
from django.core.management import BaseCommand

from config import settings
from mailings.models import Mailing, HistoryMailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = dt.now(zone)
        mailings = Mailing.objects.filter(status='запущена')
        print(f'\nКоличество рассылок для отправки: {mailings.count()}')
        print(f'Сейчас - {current_datetime}')
        for mailing in mailings:
            clients = mailing.clients.all()
            client_emails = [client.email for client in clients]
            print(f'Клиенты получатели - {client_emails}')
            try:
                response = send_mail(
                    mailing.message.theme,
                    mailing.message.body,
                    settings.EMAIL_HOST_USER,
                    client_emails,
                )
                HistoryMailing.objects.create(last_date=current_datetime,
                                              status=True,
                                              response=response, )
            except smtplib.SMTPException as e:
                print(f'Непредвиденная ошибка{e}')
                HistoryMailing.objects.create(last_date=current_datetime,
                                              status=False,
                                              response=str(e), )
