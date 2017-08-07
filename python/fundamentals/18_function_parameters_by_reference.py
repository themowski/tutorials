# Functions allow for code reuse (DRY, "Don't Repeat Yourself")
def change_list(a_list): # a_list is a reference, not a copy
    del a_list[0]
    a_list.append('test')
    # Don't need to return a_list, since we were modifying a reference, not a copy
    # There is an implicit "return None" here
some_list = ['a', 'b']
change_list(some_list) # some_list "becomes" a_list in change_list
some_other_list = ['b', 'c']
return_value = change_list(some_other_list) # some_other_list "becomes" a_list in change_list
assert return_value == None
