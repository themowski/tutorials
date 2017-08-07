class Person:
    SPECIES = 'Homo sapiens sapiens'

    # Method = function declared within a class block
    # First positional parameter is always the instance, traditionally named "self" (vs. "this" in Java or C++)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_nothing(self):
        pass

    def get_name(self):
        self.do_nothing()
        return self.first_name + ' ' + self.last_name

#s = str('Words and words')
#s.split()
me = Person('Minor', 'Gordon') # Create/"instantiate" Person
                               # Implicitly calls Person.__init__(me, 'Minor', 'Gordon')
other = Person('John', 'Doe')
other.get_name()
# me is an "instance" of Person
print me.get_name() # ~ calling Person.get_name(me)
# The dot syntax just means "access a method or a data attribute on an instance"
print me.first_name

# SPECIES is a property of all people, independent of instances
# It can be accessed via the class
print 'Species of Person', Person.SPECIES
# or via an instance
print 'My species', me.SPECIES
