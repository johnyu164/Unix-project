# -*- coding: utf-8 -*- 
import fixtext
import googlesearch
# -*- coding: utf-8 -*- 
import simularity
import readtext
from operator import itemgetter

#_import_(googlesearch)
#_import_(fixtext)
#_import_(simularity)

title = [0]
list2 = [0]
site = [0]


origin_site = raw_input('Input site:')
title[0] = googlesearch.gettitle(origin_site)
googlesearch.getsitetotxt(origin_site, '111.txt')


tempsite = googlesearch.googlesearch(title[0], 1)
site.append(tempsite)

title.append(googlesearch.gettitle(site[1]))
print 'site:' + tempsite
print 'simularity: '
temp = simularity.runsim()
list2.append(temp)


j = 2 
while j < 7:

        tempsite = googlesearch.googlesearch(title[0], j)
        site.append(tempsite)

        title.append(googlesearch.gettitle(site[j]))
        print 'site:' + tempsite
        print 'simularity: '
        temp = simularity.runsim()
        list2.append(temp)
        j=j+1

read=raw_input('Which one do you want to lesson?')

if(int(read)>7 or int(read)==0):
	print 'No such news'
else:
	get = googlesearch.googlesearch(title[0],read)
	fixtext.adjustfile('222.txt')
	readtext.reader()


'''
tempsite = googlesearch.googlesearch(title[0], 3)
site.append(tempsite)

title.append(googlesearch.gettitle(site[3]))
print 'site:' + tempsite
print 'simularity: '
temp = simularity.runsim()
list2.append(temp)



tempsite = googlesearch.googlesearch(title[0], 4)
site.append(tempsite)

title.append(googlesearch.gettitle(site[4]))
print 'site:' + tempsite
print 'simularity: '
temp = simularity.runsim()
list2.append(temp)



tempsite = googlesearch.googlesearch(title[0], 5)
site.append(tempsite)

title.append(googlesearch.gettitle(site[5]))
print 'site:' + tempsite
print 'simularity: '
temp = simularity.runsim()
list2.append(temp)


tempsite = googlesearch.googlesearch(title[0], 6)
site.append(tempsite)

title.append(googlesearch.gettitle(site[6]))
print 'site:' + tempsite
print 'simularity: '
temp = simularity.runsim()
list2.append(temp)

total=[[0,0,0]]

i = 1
while i < 7:
	total.append([site[i],title[i],list2[i]])
	i=i+1



sorted(total, key=itemgetter(2))
'''

#print total

#print list2
#print title
#print site
#fixtext.adjustfile('111.txt')
#fixtext.adjustfile('222.txt')

