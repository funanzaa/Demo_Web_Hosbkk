from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from hosbkk_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from .filter import HospitalsFilter
from datetime import datetime
from .search_hosp import *
from django.views.decorators.csrf import csrf_exempt



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
             return HttpResponseRedirect(reverse("staff_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect(reverse("login-page"))
    return HttpResponseRedirect(reverse("login-page"))

def staff_home(request):
    current_user = request.user.id
    sum_cases = Case.objects.filter(created_by_id=current_user).count()
    new_cases = Case.objects.filter(created_by_id=current_user).filter(status_id=2).count()
    penging_cases = Case.objects.filter(created_by_id=current_user).filter(status_id=4).count()
    close_cases = Case.objects.filter(created_by_id=current_user).filter(status_id=3).count()
    all_cases = Case.objects.filter(created_by_id=current_user).order_by('-create_at')
    print(current_user)
    context = {"all_case" :all_cases,"sum_case":sum_cases,"new_case": new_cases,"penging_case": penging_cases,"close_case":close_cases}
    print(context)
    return render(request, 'staff_template/staff_home_template.html', context)

@csrf_exempt #  we don't need to Pass csrf_token

def staff_add_case(request):

    hospital={}
    user  = User.objects.filter(id__gt=1)
    # hospital = Hospitals.objects.order_by('code')
    project = Project.objects.all()
    status = Status.objects.all()
    service = Service.objects.all()
    subgroup = Project_subgroup.objects.all()
    
    if request.method == "POST":
        # global hospital
        code = request.POST.get("name")
        print("POST" + code)
        hospital = Hospitals.objects.filter(label__icontains=code)|Hospitals.objects.filter(code__icontains=code)
        context = {"hospitals" : hospital}
        print(context)
        return render(request, 'staff_template/add_case_template.html', context )
        # print(hospital)
        # return hospital
    # print(hospital)
    # print(status)
    context = {"status_": status,"services" : service, "projects" : project, "users" : user, "hospitals":hospital , "subgroups" : subgroup}
    print(context)
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
        new_case = Case()
        new_case.name = case_name
        new_case.modified_user_id = user_id
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
        return HttpResponseRedirect(reverse("staff_home"))

def search_hosp(request):
    
    if request.method == "POST":
        search = request.POST.get("search")
        # print(search)
        search_hosp(search)

    hospital = Hospitals.objects.order_by('code')
    context = {"hospitals" : hospital}
    return render(request, 'staff_template/form.html', context)
