import os

def run():
	
	s=None
	song_list = []
	
	try:
		f = open('music_path.txt','r')
		s = str(f.read())
		f.close()
	except:
		pass
			
	if s==None:
		
		s = "/home/"
		#l = os.walk(s)
		#subdir = [x[0] for x in l]
		subdir = [];
		subdir.append(s)
	
		#print subdir
	
		count = 0
	
		for d in subdir:
			print "Searching",d
			l = os.walk(s)
			subdir2 = [x[0] for x in l]
			for x in subdir2:
				print "Searching",x
				names = x.split('/')
				#print names[-1]
				if names[-1]=='Music':
					s=x
					count = 1
					break
			if count == 1:
				break			
	
		#print s
	
		f = open('music_path.txt','w')
		f.write(s)
		f.close()
	
	l = os.walk(s)
	subdir = [x[0] for x in l]
	
	song_full_path = []
	
	new_list = os.listdir(s)
	for item in new_list:
		path = os.path.join(s,item)
		song_full_path.append(path)#os.path.abspath(path))
		
	
	#print song_list
	#print subdir
	for d in subdir:
		print "Searching",d
		new_list = os.listdir(d)
		for item in new_list:
			path = os.path.join(d,item)
			song_full_path.append(path)#os.path.abspath(path))
		song_list = song_list + new_list
		
		l = os.walk(s)
		new_subdir = [x[0] for x in l]
	
		subdir = subdir + new_subdir
	
	result = []
	result_path = []
	#print song_full_path
	for song in song_full_path:
		name = song.split("/")
		if ((name[-1].endswith('.wav'))| (song.endswith('.mp3'))):
			result.append(name[-1])
			result_path.append(song)
		 
	
	#print len(result)
	#return result_path	
	
	songs = [x.lower() for x in result]
	
	sd = {}
	count = 0

	for item in songs:
	
		sd[item] = result_path[count]
		count+=1

	return(sd)	
	
#run()
	
