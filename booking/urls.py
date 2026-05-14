from django.urls import path
from .views import *

urlpatterns = [
    path('reserve/', BookingView.as_view(), name='booking-list-create'),
    path('reserve/<int:id>/', BookingUpdateView.as_view(), name='booking-update-delete'),
    path('menu/', MenuItemsView.as_view(), name='menu-list'),
    path('category/', CategoriesView.as_view(), name='category-list'),
    path('favorite/', FavoriteView.as_view(), name='favorite-list-create'),
    path('favorite/<int:id>/', FavoriteDeleteView.as_view(), name='favorite-delete'),   
]