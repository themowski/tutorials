from xml.dom import minidom

impl = minidom.getDOMImplementation()

document = impl.createDocument(None, "root", None)
root_element = document.documentElement
text = document.createTextNode('Some textual content.')
root_element.appendChild(text)
print document.toxml()
