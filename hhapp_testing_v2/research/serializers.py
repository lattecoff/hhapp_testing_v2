from rest_framework import serializers
from .models import ResearchRef



class ResearchRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchRef
        fields = '__all__'
