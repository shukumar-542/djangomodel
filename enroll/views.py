from django.shortcuts import render
from .models import Students
from .forms import studentForm

# Create your views here.

def studinfo(req):
      student = Students.objects.all()
      return render(req, 'enroll/student.html', {'student':student})

def studentform(req):
      fm = studentForm(auto_id=True)
      # fm.order_fields(field_order=['email','name'])
      return render(req, 'enroll/forms.html',{'form':fm})