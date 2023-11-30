from django.shortcuts import render
from django.http import HttpResponse

def Userhome(request):
    return HttpResponse("Users Home")

def Homepage(request):
    return render(request, 'home.html')