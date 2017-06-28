# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import requests


class Bus(models.Model):
    nfc_id = models.IntegerField()


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    bus = models.ForeignKey(Bus, null=True)
    updated_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        response = requests.get("http://127.0.0.1:8000/?format=json")
        data = response.json()
        if kwargs.has_key('request'):
            request = kwargs.pop('request')
            for addition in data:
                if addition["bus"]["nfc_id"] == request.bus.nfc_id:
                    self.bus = Bus.objects.get(addition["id"])
        else:
            #self.bus = Bus.objects.get(data[0]["id"])   
            super(Location, self).save(*args, **kwargs)     


            #request = kwargs.pop('request')
            #self.ID = request.ID
        #if req.ID is None:  # Set default referenc
        super(Location, self).save(*args, **kwargs)
