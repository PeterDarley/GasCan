from django.db import models
from .tools.tools import mached_name_choices, name_collector
 
class BaseModel(models.Model):
    """ A base class to hold comon methods and attributes.  It's Abstract so Django won't make a table for it"""
    class Meta:
        abstract = True
    
    name = models.CharField(max_length=250, unique=True)
        
    def __str__(self) ->str:
        """ Generic stringify function.  Most objects will have a name so it's the default. """
        return self.name # pragma: no cover
  
    
class PerkClass(BaseModel):
    """ A class of perk, such as Badass or Military """
    class Meta:
        ordering = ['name']
        
    @property
    def perk_count(self) -> int:
        """ Returns the number of perks in this Perk Class """
        return Perk.objects.filter(perk_class=self).count()


class Sponsor(BaseModel):
    """ A Gaslands sponsor """
    class Meta:
        ordering = ['name']
        
    description = models.TextField()
    
    perk_classes = models.ManyToManyField(PerkClass, blank=True, related_name='sponsors')
    
    @property
    def perk_class_names(self) -> str:
        """Returns the names of the Perk Classes for this Sponsor as a string """
        return name_collector(self.perk_classes.all())

class VehicleType(BaseModel):
    """ A Gaslands vehicle type such as Car or Bike"""
    WEIGHTS = [(1, 'Lightweight'), (2, 'Middleweight'), (3, 'Heavyweight')]
    SPONSORS_RULE = mached_name_choices(['Include', 'Exclude'])
    
    sponsors = models.ManyToManyField(Sponsor, blank=True, related_name='vehicle_types')
    sponsors_rule = models.CharField(max_length=250, choices=SPONSORS_RULE, blank=True, null=True)
    # exclude(id_in=[p.id for p in processed])
    
    weight = models.PositiveSmallIntegerField(choices=WEIGHTS)
    hull = models.PositiveSmallIntegerField()
    handling = models.PositiveSmallIntegerField()
    max_gear = models.PositiveSmallIntegerField()
    crew = models.PositiveSmallIntegerField()
    build_slots = models.PositiveSmallIntegerField()
    cost = models.PositiveSmallIntegerField()
    trailer = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['weight', 'cost', 'name']
        
    @property
    def sponsor_names(self):
        """Returns the names of the Sponsors for this VehicleType as a string """
        return name_collector(self.sponsors.all())
    
    @property
    def perk_names(self):
        """Returns the names of the Perks for this VehicleTYpe as a string """
        return name_collector(self.perks.all())

    
class Perk(BaseModel):
    """ A Gaslands perk.  Can be categorized as part of a Sponsor, or a Perk Class, or a Vehicle Type """
    TYPES = mached_name_choices(['General', 'Sponsor'])
    
    perk_class = models.ForeignKey(PerkClass, on_delete=models.CASCADE, null=True, blank=True)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True, blank=True, related_name='perks')
    vehicle_types = models.ManyToManyField(VehicleType, blank=True, related_name='perks')

    description = models.TextField()
    type = models.CharField(max_length=250, choices=TYPES, default='General')
    cost = models.PositiveSmallIntegerField()
    
    class Meta:
        ordering = ['perk_class', 'sponsor', 'cost', 'name']
    
    @property
    def vehicle_type_names(self) -> str:
        """ returns the names of the vehicle types of the perk as a string """
        return name_collector(self.vehicle_types.all())
    
    def save(self, *args, **kwargs):
        """ Overrides save to ensure that the cost of the perk is positive """
        if self.cost < 0: self.cost = 0
        super(Perk, self).save(*args, **kwargs)
     
        
class WeaponUpgradeSpecialRule(BaseModel):
    """ A Gasslands special rule for weapons """
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
     
class Weapon(BaseModel):
    """ A Gaslands weapon """
    TYPES = mached_name_choices(['Crew', 'Shooting', 'Dropped'])
    RANGES = mached_name_choices(['Short', 'Medium', 'Long', 'Double', 'Dropped', 'Small Burst', 'Large Burst', 'Smash', 'Double/Dropped', 'Short/Medium', 'Short/Medium/Long'])
    
    type = models.CharField(max_length=250, choices=TYPES)
    range = models.CharField(max_length=250, choices=RANGES)
    attack_dice = models.CharField(max_length=10, null=True, blank=True)
    weapon_special_rules = models.ManyToManyField(WeaponUpgradeSpecialRule, blank=True, related_name='weapons')
    ammo = models.PositiveSmallIntegerField(null=True, blank=True)
    build_slots = models.PositiveSmallIntegerField()
    cost = models.PositiveBigIntegerField()
    sponsors = models.ManyToManyField(Sponsor, blank=True, related_name='weapons')
    special_rule = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['type', 'cost', 'name']
        
    @property
    def weapon_special_rule_names(self) -> str:
        """ returns the names of the Weapon Special Rules of the Weapon as a string """
        special_rule_names: str = name_collector(self.weapon_special_rules.all())
        if self.special_rule:
            if special_rule_names: special_rule_names += ", "
            special_rule_names += self.name
        return special_rule_names
    
    @property
    def sponsor_names(self) -> str:
        """ returns the names of the Sponsors for this Weapon as a string """
        return name_collector(self.sponsors.all())
    
    @property
    def attack_dice_pretty(self) -> str:
        """ returns the Attack Dice formatted nicely """
        if not self.attack_dice: return None
        dice_collector: str = ''
        for bit in self.attack_dice.split('/'):
            if dice_collector: dice_collector += "/"
            dice_collector += f"{bit}D6"
        return dice_collector
    
class Upgrade(BaseModel):
    """ A Gaslands Upgrade """
    upgrade_special_rules = models.ManyToManyField(WeaponUpgradeSpecialRule, blank=True, related_name='upgrades')
    ammo = models.PositiveSmallIntegerField(null=True, blank=True)
    has_facing = models.BooleanField(default=False)
    hull_adjust = models.SmallIntegerField(null=True, blank=True)
    handling_adjust = models.SmallIntegerField(null=True, blank=True)
    max_gear_adjust = models.SmallIntegerField(null=True, blank=True)
    crew_adjust = models.SmallIntegerField(null=True, blank=True)
    trailer_adjust = models.BooleanField('Is a trailer', default=False)
    weight_limit = models.CharField(max_length=250, choices=VehicleType.WEIGHTS, null=True, blank=True)
    sponsors = models.ManyToManyField(Sponsor, blank=True, related_name='upgrades')
    build_slots = models.SmallIntegerField()
    cost = models.SmallIntegerField()
    special_rule = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['cost', 'name']
        
    @property
    def upgrade_special_rule_names(self) -> str:
        """ returns the names of the Weapon Special Rules of the Upgrade as a string """
        special_rule_names: str = name_collector(self.upgrade_special_rules.all())
        if self.special_rule:
            if special_rule_names: special_rule_names += ", "
            special_rule_names += self.name
        return special_rule_names
    
    @property
    def sponsor_names(self) -> str:
        """ returns the names of the Sponsors for this Upgrade as a string """
        return name_collector(self.sponsors.all())
    
    
    
    
    