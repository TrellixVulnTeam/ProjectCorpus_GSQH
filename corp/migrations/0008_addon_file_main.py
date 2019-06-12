# Generated by Django 2.2.2 on 2019-06-12 17:12

import corp.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0007_auto_20190612_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='file_main',
            field=models.FileField(default=django.utils.timezone.now, upload_to=corp.models.addon_main_path, verbose_name='Файл-драйвер'),
            preserve_default=False,
        ),
    ]