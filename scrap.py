from bs4 import BeautifulSoup
import urllib2


url="http://www.google.com.tw/search?q=123"
try:
    page = urllib2.urlopen(url)
except:
    print "page no found"
    
soup = BeautifulSoup(page.read()) 
 
print soup.find_all('a')

