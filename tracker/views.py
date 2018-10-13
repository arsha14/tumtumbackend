# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
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

@api_view(['GET', 'POST'])
def LocationList(request):
    if request.method == 'GET':
        queryset = Location.objects.all()
        serializer_class = LocationSerializer(queryset, many=True)
        return Response(serializer_class.data)

    elif request.method == 'POST':
        serializer_class = LocationSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def LocationDetail(request, pk):
    try:
        queryset = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_class = LocationSerializer(queryset)
        return Response(serializer_class.data)

    elif request.method == 'PUT':
        serializer_class = LocationSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.validated_data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

