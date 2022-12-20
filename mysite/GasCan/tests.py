from django.test import TestCase
import inspect

from .models import PerkClass, Perk, Sponsor, VehicleType, Weapon, WeaponUpgradeSpecialRule, Upgrade
from .tools import mached_name_choices

# Set up elves to make objects for the tests
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


# Start the actual tests
class ToolsTests(TestCase):
    def test_mached_name_choices_should_return_list_of_tuples(self):
        """ mached_name_choices should return a list of duplicated tuples """
        self.assertTrue(mached_name_choices(['thing1', 'thing2']) == [('thing1', 'thing1'), ('thing2', 'thing2')])
    

class PerkModelTests(TestCase):
    def test_should_have_positive_cost(self):
        """ Perks should not be able to have negative cost """
        perk_class = a_perk_class()
        perk = a_perk(perk_class=perk_class, cost=-1)
        
        self.assertGreater(perk.cost, -1)
        
    def test_should_cascade_delete_correctly(self):
        """Perks should only cascade delete when their particular parent is deleted"""
        starting_perk_count = Perk.objects.all().count();
        
        sponsor = a_sponsor()
        sponsor_perk = a_perk(sponsor=sponsor)
        
        perk_class = a_perk_class()
        class_perk = a_perk(perk_class=perk_class)
        
        self.assertIs(Perk.objects.all().count(), starting_perk_count+2)
        
        perk_class.delete()
        self.assertIs(Perk.objects.all().count(), starting_perk_count+1)
        
        sponsor.delete()
        self.assertIs(Perk.objects.all().count(), starting_perk_count+0)
        
    def test_perk_class_should_return_count_of_its_perks(self):
        """ Perk Class should report correct number of child Perks """
        perk_class = a_perk_class()
        self.assertEqual(perk_class.perk_count, 0)
        
        perk1, perk2 = some_perks(2, perk_class=perk_class)
        
        self.assertEqual(perk_class.perk_count, 2)
        
    def test_perk_should_return_vehicle_types_as_str(self):
        """ Perk should report the correct vehicle types as a string """
        #vehicle_type_1 = VehicleType(name='Vehicle Type 1', weight=1, hull=1, handling=1, max_gear=1, crew=1, build_slots=1, cost=1)
        #vehicle_type_1.save()
        
        perk = a_perk()
        vehicle_type_1, vehicle_type_2 = some_vehicle_types(2)
        
        perk.vehicle_types.add(vehicle_type_1)
        perk.vehicle_types.add(vehicle_type_2)
        
        self.assertEqual(perk.vehicle_type_names, f'{vehicle_type_1.name}, {vehicle_type_2.name}')
        
    def test_sponsor_should_return_perk_classes_as_str(self):
        """ Sponsors should report the correct perk classes as a string """
        sponsor = a_sponsor()
        perk_class_1, perk_class_2 = some_perk_classes(2)
        
        sponsor.perk_classes.add(perk_class_1)
        sponsor.perk_classes.add(perk_class_2)
        
        self.assertEqual(sponsor.perk_class_names, f'{perk_class_1.name}, {perk_class_2.name}')
        
    def test_vehicle_types_should_return_sponsors_as_str(self):
        """ Vehicle Types should report the correct Sponsors as a string """
        sponsor_1, sponsor_2 = some_sponsors(2)
        vehicle_type = a_vehicle_type()
        
        vehicle_type.sponsors.add(sponsor_1)
        vehicle_type.sponsors.add(sponsor_2)
        
        self.assertEqual(vehicle_type.sponsor_names, f'{sponsor_1.name}, {sponsor_2.name}')
        
    def test_vehicle_types_should_return_perks_as_str(self):
        """ Vehicle Types should report the correct Perks as a string """
        perk_1, perk_2 = some_perks(2)
        vehicle_type = a_vehicle_type()
        vehicle_type.perks.add(perk_1)
        vehicle_type.perks.add(perk_2)
        
        self.assertEqual(vehicle_type.perk_names, f'{perk_1.name}, {perk_2.name}')
        
    def test_weapon_attack_dice_pretty_formatting_correct(self):
        """ Weapon Dice should split at the / and had D6 appended to each die count """
        weapon_1 = a_weapon(attack_dice='1')
        weapon_2 = a_weapon(attack_dice='1/2/3')
        weapon_3 = a_weapon(attack_dice=None)
        
        self.assertEqual(weapon_1.attack_dice_pretty, '1D6')
        self.assertEqual(weapon_2.attack_dice_pretty, '1D6/2D6/3D6')
        self.assertEqual(weapon_3.attack_dice_pretty, None)
        
    def test_weapons_should_return_weapon_special_rules_as_str(self):
        """ Weapons should repot the correct Weapon Special Rules as a string """
        weapon_special_rule_1, weapon_special_rule_2 = some_weapon_special_rules(2)
        weapon = a_weapon(special_rule='A special rule')
        
        weapon.weapon_special_rules.add(weapon_special_rule_1)
        weapon.weapon_special_rules.add(weapon_special_rule_2)
        
        self.assertEqual(weapon.weapon_special_rule_names, f'{weapon_special_rule_1.name}, {weapon_special_rule_2.name}, {weapon.name}')
        
    def test_upgrades_should_return_upgrade_special_rules_as_str(self):
        """ Upgrades should report the correct Upgrade Special Rules as a string """
        #upgrade_special_rule_1 = WeaponUpgradeSpecialRule(name='Upgrade Special Rule 1', description='Upgrade Special Rule 1')
        #upgrade_special_rule_1.save()
        
        #upgrade_special_rule_2 = WeaponUpgradeSpecialRule(name='Upgrade Special Rule 2', description='Upgrade Special Rule 2')
        #upgrade_special_rule_2.save()
        
        #upgrade = Upgrade(name='Upgrade', build_slots=0, cost=0, special_rule='A special rule')
        #upgrade.save()
        
        upgrade_special_rule_1, upgrade_special_rule_2 = some_upgrade_special_rules(2)
        upgrade = an_upgrade(special_rule='A special rule!')
        
        upgrade.upgrade_special_rules.add(upgrade_special_rule_1)
        upgrade.upgrade_special_rules.add(upgrade_special_rule_2)
        
        self.assertEqual(upgrade.upgrade_special_rule_names, f'{upgrade_special_rule_1.name}, {upgrade_special_rule_2}, {upgrade.name}')
        
        
        
        