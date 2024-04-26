from django import forms
from django.core import validators
from order_app.models import Order, Client, UserProfileInfo
from django.contrib.auth.models import User

class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)