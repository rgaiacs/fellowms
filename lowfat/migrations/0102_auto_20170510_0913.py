# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


def set_inaugural_grant_expiration(apps, schema_editor):  # pylint: disable=unused-argument
    Claimant = apps.get_model("lowfat", "Claimant")  # pylint: disable=invalid-name
    for claimant in Claimant.objects.all():
        claimant.inauguration_grant_expiration = datetime.date(
            claimant.application_year + 2,
            3,
            31
            )
        claimant.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0101_auto_20170426_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimant',
            name='inauguration_grant_expiration',
            field=models.DateField(default=datetime.date(2019, 3, 31)),
        ),
        migrations.RunPython(set_inaugural_grant_expiration),
        migrations.AddField(
            model_name='historicalclaimant',
            name='inauguration_grant_expiration',
            field=models.DateField(default=datetime.date(2019, 3, 31)),
        ),
    ]
