from rest_framework import serializers
from .models import Soldier, SoldierGun, SoldierWallet

class SoldierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Soldier
        fields = ['id',
                  'first_name',
                  'middle_name',
                  'national_id',             
                 ]        
        extra_kwargs = {
            'id': {'read_only': True},            
             }
        

class SoldierGunSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoldierGun
        fields = ['id',
                  'soldier',
                  'gun',                             
                 ]        
        extra_kwargs = {
            'id': {'read_only': True},    
             }
        

class SoldierWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoldierWallet
        fields = ['id',
                  'soldier',
                  'wallet_address',                 
                 ]        
        extra_kwargs = {
            'id': {'read_only': True},    
             }