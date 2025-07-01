from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Room, Reservation, Contact
from .forms import ReservationForm, RoomForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.contrib.messages import add_message
from django.middleware.csrf import get_token
SUCCESS = 25   
@login_required
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    context = {
        'csrf_token': get_token(request)
    }
    return render(request, 'contact.html',context=context)

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

class ReservationView(LoginRequiredMixin, View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        form = ReservationForm()
        return render(request, 'reservation.html', {'room': room, 'form': form})

def send_reserve(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        guest_name = request.POST.get('guest_name')
        guest_email = request.POST.get('guest_email')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        nombreAdult = request.POST.get('nombreAdult')
        nombreEnfant = request.POST.get('nombreEnfant')
        telephone = request.POST.get('telephone')
        reservation = Reservation.objects.create(
        room = room,
        guest_name = guest_name,
        guest_email = guest_email,
        check_in = check_in,
        check_out = check_out,
        nombreAdult =nombreAdult,
        nombreEnfant = nombreEnfant,
        telephone = telephone,
        )
        reservation.save()
        return render(request, 'reservation_confirmation.html',{'reservation':reservation}) 
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user) 
                messages.success(request, 'Votre compte a été créé avec succès.')
                return redirect('home')
            else: 
                messages.error(request, 'Authentification échouée. Veuillez vérifier vos informations de connexion.')
        else:
            messages.error(request, 'Erreur dans le formulaire. Veuillez vérifier les informations fournies.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def custom_logout(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('logout_success')
def logout_success(request):
    return render(request, 'logout_success.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        subject = request.POST.get('subject')
        question = request.POST.get('question')

        contact=Contact.objects.create(
            name=name,
            email=email,
            phone = phone,
            company = company,
            subject =subject,
            question =question
        )
        contact.save()

        add_message(request, SUCCESS, " The message has been sent")
        message = "The message has been sent"
        return render(request, 'contact.html' , {"message":message })