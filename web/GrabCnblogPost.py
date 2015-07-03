import urllib2
from bs4 import BeautifulSoup


class GrabCnblogPost:
    pass


def get_url():
    url_list = []
    next_page = ''
    resporn = urllib2.urlopen('http://www.cnblogs.com/catch', timeout=1500)

    soup = BeautifulSoup(resporn.read())

    for a in soup.find_all('a', attrs={'class' : 'postTitle2'}):
        url_list.append(a.get('href'))

    next = soup.find(id = 'nav_next_page')
    if next:
       next = next.find('a').get('href')

    return url_list, next

def open_url(url_list):
    for u in url_list:
        op = urllib2.urlopen(u)
        soup = BeautifulSoup(op.read())
        print soup.title.text


l, n = get_url()
print l
print n
open_url(l)
