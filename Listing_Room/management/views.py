from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render

from management.serializer import (
    HotelWriteSerializer,
    RoomTypeSerializer,
    HotelRetrieveSerializer,
    HotelListSerializer,
    BookingWriteSerializer,
    BookingReadSerializer,
    RoomWriteSerializer,
    
)
from management.models import (
    Hotel,
    RoomType,
    Room,
    Booking,
)
from management.permissions import ReadOnly



class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.prefetch_related(
        'rooms__type',
        ).order_by(
            'pk',
        )
    write_serializer_class = HotelWriteSerializer
    list_serializer_class = HotelListSerializer
    retrieve_serializer_class = HotelRetrieveSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    
    def get_serializer_class(self):
        serializer_action_maping = {
            'create': self.write_serializer_class,
            'retrieve': self.retrieve_serializer_class,
            'update': self.write_serializer_class,
            'partial_update': self.write_serializer_class,
        }
        return serializer_action_maping.get(
            self.action,
            self.list_serializer_class,
        )
        
        
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.order_by('pk')
    serializer_class = RoomWriteSerializer
    permission_classes = [IsAdminUser]
    
    
class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.order_by('pk')
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAdminUser]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related(
            'room__type',
        ).order_by(
            'pk',
        )
    write_serializer_class = BookingWriteSerializer
    read_serializer_class = BookingReadSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(guest= self.request.user,)
        return queryset
    
    def get_serializer_class(self):
        serializer_action_maping = {
            'create': self.write_serializer_class,
            'update': self.write_serializer_class,
            'partial_update': self.write_serializer_class,
        }
        
        return serializer_action_maping.get(
            self.action,
            self.read_serializer_class,
        )


def report_view(request):
    reservations = Booking.objects.all()
    return render(request, 'management/report.html', {'report_bookings': reservations})
