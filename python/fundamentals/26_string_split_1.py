# Split a string into a list of strings

# Split on commas
# Note that the separator is NOT included in the resulting strings.
header = "Year,,University Name,Student Classification,Resident Status,Headcount"
print header.split(',')

# Split on commas, maximum 2 splits i.e. the sequence will contain at most 3 elements
print "Year,University Name,Student Classification,Resident Status,Headcount".split(',', 2)
print "Year,University Name".split(',', 2) # Only one split possible

# Split on whitespace, separator = any amount of whitespace (\d+)
print "Hello, world".split()
print "Hello,  world".split()
print "Hello,  world".split(' ')

# Split on multiple characters. Entire separator must match.
print "Hello, world".split(', ')

# Can also split from the end using .rsplit()
print 'name_subname1_subname2'.rsplit('_', 1)[-1]
print "Year,University Name,Student Classification,Resident Status,Headcount".rsplit(',', 2)

# Related method: .partition()
# Does a single split and includes the separator, so the result is always a sequence with len <= 3
print "Year,University Name,Student Classification,Resident Status,Headcount".partition(',')