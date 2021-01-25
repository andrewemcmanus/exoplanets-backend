from django.shortcuts import render
from .models import Visual
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
      # DON'T render a new page...
      return render(request, 'signup.html', {'form': form})
  else:
    form = UserCreationForm()
    # DON'T render a new page...
    return render(request, 'signup.html', {'form': form})

def visuals_index(request):
    visuals = Visual.objects.all()
    return HttpResponse()

def database(request):
    if request.method == 'GET':
        response = request.POST.get('https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=compositepars&format=json&select=fpl_hostname')
        return JsonResponse(response, safe=False)
    # print(response)
        # if/then/else forcertain model parameters go here:

# if request.method == 'GET':
#     parameters = []
#     for i in range(len(response)):
#         system_name =
#         star_lum =
#         star_metal =
#         planet_eqtemp =
#         star_efftemp =
#         star_optmag =
#         star_grav =
#         star_mass =
#         planet_rad =
#         planet_eccen =
#         planet_dens =
#         planet_orbper =
#         planet_smaxis =
