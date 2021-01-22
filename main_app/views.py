from django.shortcuts import render
from .models import Exoplanets
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

########## USER ##############
def profile(request, username):
  user = User.objects.get(username=username)
  # cats = Cat.objects.filter(user=user)
  return render(request, 'profile.html', {'username': username})

def login_view(request):
  # if post, then authenticate (the user will be submitting a username and password)
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      u = form.cleaned_data['username']
      p = form.cleaned_data.get('password')
      user = authenticate(username=u, password=p)

      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/user/' + u)
        else:
          print(f"The account for {u} has been disabled.")
      else:
        print('The username and/or password is incorrect.')
  else: # get request that sent up empty form
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/cats')

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      print(user)
      login(request, user)
      return HttpResponseRedirect('/user/' + str(user))
    else:
      form = UserCreationForm()
      return render(request, 'signup.html', {'form': form})
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def get_database(request):
    if request.method == 'GET':
        # if/then/else for certain model parameters go here:
    return HttpResponse(response, content_type="'application/json'")
