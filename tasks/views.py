from dataclasses import fields
from re import template
from django.shortcuts import render
from .models import task
from .forms import addTask,editTask
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class taskview(ListView):
    model = task
    template_name = "task.html"

    def get_queryset(self):
        if self.request.user.is_anonymous:
           return None
        else:
            return task.objects.filter(user = self.request.user) 

class taskdetail(DeleteView):
    model = task
    template_name = "task_detail.html"

class taskadd(CreateView):
    model = task
    form_class = addTask
    template_name = "task_add.html"

class taskdelete(DeleteView):
    model = task
    template_name = "task_delete.html"
    success_url = reverse_lazy("tasks")

class taskupdate(UpdateView):
    model = task
    form_class = editTask
    template_name = "task_update.html"

class taskcomplete(UpdateView):
    model = task
    fields = ("complete",)
    template_name = "task_complete.html"

class registration(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")
