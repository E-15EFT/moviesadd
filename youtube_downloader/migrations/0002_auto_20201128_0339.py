# Generated by Django 3.1.3 on 2020-11-27 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_downloader', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YoutubeRecords',
            new_name='YoutubeRecord',
        ),
    ]