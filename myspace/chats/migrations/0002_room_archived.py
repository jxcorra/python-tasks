# Generated by Django 3.2.1 on 2021-05-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
