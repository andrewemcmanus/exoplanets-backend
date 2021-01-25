from django.shortcuts import render
from .models import Exoplanets
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
      return render(request, 'signup.html', {'form': form})
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def visuals_index(request):
    visuals = Visual.objects.all()
    return HttpResponse()

def database(request):
    print(request)
    if request.method == 'GET':
        response = request.get("https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=compositepars&format=json&select=fpl_hostname, fst_lum, fst_met, fpl_eqt, fst_teff, fst_optmag, fst_logg, fst_mass, fpl_radj, fpl_bmassj, fpl_eccen, fpl_dens, fpl_orbper, fpl_smax")
        # if/then/else forcertain model parameters go here:
    return JsonResponse(response, safe=False)

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
