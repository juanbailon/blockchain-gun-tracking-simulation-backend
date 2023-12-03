from django.shortcuts import render
from rest_framework import generics, permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SoldierSerializer, SoldierGunSerializer, SoldierWalletSerializer
from .models import Soldier, SoldierGun, SoldierWallet
from .wallet_handler import EncryptionHandler, WalletHandler

# Create your views here.

class RetriveSoldierView(generics.RetrieveAPIView):
    serializer_class = SoldierSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Soldier.objects.all()
    lookup_field = 'pk'


class ListAllSoldiersView(generics.ListAPIView):
    serializer_class = SoldierSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Soldier.objects.all()


class CreateSoldierView(generics.CreateAPIView):
    serializer_class = SoldierSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Soldier.objects.all()


class CreateSoldierGunView(generics.CreateAPIView):
    serializer_class = SoldierGunSerializer
    permission_classes = [permissions.AllowAny]


class ListAllSoldierGunView(generics.ListAPIView):
    serializer_class = SoldierGunSerializer
    permission_classes = [permissions.AllowAny]
    queryset = SoldierGun.objects.all()


class CreateSoldierWalletView(generics.CreateAPIView):
    serializer_class = SoldierWalletSerializer
    permission_classes = [permissions.AllowAny]


class ListAllSoldierWalletView(generics.ListAPIView):
    serializer_class = SoldierWalletSerializer
    permission_classes = [permissions.AllowAny]
    queryset = SoldierWallet.objects.all()


class CreateSoldierWalletView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):
                
        try:
            soldier = Soldier.objects.get(id = pk)
        except Soldier.DoesNotExist:
            return Response({'message': 'This soldier does not exists'}, status= status.HTTP_404_NOT_FOUND)


        soldier_wallet_obj = SoldierWallet.objects.filter(soldier= soldier)

        if soldier_wallet_obj.exists():
            return Response({'message': 'This user already has a wallet'}, status= status.HTTP_200_OK)
        
        private_key =  WalletHandler.generate_private_key()
        address = WalletHandler.generate_eth_account(private_key= private_key).address
        
        SoldierWallet.objects.create(
            soldier = soldier,
            private_key = EncryptionHandler.encryp_value(value= private_key),
            wallet_address = address
        )

        return Response(
            {
            'message': 'wallet created sucessfully',
            'wallet_address': address,
            }, 
            status= status.HTTP_201_CREATED
            )
        