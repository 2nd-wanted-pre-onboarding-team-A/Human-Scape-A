from .models import Paper
from rest_framework import serializers



class PaperListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paper
        fields = '__all__'


class PaperDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paper
        fields = '__all__'