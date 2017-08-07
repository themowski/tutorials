# Iterate over an infinite sequence = the sequence can't fit in memory
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i, x in enumerate(fib()):
    print x,
    if i == 15:
        break
print


# Also useful if getting the next element is expensive
def expensivefunction(i):
    # e.g., get a URL
    return i * 2

def expensivegenerator():
    for i in xrange(10):
        yield expensivefunction(i)
    raise StopIteration # Have to tell the caller that is iterating over the generated elements that we're done

for result in expensivegenerator():
    print result,
