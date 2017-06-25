# -*- coding: utf-8 -*-
from rest_framework import serializers
from tracker.models import Bus, Location

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    ID = BusSerializer()
    class Meta:
        model = Location
        fields = '__all__'
    

    loc = Location
    def create(self, loc):
        latitude = loc.latitude
        longitude = loc.longitude
        ID.bus_id = loc.ID.bus_id
        ID.nfc_id = loc.ID.nfc_id

# Create your views here.
