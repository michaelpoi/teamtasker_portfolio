from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request,'home.html' )

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('signin')####
    else:
        form = UserCreationForm()
    return render(request,'signup.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'dashboard.html')
