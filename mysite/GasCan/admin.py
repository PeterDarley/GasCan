from django.contrib import admin
from .models import *

models_to_register = [Sponsor, PerkClass, Perk]
admin.site.register(models_to_register)

