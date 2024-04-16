from rest_framework import serializers
from .models import Agv

class AgvSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agv
        fields = ('verhicle_id', 'verhicle_model' , 'guidance', 'is_active', 'is_connected')
        