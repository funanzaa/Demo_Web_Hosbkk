from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from hosbkk_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from .filter import HospitalsFilter
from datetime import datetime



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
        user_id = request.POST.get("user_id")
        try:
            new_case = Case()
            new_case.name = case_name
            new_case.modified_user_id = 'user_id'
            new_case.assigned_user_id = assigned_user
            new_case.description = case_desc
            new_case.resolution = case_res
            new_case.date_entered = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_case.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_case.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_case.created_by_id = user_id
            new_case.hospitals_id_id = hospital
            new_case.project_id_id = project
            new_case.project_subgroup_id_id = subgroup
            new_case.service_id_id = service
            new_case.status_id = status
            new_case.save()
            print("test")
        except:
            messages.error(request, "Failed Add Staff")
            return HttpResponseRedirect(reverse("staff_add_case"))

