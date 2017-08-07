# Advanced Python starts to look like functional programming,
# using fewer statements and more expressions without side effects.

from random import randint
from itertools import ifilter, permutations

long_list = [randint(0, 100) for i in xrange(100)]

# ifilter(predicate callable, iterable) -> iterates over iterable,
# yields elements that satisfy the predicate
for x in ifilter(lambda x: x % 3 == 0, long_list):
    print "Divisible by 3", x

# list(iterable) constructs a list by iterating over iterable
divisible_by_3 = list(ifilter(lambda x: x % 3 == 0, long_list))
# Same as
divisible_by_3 = []
for x in ifilter(lambda x: x % 3 == 0, long_list):
    divisible_by_3.append(divisible_by_3)

# Many other functions on iterables:
print tuple(permutations((1, 2, 3)))
