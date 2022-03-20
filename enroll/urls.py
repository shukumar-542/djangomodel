from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.studinfo),
    path('studentForm/', views.studentform)
]