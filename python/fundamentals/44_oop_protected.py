# Occasionally a parent class will provide methods for its
# This is generally called "protected" access and is denoted by a
# single _ prefix, in contrast to the double __ prefix of "private"
# access.
# Unlike private access, protected access is not enforced by the language.
# It is solely a convention.

class Person(object):
    '''
    A person class.

    @classvar SPECIES species of the person
    '''

    SPECIES = 'Homo sapiens sapiens'

    def __init__(self, first_name, last_name):
        '''
        The constructor of Person

        @param first_name first name of the person
        @type first_name str
        @param last_name
        '''

        # Use _ instead of __, indicating to the reader
        # that we will allow subclasses to directly access and/or modify
        # the attributes.
        # The "public" (i.e., any code accessing instances) can
        # access these attributes but they should not, by convention.
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    def _set_last_name(self, last_name):
        self.__last_name = last_name

    def get_name(self):
        '''
        Returns the full name of the person.

        Doesn't deal with multiple names.

        @return full name of the person
        @rtype str
        '''
        return self.first_name + ' ' + self.last_name


class TitledPerson(Person):
    def __init__(self, title, **kwds):
        Person.__init__(self, **kwds)
        self.__title = title

    @property
    def title(self):
        return self.__title

    def get_name(self):
        self._first_name = self._first_name.lstrip()
        return self.__title + ' ' + Person.get_name(self)


judi = Person(first_name=' Judi', last_name='Dench')
print judi._first_name # Can do this, but shouldn't
print judi.get_name()

judi_titled = TitledPerson(first_name=' Judi', last_name='Dench', title='Dame')
print judi_titled.get_name()
