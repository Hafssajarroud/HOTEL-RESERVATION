from django.db import models
from django.urls import reverse

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reservation', args=[str(self.id)])


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    nombreAdult = models.SmallIntegerField(default=1)
    nombreEnfant = models.SmallIntegerField(default=1)
    telephone = models.IntegerField(default=0)
    def __str__(self):
        return f'Reservation for {self.guest_name} in {self.room.name} ,for {self.price_per_night} in {self.room.price_per_night}  '


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone = models.IntegerField( null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200)
    question = models.TextField(max_length=255)