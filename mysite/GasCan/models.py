from django.db import models
 
class AbstractBase(models.Model):
    """ A base class to hold comon methods and attributes.  It's Abstract so Django won't make a table for it"""
    class Meta:
        abstract = True
        
    def __str__(self):
        """ Generic stringify function.  Most objects will have a name so it's the default. """
        return self.name

class Sponsor(AbstractBase):
    """ A Gaslands sponsor """
    name = models.CharField(max_length=250)
    description = models.TextField()
    
class PerkClass(AbstractBase):
    """ A class of perk, such as Badass or Military """
    name = models.CharField(max_length=250)
    
class Perk(AbstractBase):
    """ A Gaslands perk.  Can be categorized as part of a Sponsor, or a Perk Class.  The  """
    PERK_TYPES = [
        ('General', 'General'),
        ('Sponsor', 'Sponsor')]
    
    perk_class = models.ForeignKey(PerkClass, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=250, choices=PERK_TYPES, default='General')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    cost = models.PositiveSmallIntegerField()
    
    def save(self, *args, **kwargs):
        """ Overrides save to ensure that the cost of the perk is positive """
        if self.cost < 0: self.cost = 0
        super(Perk, self).save(*args, **kwargs)