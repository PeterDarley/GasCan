from django.db import models
from .tools import mached_name_choices
 
class AbstractBase(models.Model):
    """ A base class to hold comon methods and attributes.  It's Abstract so Django won't make a table for it"""
    
    class Meta:
        abstract = True
    
    name = models.CharField(max_length=250)
        
    def __str__(self) ->str:
        """ Generic stringify function.  Most objects will have a name so it's the default. """
        return self.name

class Sponsor(AbstractBase):
    """ A Gaslands sponsor """
    
    description = models.TextField()
    
class PerkClass(AbstractBase):
    """ A class of perk, such as Badass or Military """
    
    class Meta:
        ordering = ['name']
        
    @property
    def perk_count(self) -> int:
        """ Returns the number of perks in this Perk Class """
        return Perk.objects.filter(perk_class=self).count()

class VehicleType(AbstractBase):
    """ A Gaslands vehicle type such as Car or Bike"""
    
    WEIGHTS = mached_name_choices(['Lightweight', 'Middleweight','Heavyweight'])
    
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True, blank=True)
    
    weight = models.CharField(max_length=250, choices=WEIGHTS)
    hull = models.PositiveSmallIntegerField()
    handling = models.PositiveSmallIntegerField()
    max_gear = models.PositiveSmallIntegerField()
    crew = models.PositiveSmallIntegerField()
    build_slots = models.PositiveSmallIntegerField()
    cost = models.PositiveSmallIntegerField()
    trailer = models.BooleanField(default=False)
    
class Perk(AbstractBase):
    """ A Gaslands perk.  Can be categorized as part of a Sponsor, or a Perk Class, or a Vehicle Type """
    
    TYPES = mached_name_choices(['General', 'Sponsor'])
    
    perk_class = models.ForeignKey(PerkClass, on_delete=models.CASCADE, null=True, blank=True)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_types = models.ManyToManyField(VehicleType, blank=True)

    description = models.TextField()
    type = models.CharField(max_length=250, choices=TYPES, default='General')
    cost = models.PositiveSmallIntegerField()
    
    class Meta:
        ordering = ['cost', 'name']
    
    @property
    def vehicle_type_names(self) -> str:
        """ returns the names of the vehicle types of the perk as a string """
        name_collector = ''
        for vehicle_type in self.vehicle_types.all():
            if name_collector: name_collector += ', '
            name_collector += vehicle_type.name
            
        return name_collector
    
    def save(self, *args, **kwargs):
        """ Overrides save to ensure that the cost of the perk is positive """
        if self.cost < 0: self.cost = 0
        super(Perk, self).save(*args, **kwargs)
        
class WeaponSpecialRule(AbstractBase):
    """ A Gasslands special rule for weapons """
    
    description = models.TextField()
     
class Weapon(AbstractBase):
    """ A Gaslands weapon """
    
    RANGES = mached_name_choices(['Short', 'Medium', 'Long', 'Double', 'Dropped', 'Small Burst', 'Large Burst', 'Smash', 'Double/Dropped', 'Short/Medium', 'Short/Medium/Long'])
    
    weapon_special_rule = models.ManyToManyField(WeaponSpecialRule, blank=True)
    sponsor = models.ManyToManyField(Sponsor, blank=True)
    
    range = models.CharField(max_length=250, choices=RANGES)
    attack_dice = models.CharField(max_length=10, null=True, blank=True)
    slots = models.PositiveSmallIntegerField(null=True, blank=True)
    ammo = models.PositiveSmallIntegerField(null=True, blank=True)
    
    
    
    
    
    