# Generated by Django 5.0.4 on 2024-06-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0003_alter_mailing_first_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='first_date',
            field=models.DateField(verbose_name='дата первой отправки. Формат: 2024-06-13'),
        ),
    ]
