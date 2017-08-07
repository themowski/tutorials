class MyTypeWithGetAttrOperator(object):
    def __init__(self, x):
        if not isinstance(x, int):
            raise TypeError(type(x))
        self.x = x

    def __getattr__(self, attr):
        # Called if normal attribute lookup fails
        return 'Brought to you by the attribute ' + attr

    def __getitem__(self, key):
        # Act like a dictionary
        return 'Brought to you by the key ' + key

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.x)

inst = MyTypeWithGetAttrOperator(1)
print 'x =', inst.x
print 'y =', inst.y
print 'z =', inst['z']