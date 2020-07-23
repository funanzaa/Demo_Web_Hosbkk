from django import forms
from django.core import validators # Add validators
from hosbkk_app.models import * 


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

# class FormCase(forms.Form):
#     name = forms.CharField()
#     resolution = forms.CharField(widget=forms.Textarea)
#     status = forms.CharField()
 
class Form_Find_Hosp(forms.ModelForm):
    name = forms.CharField(label="Email", max_length=50)


    