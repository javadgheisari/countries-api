from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Country

class CountrySerializer(DocumentSerializer):
    class Meta:
        model = Country



class FindCountrySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)