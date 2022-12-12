from django.db import models
 
class AbstractBase(models.Model):
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

class Sponsor(AbstractBase):
    name = models.CharField(max_length=250)
    description = models.TextField()
    
class PerkClass(AbstractBase):
    name = models.CharField(max_length=250)
    
class Perk(AbstractBase):
    PERK_TYPES = [
        ('General', 'General'),
        ('Sponsor', 'Sponsor')]
    
    perk_class = models.ForeignKey(PerkClass, on_delete=models.CASCADE, null=True, blank=True)
    perk_type = models.CharField(max_length=250, choices=PERK_TYPES, default='General')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    cost = models.PositiveSmallIntegerField()
    
    def save(self, *args, **kwargs):
        if self.cost < 0: self.cost = 0
        super(Perk, self).save(*args, **kwargs)
        
        