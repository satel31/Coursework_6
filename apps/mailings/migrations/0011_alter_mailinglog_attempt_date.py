# Generated by Django 4.2.2 on 2023-07-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0010_alter_mailings_clients_alter_mailings_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglog',
            name='attempt_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of the last attempt'),
        ),
    ]