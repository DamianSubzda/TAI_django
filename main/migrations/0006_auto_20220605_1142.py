# Generated by Django 2.1.5 on 2022-06-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]