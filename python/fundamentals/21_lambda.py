a_list = [3, 1, 2, 5]

a_list.sort()
print "List sorted in ascending order", a_list

# What if we want to sort in some other order, like descending?
# Pass a function to sort():
def cmp_x_y_long(x, y):
    if x == y:
        return 0
    elif x > y:
        return -1
    else:
        return 1
# In this context the function should return:
#   0 if x and y are equal,
#   a negative integer if x should come before y in the sorted list
#   a positive integer if x should come after y in the sorted list
a_list.sort(cmp_x_y_long)
print "List sorted in descending order", a_list
a_list.sort() # Re-sort in ascending order
print "List sorted in ascending order", a_list

# Same function, but simpler
def cmp_x_y_short(x, y):
    return y - x
a_list.sort(cmp_x_y_short)
print "List sorted in descending order", a_list
# A function is just a value, like an integer, a string, et al.


# This situation is so common that there's a shorthand for it
a_list.sort(lambda x, y: y - x) # Descending order again
print "Descending", a_list
# which is the same thing as the cmp_x_y_short version above,
# just using an anonymous function (a lambda function)
# The syntax is lambda <parameters>: <value to return>
a_list.sort(lambda x, y: x - y) # Ascending order, same as a_list.sort()
print "Ascending", a_list

# Since functions are just values, we can also name them this way
cmp_x_y_short_2 = lambda x, y: y - x
# though the def syntax is preferred if you're going to give a function a name
a_list.sort(cmp_x_y_short_2)


# For more information than you would ever want to know about sorting in Python, see
# https://wiki.python.org/moin/HowTo/Sorting