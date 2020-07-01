from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def showDemoPage(request):
    return render(request, 'demo.html')