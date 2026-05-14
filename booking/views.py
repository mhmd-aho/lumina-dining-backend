from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Category, MenuItem, Table, Booking, Favorite
from .serializers import CategorySerializer, MenuItemSerializer, TableSerializer, BookingSerializer, FavoriteSerializer
class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class MenuItemsView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        if self.request.query_params.get('category'):
            return MenuItem.objects.filter(category=self.request.query_params.get('category'))
        return MenuItem.objects.all()
class TableView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class BookingUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
class FavoriteView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class FavoriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    def perform_destroy(self, instance):
        instance.delete()
