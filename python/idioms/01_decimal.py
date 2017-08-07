from decimal import Decimal # Arbitrary-precision floating point

# https://en.wikipedia.org/wiki/Floating_point
# The Python float type is backed by a C double (64-bit)
# Potentially imprecise but faster because its operations are in hardware
x = 1.03 - .42
print "Fixed-width floating point result %0.20f" % x
print
# Decimal is more precise but slower because its operations are in software
x = Decimal('1.03') - Decimal('0.42')
print 'Decimal result', x
