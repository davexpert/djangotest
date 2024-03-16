from django.shortcuts import render
from .models import Car
from rest_framework import viewsets
from . serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

