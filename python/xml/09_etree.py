from xml.etree import ElementTree

with open('feed.xml') as f:
    etree = ElementTree.parse(f)

root = etree.getroot()

print 'Document element tag', root
print

print 'All child elements'
for child in root:
    print child.tag, child.attrib
    if child.tag.endswith('title'):
        print 'Title', child.text
print
