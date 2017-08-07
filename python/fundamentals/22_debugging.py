def f(a_list):
    print "Length of list", len(a_list)
    for element_i in xrange(0, len(a_list)+1):
        #print element_i
        element = a_list[element_i]
        print element_i, element

a_list = 'ya see i go by the code of the doctor of the mix'.split()
f(a_list)