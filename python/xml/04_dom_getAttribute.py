import xml.dom
from xml.dom import minidom

with open('feed.xml') as f:
    document = minidom.parse(f)

for linkElement in document.documentElement.getElementsByTagName('link'):
    href = linkElement.getAttribute('href')
    print 'Link href', href
    nonextant = linkElement.getAttribute('nonextant')
    assert len(nonextant) == 0
