from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from hosbkk_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from .filter import HospitalsFilter



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

    user  = User.objects.filter(id__gt=1)
    hospital = Hospitals.objects.order_by('code')
    project = Project.objects.all()
    status = Status.objects.all()
    service = Service.objects.all()
    subgroup = Project_subgroup.objects.all()


    context = {"status_": status,"services" : service, "projects" : project, "users" : user, "hospitals":hospital , "subgroups" : subgroup}
    
    return render(request, 'staff_template/add_case_template.html', context)

def case_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        project = request.POST.get("project")
        case_name = request.POST.get("case_name")
        case_desc = request.POST.get("case_desc")
        case_res = request.POST.get("case_res")
        assigned_user = request.POST.get("assigned_user_id")
        hospital = request.POST.get("hospital")
        service = request.POST.get("service")
        subgroup = request.POST.get("subgroup")
        status = request.POST.get("status")
        try:
            new_case = Case()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))

