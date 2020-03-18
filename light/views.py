from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Light 


