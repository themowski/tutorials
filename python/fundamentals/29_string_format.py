import random

# Ugly way to create strings from different variables
x = random.randint(-100, 100)
y = random.randint(-100, 100)
print 'First random number is ' + str(x) + ' and second random number is ' + str(y)

# Better way:
print 'First random number is %d and second random number is %d' % (x, y)
# Works like C printf() or Java String.format()
# Many options to control formatting, like
print 'Octal x %o' % x
# See https://docs.python.org/2/library/string.html#format-specification-mini-language

# We can also supply named replacements instead of using positions, as above
print 'First random number is %(x)d and second random number is %(y)d (and again in a different format: %(y)04d)' % {'x': x, 'y': y}
# Because we can re-use the same variables %(x) and %(y) multiple times in the output string

# Common idiom:
print 'Random numbers %(x)d and %(y)d (different format: %(y)04d' % locals()
# locals() is a dictionary of all variables defined in the scope
print 'Locals', locals()

def f():
    globals()['x'] = 1
    locals()['z'] = 2 # Same as z = 2
    if 3 < 5:
        x = 2
    print locals()
    return 'String with %(z)d' % locals()
f()
print 'x is', x