from django.shortcuts import render,redirect
from django.http import HttpResponse



def homePage(request):
    return render(request, "index.html")

def Contacts(request):
    return render(request, "contact.html")

