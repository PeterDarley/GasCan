from django.test import TestCase

from .models import PerkClass, Perk, Sponsor
from .tools import mached_name_choices

class ToolsTests(TestCase):
    def test_mached_name_choices_should_return_list(self):
        """ mached_name_choices should return a list of something """
        
        self.assertTrue(mached_name_choices(['thing1', 'thing2']) == [('thing1', 'thing1'), ('thing2', 'thing2')])
        
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
        
        self.assertIs(Perk.objects.all().count(), 2)
        
        perk_class.delete()
        self.assertIs(Perk.objects.all().count(), 1)
        
        sponsor.delete()
        self.assertIs(Perk.objects.all().count(), 0)
        