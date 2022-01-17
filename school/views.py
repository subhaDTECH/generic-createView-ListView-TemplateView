from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# Create your views here.

class StudentCreateView(CreateView):
    form_class=StudentForm 
    template_name='school/student_form.html'
    success_url='/thankyou/'
class ThanksTemplateView(TemplateView):
    template_name='school/thankyou.html'
class Studentupdate(UpdateView):
    model=Student
    form_class=StudentForm
    success_url='/thankyou/'
class StudentDelete(DeleteView):
    model=Student 
    template_name='school/student_delete.html'
    success_url="/thankyou/"
class StudentShowView(ListView):
    model=Student 
    template_name='school/show.html'   
