# Generated by Django 4.2.2 on 2023-07-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0008_alter_mailinglog_attempt_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailings',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time of the ending'),
        ),
    ]
