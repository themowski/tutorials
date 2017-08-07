class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name

me = Person(first_name='Minor', last_name='Gordon')
print me.get_name() # Fine
me.first_name = None # The attributes of Person are mutable
try:
    print me.get_name() # Adding None and a str, not so good
except Exception, e:
    print 'Error getting name:', e
print


# Head off this sort of error by ensuring that the attributes of
# Person cannot be modified once a Person is created.
# This is "defensive programming", which is much like "defensive
# driving": assume the other person will do something stupid.
# In all likelihood the other person will be you, six months from now.


class ImmutablePerson(object):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def get_name(self):
        return self.__first_name + ' ' + self.__last_name

me = ImmutablePerson(first_name='Minor', last_name='Gordon')
print me.get_name()
try:
    print me.first_name
except:
    print "But now we can't access me.first_name"
try:
    print me.__first_name
except:
    print "Can't do this either; first_name is 'private', only accessible within ImmutablePerson methods as self.__first_name"
print


class ImmutablePersonWithProperties(object):
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        print 'Called first_name()'
        return self.__first_name

    @property
    def last_name(self):
        print 'Called last_name()'
        return self.__last_name

    def get_name(self):
        return self.__first_name + ' ' + self.__last_name

me = ImmutablePersonWithProperties(first_name='Minor', last_name='Gordon')
print me.get_name()
print me.first_name # Looks like an access of the variable, but actually calls me.first_name()
print


# Even "immutable" classes like the above can be assigned arbitrary attributes:
me.other_name = 'Other name'
print me.other_name
del me.other_name # Remove the attribute, so that reading me.other_name will cause an exception
# But don't do this! If you add attributes dynamically in this way the reader
# has no way of knowing what attributes an instance has by looking at the class
# definition, which makes code hard to follow.
