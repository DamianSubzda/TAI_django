# Generated by Django 2.1.5 on 2022-06-03 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_song_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='Logo',
        ),
    ]