class MyTypeWithAddOperator(object):
    def __init__(self, x):
        if not isinstance(x, int):
            raise TypeError(type(x))
        self.x = x

    def __add__(self, other):
        if isinstance(other, MyTypeWithAddOperator):
            return self.x + other.x
        elif isinstance(other, int):
            return MyTypeWithAddOperator(self.x + other)
        else:
            raise TypeError(type(other))

    def __repr__(self):
        '''
        Return a string containing a printable representation of an object.
        For many types, this function makes an attempt to return a string
        that would yield an object with the same value when passed to eval(),
        '''
        return "%s(%s)" % (self.__class__.__name__, self.x)

print 'Result', MyTypeWithAddOperator(1) + 2
# Why doesn't this work? And how can we make it work?
# print 2 + MyTypeWithAddOperator(1)
