# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-15 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import lowfat.validator


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0081_auto_20161010_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='claim',
            field=models.FileField(upload_to='expenses/', validators=[lowfat.validator.pdf]),
        ),
        migrations.AlterField(
            model_name='fund',
            name='status',
            field=models.CharField(choices=[('U', 'Unprocessed'), ('P', 'Processing'), ('A', 'Approved'), ('R', 'Reproved'), ('F', 'Archived'), ('C', 'Canceled')], default='U', max_length=1),
        ),
    ]