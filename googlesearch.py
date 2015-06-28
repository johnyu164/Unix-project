# -*- coding: utf-8 -*- 
from google import search
from bs4 import BeautifulSoup
import urllib2

listtemp=[0]

for url in search('site:http://www.appledaily.com.tw/ 八仙樂園', tld='es', lang='es', stop=20):
    listtemp.append(url)


#print(listtemp)


try:
    page = urllib2.urlopen(listtemp[1])
except:
    print "page no found"
    
soup = BeautifulSoup(page.read()) 



for art in soup.find(id="summary"):
    for s in art('script'):
        print s

