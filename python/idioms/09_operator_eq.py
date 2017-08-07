# See the operator module for the list of available operators
# https://docs.python.org/2/library/operator.html

class MyTypeWithEqOperator(object):
    def __init__(self, x):
        if not isinstance(x, int):
            raise TypeError(type(x))
        self.x = x

    def __eq__(self, other):
        '''
        Override the == comparison operator
        '''
        if not isinstance(other, MyTypeWithEqOperator):
            return False
        return self.x == other.x

class MyTypeWithoutEqOperator(object):
    def __init__(self, x):
        self.x = x

# The classic use case is complex numbers.

# The default == compares object ids
print 'Equals with overloaded operator', MyTypeWithEqOperator(1) == MyTypeWithEqOperator(1)
print 'Equals without overloaded operator', MyTypeWithoutEqOperator(1) == MyTypeWithoutEqOperator(1)
# because
left = MyTypeWithoutEqOperator(1)
right = MyTypeWithoutEqOperator(1)
print "%s != %s is %s" % (id(left), id(right), id(left) != id(right))
