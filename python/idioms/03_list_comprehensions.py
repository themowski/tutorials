# Create a list with a generator expression
print ["Number %u" % i for i in xrange(10)]
print

# Filter elements from the generator expression first
print \
["Number %u" % i
 for i in xrange(10)
 if i % 2 == 0]
print

# Some functions on sequences will take the generator expression directly
print ', '.join("Number %u" % i for i in xrange(10))
