from django import forms
from .models import user, contacto

class contactForm(forms.ModelForm):

    class Meta : 
        model = contacto
        #fields = ["name", "email", "msn"]
        fields = '__all__'

        