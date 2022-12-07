from django.db import models

class Perk_Type(models.Model):
    name = models.CharField(max_length=250)
    
