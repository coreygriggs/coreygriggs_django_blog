__author__ = 'coreygriggs'

from django import forms


class ContactForm(forms.Form):
	subject = forms.CharField()
	email = forms.EmailField(required=True)
	message = forms.CharField()