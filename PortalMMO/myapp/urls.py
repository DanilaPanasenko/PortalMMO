from django.urls import path
from .views import AdvertisementList

urlpatterns = [
    path('posts/', AdvertisementList.as_view(), name='advert_list'),
]