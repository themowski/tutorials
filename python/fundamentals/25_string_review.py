print 'Single-quoted string'
print

print "Double-quoted string" # No semantic difference to the above
print

print '''
Multi-line
string
with triple single-quotes
'''
print

x = """
Multi-line
string
with triple double-quotes
"""
print 'Lines in x', len(x.splitlines())
print

x = '''
Multi-line string,
don't include first line
triple single-quotes
'''
print 'Lines in x', len(x.splitlines())
print

print "String escaping\nThis is on a new line\nHere's a tab\tand so on"
print "This is a Windows line\r\n"
print 'This is a Unix line\n'
print 'This is a Mac OS 9 line\r'
print

# Raw string
print r'\n'
print

# Unicode string
print u'''ASCII is also Unicode'''
print


