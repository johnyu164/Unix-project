# -*- coding: utf-8 -*- 
from google import search
from bs4 import BeautifulSoup
import urllib2


def gettitle(origin_site):
	
	try:
		origin_page = urllib2.urlopen(origin_site)
	except:
		print "page no found"
		return 0

	soup = BeautifulSoup(origin_page.read())
	
	titlehere = soup.title.get_text()
	
	titlehere = titlehere.split()
	
	print titlehere[0].encode('utf-8')
	
	return titlehere[0].encode('utf-8')


def googlesearch(key, choose):

	listtemp =[0] #存googlen搜尋結果

	sites = [0,'www.appledaily.com.tw','www.ltn.com.tw','www.chinatimes.com','udn.com','news.rti.org.tw','news.cnyes.com']

	#choose = int(raw_input('Choose news site:(輸入1蘋果新聞,輸入2自由時報新聞,輸入3中時電子報,輸入4聯合新聞網,5中央廣播電台,6巨亨網)'))
		
											
	for url in search('site:' + sites[int(choose)] + ' ' + key, tld='es', lang='es', stop=5):

		listtemp.append(url)
	try:
		getsitetotxt(listtemp[1], '222.txt')
		return listtemp[1]
	except:
		getsitetotxt(' ', '222.txt')
		return 'page no found!'

	


#print(listtemp)
def getsitetotxt(site,targetfile):

	try:
		page = urllib2.urlopen(site)

		soup = BeautifulSoup(page.read())
		listp = soup.findAll('p')
	
		text_file = open(targetfile, "w")


		for art in listp:
			#print(art.encode('utf-8'))
			text_file.write(art.encode('utf-8'))


		text_file.close()
				
	except:
		
		print "news no found"
		

	


#main	
#origin_site = raw_input('Input site:')

#gettitle(origin_site)

#getsitetotxt(origin_site, '111.txt')





