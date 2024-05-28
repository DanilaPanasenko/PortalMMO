from django.urls import path
from .views import AdvertisementList, AdvertisementDetail, PostSearch, AdvertisementCreate, AdvertisementUpdate, \
    AdvertisementDelete, ResponsesCreate

urlpatterns = [
    path('posts/', AdvertisementList.as_view(), name='advert_list'),
    path('detail/<int:pk>', AdvertisementDetail.as_view(), name='detail'),
    path('posts/search/', PostSearch.as_view(), name='search'),
    path('posts/create/', AdvertisementCreate.as_view(), name='create'),
    path('posts/<int:pk>/update/', AdvertisementUpdate.as_view(), name='update'),
    path('posts/<int:pk>/delete/', AdvertisementDelete.as_view(), name='delete'),
    path('<int:pk>/response/create/', ResponsesCreate.as_view(), name='response_create'),
]
