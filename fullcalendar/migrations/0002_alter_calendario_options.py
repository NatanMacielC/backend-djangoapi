# Generated by Django 3.2.6 on 2021-08-17 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendario',
            options={'ordering': ['tipo']},
        ),
    ]
