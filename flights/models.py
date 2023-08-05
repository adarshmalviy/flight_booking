from django.db import models
from users.models import CustomUser

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    source_city = models.CharField(max_length=50, default=None)
    destination_city = models.CharField(max_length=50, default=None)
    departure_time = models.DateTimeField(default=None)
    arrival_time = models.DateTimeField(default=None)
    seat_count = models.IntegerField(default=60)

    def __str__(self):
        return self.flight_number


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number}"



# from django.db import models
# from users.models import CustomUser
# # from flights.models import Flight

# from django.db import models

# class Flight(models.Model):
#     flight_number = models.CharField(max_length=10)
#     departure_city = models.CharField(max_length=50)
#     arrival_city = models.CharField(max_length=50)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     seat_count = models.IntegerField(default=60)

# class Booking(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.username} - {self.flight.flight_number}"



# class Flight(models.Model):
#     flight_number = models.CharField(max_length=10, unique=True)
#     date = models.DateField()
#     time = models.TimeField()
#     availability = models.IntegerField(default=60)

#     def __str__(self):
#         return self.flight_number
