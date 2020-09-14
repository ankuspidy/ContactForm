from django.forms import ModelForm
from .models import Contact

class UserContactForm(ModelForm):


    class Meta:
        model = Contact
        fields = ['name','email','contact','message']
