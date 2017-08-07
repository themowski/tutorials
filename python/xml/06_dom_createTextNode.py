from xml.dom import minidom

with open('feed.xml') as f:
    document = minidom.parse(f)

locationElement = document.createElement('location')
locationElement.appendChild(document.createTextNode('ISU'))
document.documentElement.appendChild(locationElement)
print document.toxml()
