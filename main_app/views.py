from django.shortcuts import render
from .models import Visual, User, Notes
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

########## USER ##############
def profile(request, username):
  user = User.objects.get(username=username)
  visuals_index = User.objects.get(saved_visuals=saved_visuals)
  return render(request, 'profile.html', {'username': user, 'visuals_index': visuals_index})

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
  return HttpResponseRedirect('/')

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
      # DON'T render a new page...
      return render(request, 'signup.html', {'form': form})
  else:
    form = UserCreationForm()
    # DON'T render a new page...
    return render(request, 'signup.html', {'form': form})

# REMAINING ROUTES:

def get_users(request):
    users = User.objects.all().values('username')  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return JsonResponse(users_list, safe=False)

# GET submissions WHERE system_name = current page
# requires a route for displaying a given system_name...

def get_system(request, system_name):
    system = Visual.objects.all().values('system_name')
    system_list = list(systems)
    for i in range(len(system_list)):
        if system_name == system_list[i]:
            return JsonResponse(system_name, safe=False)


def get_submissions(request, system_name):
    content = Notes.objects.all().values('content')
    content_list = list(content)
    return JsonResponse(content_list, safe=False)

def get_system_list(request):
    systems = Visual.objects.all().values('system_name')
    system_list = list(systems)
    return JsonResponse(system_list, safe=False)

# def add_submissions(request):
#     if request.method == 'POST':
        # access CONTENT column from Notes database

class CreateSubmissions(CreateView):
    # user = User.objects.get(username=username)
    model = Notes
    # How to do a request for submissions??
    fields = ['content']
    success_url = '/submissions'

class UpdateSubmissions(UpdateView):
    # username = User.objects.get(username=username)
    model = Notes
    fields = ['content']

    def form_valid(self, form):
        print(self)
        self.object = form.save(commit=False)
        return HttpResponseRedirect()

class DeleteSubmissions(DeleteView):
    model = Notes
    success_url = '/submissions'
