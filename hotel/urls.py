from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('reservation/<int:room_id>/', views.ReservationView.as_view(), name='reservation'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('signup/', views.signup, name='signup'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('send_reserve/<int:room_id>/', views.send_reserve,name='send_reserve'),
    
]

