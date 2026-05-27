from django.urls import path
from .views import home_page,contact_page,profile_page

urlpatterns = [
    path('home',home_page),
    path('contact',contact_page),
    path('profile',profile_page),
]