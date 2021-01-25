from django.shortcuts import render
from .models import Visual
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from psycopg2.extras import Json
# conn = psycopg2.connect("dbname=Visual")
# cur = conn.cursor()

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

# def database(request):
#     if request.method == 'GET':
        # item = {
        #         "fpl_hostname": "GJ 163",
        #         "fst_lum": -1.708,
        #         "fst_met": 0.100,
        #         "fpl_eqt": 0,
        #         "fst_teff": 3500.00,
        #         "fst_optmag": 11.810,
        #         "fst_logg": 0,
        #         "fst_mass": 0.40,
        #         "fpl_radj": 0.290,
        #         "fpl_eccen": 0.073000,
        #         "fpl_dens": 1.70000,
        #         "fpl_orbper": 8.63182000,
        #         "fpl_smax": 0.060700
        #     }
        #
        # def sql_insert(tableName, data_dict):
        #     '''
        #     INSERT INTO Visual (system_name, star_lum, star_metal, planet_eqtemp, star_efftemp, star_optmag, star_grav, star_mass, planet_rad, planet_eccen, planet_dens, planet_orb_per, planet_smaxis)
        #     VALUES (%(fpl_hostname)s, %(fst_lum)s, %(fst_met)s, %(fpl_eqt)s, %(fst_teff)s, %(fst_optmag)s, %(fst_logg)s, %(fst_mass)s, %(fpl_radj)s, %(fpl_eccen)s, %(fpl_dens)s, %(fpl_orbper)s, %(fpl_smax)s);
        #     '''
        #     sql = '''
        #         INSERT INTO %s (%s)
        #         VALUES (%%(%s)s );
        #         '''   % (tableName, ',  '.join(data_dict),  ')s, %('.join(data_dict))
        #     return sql
        #
        # tableName = 'Visual'
        # sql = sql_insert(tableName, item)
        # cur.execute(sql, item)
        # urllib.request.urlopen('https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=compositepars&format=json&select=fpl_hostname')
        # return JsonResponse(response, safe=False)
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
