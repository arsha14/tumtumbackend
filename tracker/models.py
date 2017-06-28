# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import requests


class Bus(models.Model):
    nfc_id = models.IntegerField()


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    bus = models.ForeignKey(Bus, default='')
    updated_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if kwargs.has_key('request'):
            response = requests.get("http://127.0.0.1:8000/?format=json")
            data = response.json()
            request = kwargs.pop('request')
            for addition in data:
                if addition["bus"]["nfc_id"] == request.bus.nfc_id:
                    self.bus = Bus.objects.get(addition["id"])
            #request = kwargs.pop('request')
            #self.ID = request.ID
        #if req.ID is None:  # Set default referenc
        super(Location, self).save(*args, **kwargs)
