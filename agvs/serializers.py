from rest_framework import serializers
from .models import Agv_data, Agv_identify, STATUS


class AgvIndentifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agv_identify
        fields = ('verhicle_id', 'verhicle_model' , 'guidance', 'is_active', 'is_connected')
 
class AgvDataserializer(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Agv_data
        fields = "__all__"
    
    def get_status(self, obj):
        return STATUS[obj.status][1]
    