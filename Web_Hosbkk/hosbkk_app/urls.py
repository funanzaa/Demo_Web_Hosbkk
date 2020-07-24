from django.urls import path
from .views import *



urlpatterns = [
    path('', HomePage , name = 'home-page'),
    path('Login', Login, name = 'login-page'),
    path('doLogin', doLogin, name = 'dologin-page'),
    path('staff_home', staff_home, name= 'staff_home'),
    path('staff_add_case', staff_add_case, name= 'staff_add_case'),
    path('case_save', case_save, name= 'case_save'),
    path('form_find_hosp', form_find_hosp, name ='form_find_hosp'),
    path('find_hosp_add', find_hosp_add, name ='find_hosp_add'),
    path('add_case/<str:hosp_id>', add_case, name="add_case"),
    path('edit_case/<str:pk_case>', edit_case, name="edit_case"),
    # path('form_find_case_home', form_find_case_home, name="form_find_case_home"),
]