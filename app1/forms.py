from django import forms
from .models import Signup,Pictures
class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=12)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=12)
    class Meta():
        model=Signup
        fields='__all__'
        
class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=12)
    class Meta():
        model=Signup
        fields=('Email','Password',)
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Signup
        fields=('Name','Age','Place','Photo','Email')
        
class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=12)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=12)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=12)
    
class PicturesForm(forms.ModelForm):
  class Meta():
       model=Pictures
       fields='__all__'
       
class DescriptionForm(forms.ModelForm):
    class Meta():
        model=Pictures
        fields=('Car','Image','Brand','Details')