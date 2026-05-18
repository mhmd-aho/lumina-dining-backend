from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    def __str__(self):
        return f"Table {self.table_number} with capacity {self.capacity}"
class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    guests = models.IntegerField()
    def __str__(self):
        return f"booking for {self.user.username} at {self.booking_time}"
    @classmethod
    def delete_expired_bookings(cls):
        return cls.objects.filter(booking_time__lt=timezone.now()).delete()
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} like {self.menu_item.name}"