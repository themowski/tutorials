import sys

i = 1
print 'Integer class', i.__class__
print 'Integer class name', i.__class__.__name__
print 'Integer class module', i.__class__.__module__
print 'Integer doc'
print int.__doc__
print
class MyType(object):
    pass
print 'MyType module', MyType().__class__.__module__
print 'MyType module name (not the module object!)', MyType.__module__
print 'MyType file', sys.modules[MyType.__module__]
print 'MyType methods:'
for method_name in dir(MyType()):
    print method_name
print
print 'MyType __dict__:',
inst = MyType()
inst.x = 1 # Can assign arbitrary attributes. Where do they go?
print inst.__dict__ # Instances are backed by dicts.
inst.__dict__['y'] = 2
print ["%s=%s" % (attr, getattr(inst, attr))
       for attr in dir(inst)
       if attr[0] != '_']