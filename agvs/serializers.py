from rest_framework import serializers
from .models import Agv_identify, Agv_data


class AgvIdentifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agv_identify
        fields = ('verhicle_id', 'verhicle_model' , 'guidance', 'is_active', 'is_connected')
 
class AgvDataserializer(serializers.ModelSerializer):
    
    agv_identify = AgvIdentifySerializer()
    
    class Meta:
        model = Agv_data
        fields = "__all__"
    