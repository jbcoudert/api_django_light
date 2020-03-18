from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .serializers import LightModelSerializer
from light.models import Light

class LightListAPIView(ListAPIView):

    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

class LightCreateAPIView(CreateAPIView):

    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

class LightUpdateAPIView(UpdateAPIView):

    queryset = Light.objects.all()
    serializer_class = LightModelSerializer


