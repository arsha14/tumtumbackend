# -*- coding: utf-8 -*-
from rest_framework import serializers
from tracker.models import Bus, Location

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    bus = BusSerializer(required = False)
    class Meta:
        model = Location
        fields = '__all__'



    def create(self, validated_data):
        bus_data = validated_data.pop('bus')
        location = Location.objects.create(**validated_data)
        Bus.objects.create(location=location, **bus_data)
        return location


    def update(self, instance, validated_data):
        bus_data = validated_data.pop('bus')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        bus = instance.bus

        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.save()
        bus.save()
        return instance

    #    loc = self.Meta.Location
    #    self.Meta.Location.create_loc(loc, data)
    #    self = Location
    #    self.latitude = validated_data["latitude"]
    #    self.longitude = validated_data["longitude"]
    #    self.ID.bus_id = validated_data["ID"]["bus_id"]
    #    self.ID.nfc_id = validated_data["ID"]["nfc_id"]
    #    return self

# Create your views here.
