class Person(object): # Person inherits object, the root class
    def __init__(self, first_name, last_name):
        object.__init__(self)
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name

# Student inherits Person; a student "is-a" person
# https://en.wikipedia.org/wiki/Liskov_substitution_principle
class Student(Person):
    def __init__(self, university_name, **kwds):
        Person.__init__(self, **kwds)
        self.university_name = university_name


brian = Student(first_name='Brian', last_name='Lois', university_name='Iowa State University')
minor = Person(first_name='Minor', last_name='Gordon')


def Person_get_name(person_dict):
    return person_dict['first_name'] + ' ' + person_dict['last_name']

person_dict = {'first_name': 'Brian', 'last_name': 'Lois'}

print Person.get_name(person_dict)
person_dict['first_name'] = None
print Person.get_name(person_dict)
print brian.get_name()

if isinstance(brian, Student):
    print 'Brian is a student'
else:
    print 'Brian is not a student'

if isinstance(brian, Person):
    print 'Brian is a person'
else:
    print 'Brian is not a person'


if isinstance(minor, Student):
    print 'Minor is a student'
else:
    print 'Minor is not a student'

if isinstance(minor, Person):
    print 'Minor is a person'
else:
    print 'Minor is not a person'
