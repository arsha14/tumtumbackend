# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Bus(models.Model):
    nfc_id = models.IntegerField()
    bus_id = models.IntegerField()

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    tag_id = models.ForeignKey(Bus)
    updated_time = models.DateTimeField(auto_now = True)



# Create your models here.
