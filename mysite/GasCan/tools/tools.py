''' Holds any random tools used in GasCan. '''
from django.db.models.query import QuerySet


if __name__ == '__main__':
    """ Tools should never be run.  It only holds functions. """
    pass

def mached_name_choices(choices: list) -> list:
    """ Functin to return a list of tuples that contains the origional list doubled
    ['thing1', 'thing2'] becomes [('thing1', 'thing1'), ('thing2', thing2')] """
    
    tuple_choices: tuple = []
    for choice in choices:
        tuple_choices.append((choice, choice))
        
    return tuple_choices


def name_collector(query_set: QuerySet) -> str:
    """Returns the names from the provided QuerySet as a string """
    # This is gross.  There's probably a way to get the names in a QuerySet as a string in a single line
    name_collector: str = ''
    for my_object in query_set:
        if name_collector: name_collector += ', '
        name_collector += my_object.name
    return name_collector