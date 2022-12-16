from django.test import TestCase

from .models import PerkClass, Perk, Sponsor, VehicleType
from .tools import mached_name_choices

class ToolsTests(TestCase):
    def test_mached_name_choices_should_return_list_of_tuples(self):
        """ mached_name_choices should return a list of duplicated tuples """
        
        self.assertTrue(mached_name_choices(['thing1', 'thing2']) == [('thing1', 'thing1'), ('thing2', 'thing2')])
    

class PerkModelTests(TestCase):
    def test_should_have_positive_cost(self):
        """ Perks should not be able to have negative cost """
        perk_class = PerkClass(name='Test Perks')
        perk_class.save()
        
        perk = Perk(name='Bad Perk', cost=-1, perk_class=perk_class, description="A Perk")
        perk.save()
        
        perk_class.full_clean()
        perk.full_clean()
        self.assertGreater(perk.cost, -1)
        
    def test_should_cascade_delete_correctly(self):
        """Perks should only cascade delete when their particular parent is deleted"""
        starting_perk_count = Perk.objects.all().count();
        
        perk_class = PerkClass(name='Test Perk')
        perk_class.save()
        
        sponsor = Sponsor(name='Test Sponsor', description='This is a test')
        sponsor.save()
        
        sponsor_perk = Perk(name='Sponsor Perk', description='Sponsor Perk', sponsor=sponsor, cost=0)
        sponsor_perk.save()
        
        perk_class = PerkClass(name='Test Perks')
        perk_class.save()
        
        class_perk = Perk(name='Bad Perk', cost=-1, perk_class=perk_class, description="A Perk")
        class_perk.save()
        
        self.assertIs(Perk.objects.all().count(), starting_perk_count+2)
        
        perk_class.delete()
        self.assertIs(Perk.objects.all().count(), starting_perk_count+1)
        
        sponsor.delete()
        self.assertIs(Perk.objects.all().count(), starting_perk_count+0)
        
    def test_perk_class_should_return_count_of_its_perks(self):
        """ Perk Class should report correct number of child Perks """
        
        perk_class = PerkClass(name='Test Perk')
        perk_class.save()
        
        self.assertEqual(perk_class.perk_count, 0)
        
        perk1 = Perk(name='Perk 1', perk_class=perk_class, description='Perk 1', cost=0)
        perk1.save()
        
        perk2 = Perk(name='Perk 2', perk_class=perk_class, description='Perk 2', cost=0)
        perk2.save()
        
        self.assertEqual(perk_class.perk_count, 2)
        
    def test_perk_should_return_vehicle_types_as_str(self):
        """ Perk should report the correct vehicle types as a string """
        
        vehicle_type_1 = VehicleType(name='Vehicle Type 1', hull=1, handling=1, max_gear=1, crew=1, build_slots=1, cost=1)
        vehicle_type_1.save()
        
        vehicle_type_2 = VehicleType(name='Vehicle Type 2', hull=1, handling=1, max_gear=1, crew=1, build_slots=1, cost=1)
        vehicle_type_2.save()
        
        perk = Perk(name='Perk', description='Perk', cost=0)
        perk.save()
        
        perk.vehicle_types.add(vehicle_type_1)
        perk.vehicle_types.add(vehicle_type_2)
        
        self.assertEqual(perk.vehicle_type_names, 'Vehicle Type 1, Vehicle Type 2')
        
    def test_sponsor_should_return_perk_classes_as_str(self):
        """ Sponsors should report the correct perk classes as a string """
        
        perk_class_1 = PerkClass(name='Perk Class 1')
        perk_class_1.save()
        
        perk_class_2 = PerkClass(name='Perk Class 2')
        perk_class_2.save()
        
        sponsor = Sponsor(name='Sponsor', description='Sponsor')
        sponsor.save();
        
        sponsor.perk_classes.add(perk_class_1)
        sponsor.perk_classes.add(perk_class_2)
        
        self.assertEqual(sponsor.perk_class_names, 'Perk Class 1, Perk Class 2')
        
        
        