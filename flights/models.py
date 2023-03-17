from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


# Creata a class for each main table and inside give it's properties
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
# Even after defining this class, there will be no file in the directory
# representing this table. Hence we use MIGRATIONS
# ----------------------------- MIGRATIONS ------------------------------
# This is a way of telling django that we need to modify the database with
# the changes we made.

    # To get nicely formatted rows in cmd when fetching data
    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination} in {self.duration} mins"
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"