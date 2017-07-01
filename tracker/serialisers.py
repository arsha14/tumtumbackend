# -*- coding: utf-8 -*-
from rest_framework import serializers
from tracker.models import Location



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'