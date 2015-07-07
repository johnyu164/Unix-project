# -*- coding: utf-8 -*-
 
import sys		
import time		
import pygst		
pygst.require("0.10")
import gst		
import re

def reader():
	text_file = open("222.txt","r")
	text = text_file.read().decode('utf-8')

	text_file.close() 


	wordlist = text.split('，'.decode('utf-8'))
	print wordlist
	for input_string in wordlist:
		music_stream_uri = 'http://translate.google.com/translate_tts?ie=utf-8&tl=zh&q=' + input_string
		player = gst.element_factory_make("playbin", "player")
		player.set_property('uri', music_stream_uri)
		player.set_state(gst.STATE_PLAYING)
	
		time.sleep(5)

	return 0


