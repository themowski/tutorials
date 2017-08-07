import xml.dom
from xml.dom import minidom

with open('feed.xml') as f:
    document = minidom.parse(f)

print 'Print contents of all title elements'
for childElement in document.documentElement.getElementsByTagName('title'):
    for grandChildNode in childElement.childNodes:
        if grandChildNode.nodeType != xml.dom.Node.TEXT_NODE:
            continue
        print 'Title:', grandChildNode.data
        break
print


print 'Print contents of all entry/title elements'
for entryElement in document.documentElement.getElementsByTagName('entry'):
    for titleElement in entryElement.getElementsByTagName('title'):
        for node in titleElement.childNodes:
            if node.nodeType != xml.dom.Node.TEXT_NODE:
                continue
            print 'Title', node.data
            break
