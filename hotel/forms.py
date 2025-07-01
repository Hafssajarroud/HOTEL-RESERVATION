from django import forms
from .models import Reservation
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_name', 'guest_email', 'check_in', 'check_out']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'description', 'price_per_night', 'image')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')