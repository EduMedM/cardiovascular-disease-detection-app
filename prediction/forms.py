from django import forms
from prediction.models import Patient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from datetime import date

class PatientForm(forms.ModelForm):
    
    class Meta:
        st_depression = forms.DecimalField(
        max_digits=5,  
        decimal_places=2,  
        widget=forms.NumberInput(attrs={'class': 'form-control'}), 
        )
        
        date_of_birth = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        )
        
        model = Patient
        fields = ('name','surname','email', 'id_num', 'phone_number', 'date_of_birth', 'sex','cp',
                  'resting_bp','serum_cholesterol', 'cholesterol_reference_value', 'fasting_blood_sugar',
                  'resting_ecg', 'max_heart_rate','exercise_induced_angina','st_depression','st_slope',
                  'number_of_vessels','thallium_scan_results')

class UserUpdateForm(UserChangeForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'minlength': '8'}), required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'minlength': '8'}), required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
