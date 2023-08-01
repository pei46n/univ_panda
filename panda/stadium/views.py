from django.shortcuts import render, get_object_or_404
from .models import Stadium
from django.views import generic

# Create your views here.
# def home(request):
#     return render(request, 'stadium/home.html')

class HomeView(generic.ListView):
    template_name = 'stadium/home.html'
    model = Stadium

class IndexView(generic.ListView):
    template_name = 'stadium/stadium_list.html'
    model = Stadium

class DetailView(generic.DetailView):
    template_name = 'stadium/stadium_detail.html'
    model = Stadium

class J1_View(generic.ListView):
    template_name = 'stadium/stadium_j1_list.html'
    model = Stadium

class J2_View(generic.ListView):
    template_name = 'stadium/stadium_j2_list.html'
    model = Stadium

class J3_View(generic.ListView):
    template_name = 'stadium/stadium_j3_list.html'
    model = Stadium