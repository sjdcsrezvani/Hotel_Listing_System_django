from django.db import models



class RoomType(models.Model):
    type = models.CharField(max_length=50)
    
    objects = models.Manager()

    def __str__(self):
        return self.type


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    hotel = models.ForeignKey(
        'management.Hotel',
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    type = models.ForeignKey(
       'management.RoomType',
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    number = models.IntegerField()
    beds = models.IntegerField()
    
    objects = models.Manager()

    def __str__(self):
        return f'Hotel Name: {self.hotel}. room: {self.number}. Beds: {self.beds}'
    
    
class Booking(models.Model):
    room = models.ForeignKey(
        'management.Room',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    guest = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    objects = models.Manager()
    
    def __str__(self):
        return f'From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To : {self.check_out.strftime("%d-%b-%Y %H:%M")}'
    