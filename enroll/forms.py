from faulthandler import disable
from tkinter import Widget
from django import forms

class studentForm(forms.Form):
      name =  forms.CharField(label='your name',initial='shukumar',help_text='limit 70 characther')
      email = forms.EmailField(widget=forms.FileInput())
      # key=  forms.CharField(widget=forms.HiddenInput())