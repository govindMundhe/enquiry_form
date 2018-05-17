# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('owner_name', models.CharField(max_length=200)),
                ('internet', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20)),
                ('Waiting', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20)),
                ('sms', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20)),
                ('demo', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=20)),
                ('demo_date', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=10)),
                ('soft_ava', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=20)),
                ('details', models.TextField(max_length=100)),
            ],
        ),
    ]