# Generated by Django 5.0.3 on 2024-04-07 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 7, 15, 49, 35, 552005, tzinfo=datetime.timezone.utc))),
                ('is_open', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 15, 49, 35, 547019, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 15, 49, 35, 551008, tzinfo=datetime.timezone.utc)),
        ),
    ]
