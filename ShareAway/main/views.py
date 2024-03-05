from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddIdeaForm
from .models import Idea

# Create your views here.

def home(request):
    ideas = Idea.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, try again.")
            return redirect('home')
    else:
        return render(request, "home.html", {'ideas':ideas})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

def idea(request, pk):
    if request.user.is_authenticated:
        idea = Idea.objects.get(id=pk)
        return render(request, 'idea.html', {'idea':idea})
    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')
    
def delete_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.user == idea.author:
        delete_it = Idea.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Idea deleted!")
        return redirect('home')
    else:
        messages.success(request, "You are not allowed to do that!")
        return redirect('home')


def add_idea(request):
    form = AddIdeaForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                idea = form.save(commit=False)
                idea.author = request.user
                idea.save()
                messages.success(request, "Idea added!")
                return redirect('home')
        return render(request, 'add_idea.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to do that!")
        return redirect('home')


def update_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.user == idea.author:
        current_idea = Idea.objects.get(id=pk)
        form = AddIdeaForm(request.POST or None, instance=current_idea)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.save()
            messages.success(request, "Idea has been updated!")
            return redirect('home')
        return render(request, 'update_idea.html', {'form':form})
    else:
        messages.success(request, "You are not allowed to do that!")
        return redirect('home')
    