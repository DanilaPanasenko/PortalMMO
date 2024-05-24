from django.urls import path
from .views import AdvertisementList, AdvertisementDetail, PostSearch, AdvertisementCreate

urlpatterns = [
    path('posts/', AdvertisementList.as_view(), name='advert_list'),
    path('detail/<int:pk>', AdvertisementDetail.as_view(), name='detail'),
    path('posts/search/', PostSearch.as_view(), name='search'),
    path('posts/create/', AdvertisementCreate.as_view(), name='create'),
]
