# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0040_auto_20160720_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fellow',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lowfat.Fellow'),
            preserve_default=False,
        ),
    ]
