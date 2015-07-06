# -*- coding: utf-8 -*- 
from google import search
from bs4 import BeautifulSoup
import urllib2

listtemp=[0]

sites='http://www.appledaily.com.tw/'

key='八仙樂園'


for url in search('site:' + sites + ' ' + key, tld='es', lang='es', stop=5):
    listtemp.append(url)


#print(listtemp)

try:
    page = urllib2.urlopen(listtemp[2])
except:
    print "page no found"
    
soup = BeautifulSoup(page.read()) 

text_file = open("222.txt", "w")

listp = soup.findAll('p')

for art in listp:
    print(art.encode('utf-8'))
    text_file.write(art.encode('utf-8'))

text_file.close()
