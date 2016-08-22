#!/usr/bin/env python

import song_list

(song_list,song_path_list) = song_list.run()

songs = [x.lower() for x in song_list]

sd = {}
count = 0

for item in songs:
	
	sd[item] = song_path_list[count]
	count+=1

inp = ''

while inp!='x':
	
	inp = raw_input("search string-->")
	
	for item in sd.keys():
		
		if item.find(inp)>=0:
			print sd[item]
	
			
	 	
	

