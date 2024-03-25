from datetime import date,timedelta, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.utils.timezone import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .resources import CdrResource
from tablib import Dataset

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logout_admin(request):
    logout(request)
    return redirect('landing')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def singular(request):
    return render(request, 'singular_number.html')

@login_required(login_url='login')
def multiple(request):
    return render(request, 'multiple_number.html')


def importExcel(request): 
    if request.method == 'POST':
        cdr_resource = CdrResource()
        dataset = Dataset()
        new_cdr = request.FILES['cdr']
        imported_data = dataset.load(new_cdr.read()),
        for data in imported_data:
            value = Cdr(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
            )
            value.save()
    
    return render(request, 'form.html')
