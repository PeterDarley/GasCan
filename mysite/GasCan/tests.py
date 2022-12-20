from django.test import TestCase

# from .models import PerkClass, Perk, Sponsor, VehicleType, Weapon, WeaponUpgradeSpecialRule, Upgrade
from .tools.tools import mached_name_choices
from .tools.testing import *

# Set up elves to make objects for the tests


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
        upgrade_special_rule_1, upgrade_special_rule_2 = some_upgrade_special_rules(2)
        upgrade = an_upgrade(special_rule='A special rule!')
        
        upgrade.upgrade_special_rules.add(upgrade_special_rule_1)
        upgrade.upgrade_special_rules.add(upgrade_special_rule_2)
        
        self.assertEqual(upgrade.upgrade_special_rule_names, f'{upgrade_special_rule_1.name}, {upgrade_special_rule_2}, {upgrade.name}')
        
        
        
        