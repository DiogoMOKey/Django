# Generated by Django 4.1.2 on 2022-10-15 11:43

import FoxSports.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('team1', models.CharField(max_length=20)),
                ('team2', models.CharField(max_length=20)),
                ('number_tickets', models.IntegerField(default=1)),
                ('game_finished', models.BooleanField(default=False)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='qrcode')),
            ],
        ),
        migrations.CreateModel(
            name='Game_Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('NO', 'Normal'), ('CL', 'Clients'), ('UR', 'Urgent')], default='NO', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('n_tickets', models.IntegerField(default=1)),
                ('invite_code', models.CharField(default=FoxSports.models.generate_unique_code, max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=8, unique=True)),
                ('seats_capacity', models.IntegerField(default=3000)),
                ('localitation', models.TextField(max_length=20, unique=True)),
                ('open', models.BooleanField(default=True)),
                ('photo', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aceite', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
