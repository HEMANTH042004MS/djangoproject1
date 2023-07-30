from django import forms
from newapp.models import DIRECTORS


# Create your models here.

class DIRECTORSFORM(forms.ModelForm):
	class Meta:
			model = DIRECTORS
			fields='__all__'

	
    	
