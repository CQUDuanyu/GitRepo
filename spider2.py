from urllib.request import urlopen
from bs4 import *
import re


pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://enwikipedia.org"+pageUrl)
    bsobj = BeautifulSoup(html)
    for link in bsobj.findAll("a",href = re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                #we have encountered a new page
                newPage = link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")
