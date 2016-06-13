
####################first version##################
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])
################this code include all links################

###########second version########################
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html,"html.parser")
# count = 0
# for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$")):
# 	if "href" in link.attrs:
# 		print(link.attrs["href"])
# 		count+=1
# print(count)
#################this chunk of code get rid of the most useless link#############

###############third version make 2nd code into a funtion and called it with a main funtion###########

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj = BeautifulSoup(html)
	return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")

while len(links)>0:
	newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)