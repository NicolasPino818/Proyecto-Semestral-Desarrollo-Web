from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import user, usercontact, newProduct

class contactForm(forms.ModelForm):

    class Meta : 
        model = usercontact
        #fields = ["name", "email", "msn"]
        fields = '__all__'


class registroUser(forms.ModelForm):
    class Meta : 
        model = user
        fields = '__all__'

class addProduct(forms.ModelForm):
    class Meta : 
        model = newProduct
        fields = '__all__'
        


        