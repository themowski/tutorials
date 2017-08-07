import xml.dom
from xml.dom import minidom

with open('feed.xml') as f:
    document = minidom.parse(f)

for childNode in document.documentElement.childNodes:
    if childNode.nodeType != xml.dom.Node.ELEMENT_NODE:
        continue
    if childNode.tagName != 'title':
        continue
    for grandChildNode in childNode.childNodes:
        if grandChildNode.nodeType != xml.dom.Node.TEXT_NODE:
            continue
        print grandChildNode.parentNode.tagName, ':', grandChildNode.data
        break

