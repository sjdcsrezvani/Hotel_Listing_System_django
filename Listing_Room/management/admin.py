from django.contrib import admin
from .models import Room, Booking, RoomType, Hotel
# Register your models here.
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Hotel)