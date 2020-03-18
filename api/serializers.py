# api/serializers.py

from rest_framework import serializers
from light.models import Light
 


class LightModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Light
        # fields = ['id', 'color', 'state']  OU 
        fields = '__all__'