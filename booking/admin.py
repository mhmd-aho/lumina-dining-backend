from django.contrib import admin
from .models import Category, MenuItem, Table, Booking, Favorite

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Favorite)
