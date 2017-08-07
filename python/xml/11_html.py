# http://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup

with open('example.html') as f:
    soup = BeautifulSoup(f)

print 'Page title', soup.title.string
print 'Number of scripts', len(soup.head.find_all('script'))
print

print 'Metas'
for meta in soup.head.find_all('meta'):
    name = meta.get('name')
    content = meta.get('content')
    if name is None or content is None:
        continue
    print name, '=', content
print

print 'Links'
for link in soup.find_all('a'):
    href = link.get('href')
    if href is None:
        continue
    print href
print

# print 'Text of the page'
# print soup.get_text()
# Could do some natural language processing
