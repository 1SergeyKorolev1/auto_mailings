from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}
PERIODICITY_DATA = {
    'раз в день': 'день',
    'раз в неделю': 'неделя',
    'раз в месяц': 'месяц'
}
STATUS_DATA = {
    'завершена': 'завершена',
    'создана': 'создана',
    'запущена': 'запущена',
}

class MailingMessage(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема письма')
    body = models.CharField(max_length=150, verbose_name='тело письма')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.theme}'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text='укажите владельца', verbose_name='владелец',
                              **NULLABLE)

    class Meta:
        verbose_name = 'Сообщение рассылки'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Сообщения рассылки'  # Настройка для наименования набора объектов

class RecipientClient(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=150, verbose_name='ф.и.о')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text='укажите владельца', verbose_name='владелец',
                              **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'Клиент получатель'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Клиенты получатели'  # Настройка для наименования набора объектов
        permissions = [
            ('can_edit_email', 'Can edit email'),
            ('can_edit_full_name', 'Can edit full_name'),
            ('can_edit_comment', 'Can edit comment')
        ]

class Mailing(models.Model):
    first_date = models.DateField(verbose_name='дата первой отправки. Формат: 2024-06-13')
    periodicity = models.CharField(choices=PERIODICITY_DATA, verbose_name='периодичность')
    check_periodicity = models.IntegerField(default='0', verbose_name='дней до следующей отправки')
    status = models.CharField(choices=STATUS_DATA, default='создана', verbose_name='статус', **NULLABLE)
    message = models.ForeignKey(MailingMessage, on_delete=models.SET_NULL, verbose_name='сообщение', **NULLABLE)
    clients = models.ManyToManyField(RecipientClient, verbose_name='клиенты')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text='укажите владельца', verbose_name='владелец',
                              **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'рассылка стартовала {self.first_date}'

    class Meta:
        verbose_name = 'Рассылка'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Рассылки'  # Настройка для наименования набора объектов
        permissions = [
            ('can_edit_status', 'Can edit status'),
            ('can_edit_periodicity', 'Can edit periodicity'),
            ('can_edit_clients', 'Can edit clients')
        ]

class HistoryMailing(models.Model):
    last_date = models.DateField(verbose_name='дата последней попытки')
    status = models.BooleanField(verbose_name='статус успешно/нет')
    response = models.CharField(verbose_name='ответ почтового сервера')


