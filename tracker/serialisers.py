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



    def create(self, data):
        self.latitude = data["latitude"]
        self.longitude = data["longitude"]
        self.ID.bus_id = data["ID"]["bus_id"]
        self.ID.nfc_id = data["ID"]["nfc_id"]

# Create your views here.
