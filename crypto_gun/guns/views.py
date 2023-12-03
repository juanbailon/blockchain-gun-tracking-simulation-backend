from django.shortcuts import render
from rest_framework import generics, permissions,status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GunSerializer
from .models import Gun
from .utils import calculate_sha256_bytes, bytes_to_unsigned_int

# Create your views here.

class RetriveGunView(generics.RetrieveAPIView):
    serializer_class = GunSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Gun.objects.all()
    lookup_field = 'pk'


class ListAllGunsView(generics.ListAPIView):
    serializer_class = GunSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Gun.objects.all()


class CreateGunView(generics.CreateAPIView):
    serializer_class = GunSerializer
    permission_classes = [permissions.AllowAny]


class GetGunHashIntView(APIView):
    
    permission_classes = [permissions.AllowAny]

    def get(self, request, gun_id):

        try:
           gun = Gun.objects.get(id= gun_id)
        except Gun.DoesNotExist:
            return Response({'message': 'Gun with the provided id does not exists'}, status= status.HTTP_404_NOT_FOUND)
        

        hash = calculate_sha256_bytes(input_string= gun.serial_number)
        unsigned_integer = bytes_to_unsigned_int(hash_bytes= hash)

        return Response({'NFT-ID': unsigned_integer}, status= status.HTTP_200_OK)