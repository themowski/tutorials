from xml.dom import minidom

with open('feed.xml') as f:
    document = minidom.parse(f)

with open('feed.xml') as f:
    f_str = f.read()
    document = minidom.parseString(f_str)

print 'Entire document:'
print document.toxml()
