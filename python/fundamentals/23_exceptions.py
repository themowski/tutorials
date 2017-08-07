import random

def f(a_list):
    element_i = random.randint(0, len(a_list))
    try:
        element = a_list[element_i]
    except IndexError:
        print "Element was not in the list", element_i

a_list = 'ya see i go by the code of the doctor of the mix'.split()
for i in xrange(100):
    f(a_list)


# Many different kinds of exceptions:
try:
    int('not an integer')
except ValueError, e:
    print "Something went wrong:", e

try:
    undefined_variable + 1
except NameError, e:
    print "Got a NameError:", e