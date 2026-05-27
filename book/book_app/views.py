

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json
from django.shortcuts import render



def home_page(request):
    return render(request,'home.html')
def contact_page(request):
    return render(request,'contact.html')
def profile_page(request):
    return render(request,'profile.html',{"name":"thanuja","email":"thanuja29@gmail.com","branch":"cse","address":"guntur","role":"admin","marks":78,
                                          "user_data":
                                          [
                                              {"name":"harshitha","email":"harshi@gmail.com"},
                                              {"name":"stephy","email":"stephy@gmail.com"},
                                              {"name":"chethana","email":"chethu@gmail.com"}
                                          ],"range":range(0,10)
                                                                                                                                                     })
