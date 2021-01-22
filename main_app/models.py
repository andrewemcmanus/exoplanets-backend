from django.db import models, migrations
from django.contrib.auth.models import User

# only makes sense to display SOME of these
class Visual(models.Model):
    system_name = models.CharField(max_length=100, null=True,)
    star_lum = models.FloatField()
    star_metal = models.FloatField()
    planet_eqtemp = models.FloatField()
    star_efftemp = models.FloatField()
    star_optmag = models.FloatField()
    star_grav = models.FloatField()
    star_mass = models.FloatField()
    planet_rad = models.FloatField()
    planet_eccen = models.FloatField()
    planet_dens = models.FloatField()
    planet_orbper = models.FloatField()
    planet_smaxis = models.FloatField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    saved_visuals = models.ManyToManyField(Visual)

    def __str__(self):
        return self.name

class Notes(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    system_name = models.ForeignKey(Visual, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
