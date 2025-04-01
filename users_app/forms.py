from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 

input_class = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5'
 
class SignUpForm(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': input_class, 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'alejandrolopez (+6 caracteres)', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': input_class, 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'alejandrolopez@mail.com', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': input_class, 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'******** (8 o más caracteres entre letras y números)', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': input_class, 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'********', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['first_name'].widget.attrs.update({ 
            'class': input_class, 
            'required':'', 
            'name':'first_name', 
            'id':'first_name', 
            'type':'text', 
            'placeholder':'Alejandro', 
            'maxlength': '16', 
            'minlength': '2', 
            }) 
        self.fields['last_name'].widget.attrs.update({ 
            'class': input_class, 
            'required':'', 
            'name':'last_name', 
            'id':'last_name', 
            'type':'text', 
            'placeholder':'Lopez', 
            'maxlength': '16', 
            'minlength': '2', 
            }) 
    
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')