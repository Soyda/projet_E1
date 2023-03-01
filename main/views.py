from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from  django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def index(request):
    # return HttpResponse("Hello, world. You're at the index.")
    return render(request, "main/index.html")

def about(request):
    return render(request, 'main/about.html')