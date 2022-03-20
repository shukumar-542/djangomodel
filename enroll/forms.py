from tkinter import Widget
from django import forms

class studentForm(forms.Form):
      name =  forms.CharField()
      email = forms.EmailField()
      # key=  forms.CharField(widget=forms.HiddenInput())