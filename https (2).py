import httplib
import BeautifulSoup

c = httplib.HTTPSConnection("https://www.google.com.tw/search?q=123")
c.request("GET", "/")
response = c.getresponse()

print response.status, response.reason

data = response.read()

soup = BeautifulSoup(c) 
 
print soup