import urllib2
from bs4 import BeautifulSoup

cin =str(raw_input("keyword:"))

target = cin.replace(" ","+") 

url="https://www.google.com.tw/search?q="+target

try:
    page = urllib2.urlopen(url)
except:
    print "page no found"
    
soup = BeautifulSoup(page.read()) 
 
print soup.find_all('a')
