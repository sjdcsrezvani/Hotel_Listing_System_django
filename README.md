## It is A Hotel Room Booking Website developed using Django Framework

#### my first backend project

there was a bug in view.py , it is fixed now

### technologies used

* postgresql
* django
* django rest framework

### features for normal users
* can book rooms , choose hotel and room type
* if a room was occupied at certain time it can not be booked

### features for super user

* can book rooms
* can see html report of all bookings
* can add new hotels, rooms, room_type


create super user to add data to Room, Hotel and RoomType tables then use Booking API

### database diagram

![Screenshot 2024-08-03 141739](https://github.com/sjdcsrezvani/Hotel_Listing_System_django/blob/da1015f2fb4bbaa65672ca92d7a55241a4e44dbb/Database%20ER%20diagram%20(crow's%20foot).jpeg)

### conclusion:

if we add user model , authentication and some more attribute for rooms we can use this rest API in real world
