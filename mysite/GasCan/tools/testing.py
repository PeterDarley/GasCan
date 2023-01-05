""" Holds test object setup stuff """

from ..models import PerkClass, Perk, Sponsor, VehicleType, Weapon, WeaponUpgradeSpecialRule, Upgrade
import inspect

if __name__ == '__main__':
    """ Tools should never be run.  It only holds functions. """
    pass # pragma: no cover


object_counts = {}

def next_count() -> int:
    """ Get new count of objects.  Used to make sure objects don't have the same name """
    count_object = inspect.stack()[1].function
    if count_object not in object_counts: object_counts[count_object] = 0
    object_counts[count_object] += 1
    return object_counts[count_object]


def a_sponsor() -> Sponsor:
    """ Get a Sponsor fot testing """
    key = next_count()
    sponsor = Sponsor(name=f'Sponsor {key}', description = f'Sponsor {key}')
    sponsor.save()
    return sponsor

def some_sponsors(count: int, **kwargs) ->list:
    """ Get some Sponsors for testing """
    sponsors = []
    for i in range(count):
        sponsors.append(a_sponsor(**kwargs))
    return sponsors


def a_perk_class() -> PerkClass:
    """ Get a Perk Class for testing """
    key = next_count()
    perk_class = PerkClass(name=f'Perk Class {key}')
    perk_class.save()
    return perk_class

def some_perk_classes(count: int, **kwargs) -> list:
    """ Get count Perk Classes for testing """
    perk_classes = []
    for i in range(count):
        perk_classes.append(a_perk_class(**kwargs))
    
    return perk_classes


def a_perk(*, perk_class: PerkClass=None, sponsor: Sponsor=None, cost: int=0) -> Perk:
    """ Get a Perk for testing """
    key = next_count()
    perk = Perk(name=f'Perk {key}', 
                description=f'Perk {key}', 
                perk_class=perk_class,
                sponsor=sponsor, 
                cost=cost)
    perk.save()
    return perk


def some_perks(count: int, **kwargs) -> list:
    """ Get count Perks for testing """
    perks = []
    for i in range(count):
        perks.append(a_perk(**kwargs))
        
    return perks


def a_vehicle_type() -> VehicleType:
    """ Get a generic VehicleType for testing """
    key = next_count()
    vehicle_type = VehicleType(name=f'Vehicle Type {key}', weight=1, hull=1, handling=1, max_gear=1, crew=1, build_slots=1, cost=1)
    vehicle_type.save()
    return vehicle_type


def some_vehicle_types(count: int, **kwargs) -> list:
    """ Get some Vehicle Types for testing """
    vehicle_types = []
    for i in range(count):
        vehicle_types.append(a_vehicle_type(**kwargs))
    
    return vehicle_types


def a_weapon_special_rule() -> WeaponUpgradeSpecialRule:
    """ Get a Weapon Special Rule for testing """
    key = next_count()
    weapon_special_rule = WeaponUpgradeSpecialRule(name=f'Weapon Special Rule {key}', description='Weapon Special Rule {key}')
    weapon_special_rule.save()
    return weapon_special_rule

def some_weapon_special_rules(count, **kwargs) -> list:
    """ Get some Weapon Special Rules for testing """
    weapon_special_rules = []
    for i in range(count):
        weapon_special_rules.append(a_weapon_special_rule(**kwargs))
    
    return weapon_special_rules


def a_weapon(*, attack_dice: str='0', range: str='Short', build_slots: int=1, cost: int=1, special_rule: str=None) -> Weapon:
    """ Get a Weapon for testing """
    key = next_count()
    weapon = Weapon(name=f'Weapon {key}', attack_dice=attack_dice, range=range, build_slots=build_slots, cost=cost, special_rule=special_rule)
    weapon.save()
    return weapon

def some_weapons(count, **kwargs) -> list:
    """ Get some Weapons for testing. """
    weapons = []
    for i in range(count):
        weapons.append(a_weapon(**kwargs))
    
    return weapons


def an_upgrade_special_rule() -> WeaponUpgradeSpecialRule:
    """ Get an Upgrade Special Rule """
    key = next_count()
    upgrade_special_rule = WeaponUpgradeSpecialRule(name = f'Upgrade Special Rule {key}', description = f'Upgrade Special Rule {key}')
    upgrade_special_rule.save()
    return upgrade_special_rule

def some_upgrade_special_rules(count, **kwargs):
    """ Get some Upgrade Special Rules for testing. """
    upgrade_special_rules = []
    for i in range(count):
        upgrade_special_rules.append(an_upgrade_special_rule(**kwargs))
    
    return upgrade_special_rules


def an_upgrade(*, build_slots: int=0, cost: int=0, special_rule: str=None) -> Upgrade:
    """ Get an Upgrade for testing. """
    key = next_count()
    upgrade = Upgrade(name=f'Upgrade {key}', build_slots=build_slots, cost=cost, special_rule=special_rule)
    upgrade.save()
    return upgrade

def some_upgrades(count, **kwargs) -> list:
    upgrades = []
    for i in range(count):
        upgrades.append(an_upgrade(**kwargs))
    
    return upgrades
