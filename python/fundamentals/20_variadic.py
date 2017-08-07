# You will see this often in matplotlib:
def f(*args, **kwds):
    print "f"
    print "Positional arguments", type(args), args
    print "Keyword arguments", type(kwds), kwds
    print

f('regents.csv', tree=True)
f(csv_file_path='regents.csv', tree=True, otherparam=False)
f(1, 2, 3)
f(1, 2, 3, 4, 5)

# args is a tuple with all of the positional arguments
# kwds is a dictionary with all of the keyword arguments
# You can use any parameter names as long as you have the * and ** syntax
# def f(*positional_arguments, **keyword_arguments):
# args and kwds are the traditional names. matplotlib likes kwargs for the latter.


# There are also hybrid forms, like
def g(required_parameter, optional_parameter=True, *args, **kwds):
    print "Required", required_parameter
    print "Optional", optional_parameter
    print "Remaining positional", args
    print "Remaining keyword", kwds
    print
g(1, csv_file_path='regents')
g(2, 3, 4)


# The *args, **kwds syntax doesn't give you much hint as to what the possible parameters are,
# which are required and which are optional, what their expected types
# and content, might be, etc.
# You usually have to get this information from documentation, as in matplotlib:
# http://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot


# It's considered poor form to have more than 4 or 5 required, positional parameters.
# Everything beyond that should be keywords (or everything should be keywords).
# Keywords can be "required" like so:
def h(required_keyword_parameter=None, other_required_parameter=None):
    assert required_keyword_parameter is not None, "You didn't specify that parameter and you should have"
# This way people don't have to remember the parameter order and you can add
# parameters to your function without worrying about breaking any of your callers' code.


# You can also pass in arbitrary numbers of positional and keyword parameters
def anything(*args, **kwds):
    pass
call_positional_arguments = [1, 2, 3]
call_keyword_arguments = {'arg': 7}
anything(*call_positional_arguments, **call_keyword_arguments)
anything(*[1, 2, 3], **{'arg': 7}) # Same thing

def something(x, y):
    return x + 1
something(*[1, 2]) # Also works
something(*(1, 2)) # Tuple instead of a list, same thing in this context
something(**{'x': 1, 'y': 2}) # Same thing here.


# You'd often use this to "wrap" a function, perhaps for debugging purposes:
def real_func(x, y):
    return x + y

def wrapper_func(*args, **kwds):
    print "We're calling real_func with", args, kwds
    return real_func(*args, **kwds) # So I don't have to update wrapper_func's parameters when real_func's change

wrapper_func(1, 2)
