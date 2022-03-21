from django.forms import ModelForm
from myapp.models import *

class ContactRegister(ModelForm):

	class Meta:
		model=Contact
		fields='__all__'