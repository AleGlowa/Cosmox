# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galaxy',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='planet',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='planetarysystem',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]