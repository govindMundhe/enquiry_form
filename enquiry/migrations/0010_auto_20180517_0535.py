# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0009_auto_20180514_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='Waiting',
            new_name='waiting',
        ),
    ]