# Create a dict from a generator expression that yields (key, value) tuples
print dict((i, "Number %u" % i) for i in xrange(10))

print dict((i, "Number %u" % i) for i in xrange(10) if i % 2 == 0)
