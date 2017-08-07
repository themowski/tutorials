# Join a sequence of strings into a single string
# Inverse operation of .split()
# Syntax: <separator string>.join(sequence of strings)

print ','.join(['Year', 'University Name'])

print ''.join(['Hello, ', 'world'])
joined_str = ''
for substr in ['Hello, ', 'world']:
    joined_str += substr

print ', '.join(('Hello', 'world')) # Tuple instead of a list

# Won't work, because range(10) produces a list of numbers, not strings
print range(10)
# print ','.join(range(10))
str_list = []
for i in xrange(10):
    str_list.append(str(i))
print ','.join(str_list)
for str_i in (str(i) for i in xrange(10)):
    print str_i
print ','.join(str(i) for i in xrange(10)) # List comprehension

# Capitalize every word in a sentence
sentence = 'this is an uncapitalized sentence'
print ' '.join(word.capitalize()
               for word in sentence.split())
# Equivalent, more verbose:
capitalized_sentence = []
for word in sentence.split():
    capitalized_sentence.append(word.capitalize())
print ' '.join(capitalized_sentence)

# Capitalize every other letter
word = 'longword'
# i % 2 == 0 ? c.upper() : c
print ''.join(c.upper() if i % 2 == 0 else c
               for i, c in enumerate(word))
# Equivalent, more verbose:
out_word = []
for i, c in enumerate(word):
    if i % 2 == 0:
        out_word.append(c.upper())
    else:
        out_word.append(c)
print ''.join(out_word)