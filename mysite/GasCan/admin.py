from django.contrib import admin
from .models import Sponsor, PerkClass, Perk

class Perk_PerkClass_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for perk classes. Excludes the type so all perks that are part of perk classes have a General type. """
    model = Perk
    extra = 1
    exclude = (['sponsor', 'type'])
    
class Perk_Sponsor_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for sponsors. """
    model = Perk
    extra = 1
    exclude = (['perk_class'])
    
@admin.register(PerkClass)
class PerkClassAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Perk Classes """
    inlines = [Perk_PerkClass_InLine]
    
@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Sponsors """
    inlines = [Perk_Sponsor_InLine]