from rest_framework import serializers
from .models import Category, MenuItem, Table, Booking
from django.utils import timezone
from datetime import timedelta
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
    def validate(self, attrs):
        if attrs['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return attrs
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
    def validate(self, attrs):
        if attrs['capacity'] < 2:
            raise serializers.ValidationError("Capacity cannot be less than 2")
        if attrs['table_number'] < 1:
            raise serializers.ValidationError("Table number cannot be less than 1")
        return attrs
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','table','user','booking_time','guests']
        read_only_fields = ['id','user']
    def validate(self, attrs):
        booking_id = self.instance.id if self.instance else None
        booking_Duration = timedelta(minutes = 90)
        start_time = attrs['booking_time']
        end_time = start_time + booking_Duration
        overlapping_bookings= Booking.objects.filter(
            table=attrs['table'],
            booking_time__lt=end_time,
            booking_time__gt= start_time-booking_Duration
        ).exclude(id=booking_id)
        if overlapping_bookings.exists():
            raise serializers.ValidationError("This table is occupied during that time window.")
        if attrs['guests'] > attrs['table'].capacity:
            raise serializers.ValidationError("Number of guests exceeds table capacity")
        if attrs['booking_time'] < timezone.now():
            raise serializers.ValidationError("Booking time cannot be in the past")
        return attrs