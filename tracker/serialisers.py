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



    def create(self, validated_data):
        ID_data = validated_data.pop('ID')
        location = Location.objects.create(**validated_data)
        Bus.objects.create(location=location, **ID_data)
        return location
    #    loc = self.Meta.Location
    #    self.Meta.Location.create_loc(loc, data)
    #    self = Location
    #    self.latitude = validated_data["latitude"]
    #    self.longitude = validated_data["longitude"]
    #    self.ID.bus_id = validated_data["ID"]["bus_id"]
    #    self.ID.nfc_id = validated_data["ID"]["nfc_id"]
    #    return self

# Create your views here.
