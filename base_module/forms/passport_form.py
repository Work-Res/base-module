from django import forms
from ..models import Passport


class PassportForm(forms.ModelForm):
	class Meta:
		model = Passport
		fields = '__all__'
