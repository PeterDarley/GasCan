from django.contrib import admin
from .models import Sponsor, PerkClass, Perk, VehicleType, WeaponSpecialRule, Weapon

# Set up the inlines
class Perk_PerkClass_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for perk classes. Excludes the type so all perks that are part of perk classes have a General type. """
    model = Perk
    extra = 0
    exclude = (['sponsor', 'type', 'vehicle_type'])
    
class Perk_Sponsor_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for sponsors. """
    model = Perk
    extra = 0
    exclude = (['perk_class', 'vehicle_type'])
    
class Perk_VehicleType_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for vehicle types. """
    model = Perk.vehicle_type.through
    extra = 0
    exclude = (['sponsor', 'type', 'perk_class'])

class WeaponSpecialRuleInline(admin.TabularInline):
    """ Provides the inline formatting for the WeaponSpecialRule inline """
    model = WeaponSpecialRule

# Build admin pages
@admin.register(PerkClass)
class PerkClassAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Perk Classes """
    inlines = [Perk_PerkClass_InLine]

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Sponsors """
    inlines = [Perk_Sponsor_InLine]
    
@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    """ Provides the admin interface for VehicleType """
    inlines = [Perk_VehicleType_InLine]
    
@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Weapon """
    
admin.site.register(Perk)
admin.site.register(WeaponSpecialRule)
