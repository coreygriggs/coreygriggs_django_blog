__author__ = 'coreygriggs'

from django import forms


class ContactForm(forms.Form):
	subject = forms.CharField(max_length=40)
	email = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea)