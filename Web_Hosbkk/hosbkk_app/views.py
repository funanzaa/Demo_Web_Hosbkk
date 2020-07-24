from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from hosbkk_app.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from .filter import HospitalsFilter
from datetime import datetime
from hosbkk_app.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def HomePage(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("home-page"))

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

@login_required
def staff_home(request):
    
    form = Form_Find_Hosp()

    if request.method == 'POST':
        form = Form_Find_Hosp(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS")
            name = form.cleaned_data['text_find']
            case = Case.objects.filter(name__icontains=name)
            print(case)
    


    current_user = request.user.id
    sum_cases = Case.objects.filter(created_by_id=current_user).count()
    new_cases = Case.objects.filter(created_by_id=current_user).filter(status_id=2).count()
    penging_cases = Case.objects.filter(created_by_id=current_user).filter(status_id=4).count()
    close_cases = Case.objects.filter(created_by_id=current_user).filter(status_id=3).count()
    all_cases = Case.objects.filter(created_by_id=current_user).order_by('-id')[:10] 
    context = {"form": form,"all_case" :all_cases,"sum_case":sum_cases,"new_case": new_cases,"penging_case": penging_cases,"close_case":close_cases,'check': 'data_home'}
    return render(request, 'staff_template/staff_home_template.html', context)

# @csrf_exempt #  we don't need to Pass csrf_token
@login_required
def staff_add_case(request):

    current_user = request.user.id
    hospital={}
    print(current_user)
    # user  = User.objects.filter(id__gt=1)
    user  = User.objects.filter(id__exact=current_user)
    # hospital = Hospitals.objects.order_by('code')
    project = Project.objects.all()
    status = Status.objects.all()
    service = Service.objects.all()
    subgroup = Project_subgroup.objects.all()
    
    if request.method == "POST":

        code = request.POST.get("name")
        hospital = Hospitals.objects.filter(label__icontains=code)|Hospitals.objects.filter(code__icontains=code)
        context = {"hospitals" : hospital}
        return render(request, 'staff_template/add_case_template.html', context )
    context = {"status_": status,"services" : service, "projects" : project, "users" : user, "hospitals":hospital , "subgroups" : subgroup}
    return render(request, 'staff_template/add_case_template.html', context)

def case_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        messages.success(request, "")
        project = request.POST.get("project")
        case_name = request.POST.get("case_name")
        case_desc = request.POST.get("case_desc")
        case_res = request.POST.get("case_res")
        assigned_user = request.POST.get("assigned_user_id")
        hospital = request.POST.get("hospital_pk")
        service = request.POST.get("service")
        subgroup = request.POST.get("subgroup")
        status = request.POST.get("status")
        user_id = request.POST.get("user_id")
        try:
            new_case = Case()
            new_case.name = case_name
            new_case.modified = user_id
            new_case.assigned_user = assigned_user
            new_case.description = case_desc
            new_case.resolution = case_res
            new_case.date_entered = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_case.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_case.update_at = ""
            new_case.created_by_id = user_id
            new_case.hospitals_id = hospital
            new_case.project_id = project
            new_case.project_subgroup_id = subgroup
            new_case.service_id = service
            new_case.status_id = status
            new_case.save()
            messages.success(request, "Successfully Add Case")
            return HttpResponseRedirect(reverse("staff_home"))
        except:
            messages.error(request, "Failed to Add Case")
            return HttpResponseRedirect(reverse("form_find_hosp"))
def form_find_hosp(request):
    # form = Form_Find_Hosp()
    # if request.method != "POST":
    #       return HttpResponse("Method Not Allowed")
    # else:
    #      form = Form_Find_Hosp(request.POST)
    #     if form.is_valid():
    #         text = form.cleaned_data['name']
    #         # print("VALIDATION SUCCESS!")
    #         # print("Name : " + form.cleaned_data['name'])
    #         # print("resolution : " + form.cleaned_data['resolution'])
    #         # print("status : " + form.cleaned_data['status'])
    #         # form.save(commit=True)
    #         # return HttpResponseRedirect(reverse("staff_home"))
    #         # return render(request, 'staff_template/form_add_case.html', {'form' : form })
    #     # else:
    #         # print("Error From Invild")
    return render(request, 'staff_template/form_find_hosp.html')

def find_hosp_add(request):

    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        code_lable = request.POST.get("code_lable")
        hospital = Hospitals.objects.filter(label__icontains=code_lable)|Hospitals.objects.filter(code__icontains=code_lable)
        context = {"hospitals" : hospital}
        return render(request, 'staff_template/form_find_hosp.html', context )

def add_case(request, hosp_id):

    current_user = request.user.id
    # print(current_user)
    # user  = User.objects.filter(~Q(id = current_user)&~Q(username = "admin")) # not equal user and admin
    user  = User.objects.filter(~Q(username = "admin"))
    print(user)
    hospital = Hospitals.objects.filter(id=hosp_id)
    project = Project.objects.all()
    status = Status.objects.all()
    service = Service.objects.all()
    subgroup = Project_subgroup.objects.all()
    context = {"status_": status,"services" : service, "projects" : project, "users" : user, "hospitals":hospital , "subgroups" : subgroup}

    return render(request, 'staff_template/add_case_template.html', context)


def edit_case(request,pk_case):
    current_user = request.user.id
    case = Case.objects.filter(id=pk_case)
    project = Project.objects.all()
    context = {"case":case,"user":current_user,"projects" : project}
    print(context)
    return render(request, 'staff_template/edit_case_template.html',context)

# def form_find_case_home(request):
#     form = Form_Find_Hosp()
#     print("test")
#     return render(request,'staff_template/staff_home_template.html', {'form':form})