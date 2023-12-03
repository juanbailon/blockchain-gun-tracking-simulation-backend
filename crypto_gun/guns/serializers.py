from rest_framework import serializers
from .models import Gun

class GunSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gun
        fields = ['id',
                  'serial_number',
                  'type',                  
                 ]        
        extra_kwargs = {
            'id': {'read_only': True},            
             }