from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone

from management.models import Hotel, RoomType, Room, Booking


    

class RoomWriteSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        
        
class HotelWriteSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Hotel
        fields = '__all__'

        
class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

        
class RoomReadSerializer(RoomWriteSerializer):
    type = RoomTypeSerializer()    

    
class HotelRetrieveSerializer(HotelWriteSerializer):
    rooms = RoomReadSerializer(many=True)
    

class HotelListSerializer(HotelRetrieveSerializer):
    rooms = None
    


from .models import Room, Booking

class RoomAvailabilityChecker:
    def __init__(self, room, check_in, check_out):
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def is_room_available(self):
        booking_list = Booking.objects.filter(room=self.room)
        for booking in booking_list:
            if not (booking.check_in > self.check_out or booking.check_out < self.check_in):
                return False
        return True



    
class BookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
    def create(self, validated_data):
        room = validated_data.get('room')
        check_in = validated_data.get('check_in')
        check_out = validated_data.get('check_out')

        checker = RoomAvailabilityChecker(room, check_in, check_out)
        if checker.is_room_available():
            return super().create(validated_data)
        else:
            raise serializers.ValidationError('This room is not available')




        
class BookingReadSerializer(serializers.ModelSerializer):
    room = RoomReadSerializer()
    class Meta:
        model = Booking
        exclude = ['email',]  
        