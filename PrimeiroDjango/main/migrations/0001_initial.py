# Generated by Django 3.2.6 on 2021-09-04 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeusfilmesFavoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('resumo', models.TextField()),
                ('data', models.DateTimeField(default=datetime.datetime(2021, 9, 4, 8, 36, 40, 455741), verbose_name='Publicado em')),
            ],
        ),
    ]
