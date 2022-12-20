from django.contrib import admin
from .models import Sponsor, PerkClass, Perk, VehicleType, WeaponUpgradeSpecialRule, Weapon, Upgrade


# Set up the inlines
class Perk_PerkClass_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for perk classes. Excludes the type so all perks that are part of perk classes have a General type. """
    model = Perk
    extra = 0
    exclude = (['sponsor', 'type', 'vehicle_types'])
    
    
class Perk_Sponsor_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for sponsors. """
    model = Perk
    extra = 0
    exclude = (['perk_class', 'vehicle_types'])
    
    
class Perk_VehicleType_InLine(admin.TabularInline):
    """ Provides the inline formatting for the perks for vehicle types. """
    model = Perk.vehicle_types.through
    extra = 0
    exclude = (['sponsor', 'type', 'perk_class'])


class WeaponSpecialRuleInline(admin.TabularInline):
    """ Provides the inline formatting for the WeaponUpgradeSpecialRule inline """
    model = WeaponUpgradeSpecialRule


# Build admin pages
@admin.register(PerkClass)
class PerkClassAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Perk Classes """
    inlines = [Perk_PerkClass_InLine]
    list_display = ('name', 'perk_count')


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Sponsors """
    inlines = [Perk_Sponsor_InLine]
    list_display = ('name', 'perk_class_names')
    
    
@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    """ Provides the admin interface for VehicleType """
    inlines = [Perk_VehicleType_InLine]
    list_display = ('name', 'weight', 'hull', 'handling', 'max_gear', 'crew', 'build_slots', 'perk_names', 'cost')

@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Perks """
    list_display = ('name', 'perk_class', 'sponsor', 'vehicle_type_names', 'cost')


@admin.register(WeaponUpgradeSpecialRule)
class WeaponSpeacialRuleAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Weapon """
    
    
@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Weapon """
    list_display = ('name', 'type', 'range', 'attack_dice_pretty', 'build_slots', 'cost', 'weapon_special_rule_names', 'ammo', 'sponsor_names')
    #list_editable = ('type',)

@admin.register(Upgrade)
class UpgradeAdmin(admin.ModelAdmin):
    """ Provides the admin interface for Upgrade """
    list_display = ('name', 'build_slots', 'cost', 'upgrade_special_rule_names', 'sponsor_names')

