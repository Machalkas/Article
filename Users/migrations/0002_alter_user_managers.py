# Generated by Django 4.0.2 on 2022-02-08 15:10

import Users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', Users.models.Manager()),
            ],
        ),
    ]