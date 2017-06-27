# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Bus(models.Model):
    nfc_id = models.IntegerField()
    bus_id = models.IntegerField()

    def __unicode__(self):
        return self

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    ID = models.ForeignKey(Bus, null=True)
    updated_time = models.DateTimeField(auto_now = True)


    def __unicode__(self):
        return self
    
    



# Create your models here.
