# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='demo',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20),
        ),
    ]
