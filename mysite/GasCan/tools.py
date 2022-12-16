'''
Created on Dec 13, 2022

@author: pdarley

Holds any random tools used in GasCan
'''

def mached_name_choices(choices: list) -> list:
    """ Functin to return a list of tuples that contains the origional list doubled
    ['thing1', 'thing2'] becomes [('thing1', 'thing1'), ('thing2', thing2')] """
    
    tuple_choices: tuple = []
    for choice in choices:
        tuple_choices.append((choice, choice))
        
    return tuple_choices