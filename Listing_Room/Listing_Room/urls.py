from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from management.views import (
    HotelViewSet,
    RoomTypeViewSet,
    BookingViewSet,
    report_view,
    RoomViewSet,
)


router = routers.DefaultRouter()
router.register('bookings', BookingViewSet)
router.register('hotels', HotelViewSet)
router.register('room_types', RoomTypeViewSet)
router.register('rooms', RoomViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    path('report/', report_view, name='report'),
]