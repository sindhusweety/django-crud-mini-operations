from rest_framework import serializers
from .models import Continents, Country, State

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continents
        fields = ['id', 'continent_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name', 'continent_id']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name', 'continent_id', 'country_id']