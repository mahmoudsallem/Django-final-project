from django.urls import path
from .views import PropertyDetail, PropertyList

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<int:pk>/', PropertyDetail.as_view(), name='property_detail_short'),
    path('<int:pk>/<slug:slug>/', PropertyDetail.as_view(), name='property_detail'),
]