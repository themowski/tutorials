import xml.sax
import xml.sax.handler

class MyContentHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.__link_hrefs = []
        self.__level = 0

    @property
    def link_hrefs(self):
        return self.__link_hrefs

    def startDocument(self):
        print 'startDocument'

    def endDocument(self):
        print 'endDocument'

    def startElement(self, name, attrs):
        print ' ' * self.__level + 'startElement', name
        self.__level += 1
        if name != 'link':
            return
        self.__link_hrefs.append(attrs['href'])

    def endElement(self, name):
        self.__level -= 1
        print ' ' * self.__level + 'endElement', name

    def characters(self, content):
        print ' ' * self.__level + 'characters ', "'" + content + "'"


with open('feed.xml') as f:
    handler = MyContentHandler()
    xml.sax.parse(f, handler)
    print
    for link_href in handler.link_hrefs:
        print 'Link href', link_href
