from django.urls import path
from . import views


app_name='guns'


urlpatterns = [    
    path('<int:pk>', views.RetriveSoldierView.as_view(), name='get_soldier_info'),
    path('', views.ListAllSoldiersView.as_view(), name='list_all_soldiers'),
    path('create', views.CreateSoldierView.as_view(), name='create_soldier'),
    path('assign-gun', views.CreateSoldierGunView.as_view(), name='assign_gun_to_soldier'),
    path('all-gun', views.ListAllSoldierGunView.as_view(), name='list_all_SoldierGuns'),
    path('wallets', views.ListAllSoldierWalletView.as_view(), name='list_all_SoldierWallet'),
    path('<int:pk>/wallet/create', views.CreateSoldierWalletView.as_view(), name='list_all_SoldierWallet'),
]