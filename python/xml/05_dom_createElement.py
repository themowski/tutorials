from xml.dom import minidom

with open('feed.xml') as f:
    document = minidom.parse(f)

print 'Before createElement:'
print document.toxml()
print

print 'After createElement'
locationElement = document.createElement('location')
document.documentElement.appendChild(locationElement)
print document.toxml()
