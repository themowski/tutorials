class Person(object):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name


class TitledPerson(Person):
    def __init__(self, title, **kwds):
        Person.__init__(self, **kwds)
        self.__title = title

    @property
    def title(self):
        return self.__title

    # This get_name replaces the version in Person for TitledPerson instances
    def get_name(self):
        return self.__title + ' ' + Person.get_name(self)


judi = TitledPerson(first_name='Judi', last_name='Dench', title='Dame')
print judi.get_name()
print judi.title

jeremy = Person(first_name='Jeremy', last_name='Paxman')
print jeremy.get_name()
