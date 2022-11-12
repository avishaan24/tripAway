from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import order

from django import forms

# class Orderform(ModelForm):
#     class Meta:
#         models= order
#         fields= ' _all__ '

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUser,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class']="search_input search_input_3"
        self.fields['first_name'].widget.attrs['placeholder']="First Name"
        self.fields['last_name'].widget.attrs['class']="search_input search_input_3"
        self.fields['last_name'].widget.attrs['placeholder']="Last Name"
        self.fields['username'].widget.attrs['class']="search_input search_input_3"
        self.fields['username'].widget.attrs['placeholder']="User Name"
        self.fields['email'].widget.attrs['class']="search_input search_input_3"
        self.fields['email'].widget.attrs['placeholder']="Email"
        self.fields['password1'].widget.attrs['class']="search_input search_input_3"
        self.fields['password1'].widget.attrs['placeholder']="Password"
        self.fields['password2'].widget.attrs['class']="search_input search_input_3"
        self.fields['password2'].widget.attrs['placeholder']="Confirm Password"