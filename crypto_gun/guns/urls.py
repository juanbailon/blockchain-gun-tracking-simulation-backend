from django.urls import path
from . import views

app_name='guns'


urlpatterns = [    
    path('<int:pk>', views.RetriveGunView.as_view(), name='get_soldier_info'),
    path('', views.ListAllGunsView.as_view(), name='get_all_soldier_info'),
    path('create', views.CreateGunView.as_view(), name='get_all_soldier_info'),
    path('<int:gun_id>/nft/id', views.GetGunHashIntView.as_view(), name='get_gun_nft_id'),
]