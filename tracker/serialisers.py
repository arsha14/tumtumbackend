# -*- coding: utf-8 -*-
from rest_framework import serializers
from tracker.models import Bus, Location

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        field = ('nfc_id', 'bus_id')

class LocationSerializer(serializers.ModelSerializer):
    bus = BusSerializer()
    class Meta:
        model = Location
        field = ('latitude', 'longitude', 'bus')
# Create your views here.
