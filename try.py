from bs4 import BeautifulSoup
import urllib2


url="http://udn.com/news/breaknews/1"
try:
    page = urllib2.urlopen(url)
except:
    print "page no found"
    
soup = BeautifulSoup(page.read()) 
 
for word in soup.find_all('a'):
    print(word.getText())
    print(word.get('href'))
