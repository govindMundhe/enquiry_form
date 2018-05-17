# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
from django.utils import timezone


# Create your models here.
class Enquiry(models.Model):
    CHOICES = (
        ('Y', 'YES'),
        ('N', 'NO'),
    )
    SCALE = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    hotel_name = models.CharField(max_length=200)
    address = models.TextField(max_length = 200)
    owner_name = models.CharField(max_length=200)
    internet = models.CharField(max_length = 20,choices=CHOICES)
    waiting = models.CharField(max_length = 20,choices=CHOICES)
    sms = models.CharField(max_length = 20,choices=CHOICES)
    demo = models.CharField(max_length =20,choices=CHOICES)
    demo_date = models.DateField(default = timezone.now, blank=True)
    phone = models.CharField(max_length=10)
    existing_software = models.CharField(max_length=20,choices=CHOICES)


    def __str__(self):
        return 'Name: {} '.format(self.hotel_name)