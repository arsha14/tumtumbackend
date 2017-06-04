# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Location
from django.shortcuts import render
from rest_framework import generics
from serialisers import LocationSerializer



class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class LocationDetail(generics.RetrieveDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
# Create your views here.
