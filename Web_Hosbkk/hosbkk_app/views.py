from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    return render(request, 'staff_template/login.html')