from django.urls import path
from .views import *

urlpatterns = [
    path('reserve/', BookingView.as_view(), name='booking-list-create'),
    path('menu/', MenuItemsView.as_view(), name='menu-list'),
    path('category/', CategoriesView.as_view(), name='category-list'),
]