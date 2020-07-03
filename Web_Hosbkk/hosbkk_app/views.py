from django.contrib import messages
from hosbkk_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from hosbkk_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse



def HomePage(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2> Method Not Allowed </h2>")
    else:
        user =EmailBackEnd.authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            # if user.user_type == "1":
            #     return HttpResponseRedirect('/admin_home')
            # elif user.user_type == "2":
            #     return HttpResponseRedirect(reverse("staff_home"))
            # else:
            #     return HttpResponseRedirect(reverse("student_home"))
            return HttpResponseRedirect(reverse("staff_home"))
            # return HttpResponse("username : " + user.username + " Password : " + user.password)
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect(reverse("login-page"))

    return HttpResponseRedirect(reverse("login-page"))

def staff_home(request):
    return render(request, 'staff_template/staff_home_template.html')

def staff_add_case(request):
    status = Status.objects.all()
    service = Service.objects.all()
    
    return render(request, 'staff_template/add_case_template.html', {"Status": status,"services": service})
