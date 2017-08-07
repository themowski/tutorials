# A very brief overview

class Person(object): # Inherit the root class, object
    # Method = function declared within a class block
    # First positional parameter is always the instance, traditionally named "self" (vs. "this" in Java or C++)
    def __init__(self, first_name, last_name):
        self.SPECIES = "Homo sapiens sapiens"
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name

me = Person('Minor', 'Gordon') # Create/"instantiate" Person
                               # Implicitly calls the methods __init__(me, 1)
# me is an "instance" of Person
print me.get_name() # ~ calling Person.get_name(me)
# The dot syntax just means "access a method or a data member on an instance"
print me.first_name
print me.SPECIES # Not a method, just a variable attached to the instance

# So when you see 'class datetime' here:
# http://docs.python.org/2/library/datetime
# Calling datetime.now() creates an instance of the datetime class
# Then you access it with some_datetime.year, etc., just like me. above

# str is also a class, albeit a special one. When you do:
s = "A string"
# s is now an instance of the class str
print "String type", type(s), s.__class__.__name__
# And we're just calling methods on that instance:
s.capitalize() # str.capitalize(s)
# The str class is documented here:
# http://docs.python.org/2/library/stdtypes.html#string-methods

# The same goes for integers, floats, et al.
i = 129
print "Integer type", type(i)
print "Number of bits in the binary representation of the integer", i.bit_length()

# Unlike some other languages such as C or Java, there are no primitive types in Python.
# Everything is an instance of some class.
