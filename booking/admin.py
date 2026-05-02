from django.contrib import admin
from .models import Category, MenuItem, Table, Booking

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Booking)
