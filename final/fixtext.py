# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

def adjustfile(which_file):
	text_file = open(which_file,"r")
	text = text_file.read().decode('utf-8')

	text_file.close()    
	#print text

	soup = BeautifulSoup(text)
	result_text = soup.getText()

	write_file = open(which_file,"w")

	write_file.write(result_text.encode('utf-8'))
	
	print result_text
		
	print('/////////////////////////////////////分隔線////////////////////////////////////////')

	write_file.close()



