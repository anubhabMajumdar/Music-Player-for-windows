#!/usr/bin/env python

# CREATED BY ANUBHAB MAJUMDAR

from tkinter import *
import tkMessageBox
import os
import sys
import pygame
import song_list_2
import random

# Global Variables

songs_list = []
song_full_path = []
sounds = pygame.mixer
sounds.init()
pause = 0
RED = (255,0,0)
first_time = 0

class music_player(Frame):
	
	def __init__(self, app):
		
		global songs_list, song_full_path, text, first_time
		
		Frame.__init__(self, app)
		
		self.app = app
		
		#(songs_list, song_full_path) = song_list.run()
		self.songs = song_list_2.run()
		
		self.button_frame = Frame()
		
		self.refresh_button = Button(self.button_frame, text='Refresh',command=self.refresh)
		self.refresh_button.pack(side='left')
		
		self.previous_button = Button(self.button_frame, text='Previous',command=self.previous)
		self.previous_button.pack(side='left')
		
		self.play_button = Button(self.button_frame, text='Play',command=self.play)
		self.play_button.pack(side='left')
		
		self.stop_button = Button(self.button_frame, text='Stop',command=self.stop)
		self.stop_button.pack(side='left')
		
		self.button_text = 'Pause/Unpause'
		self.pause_button = Button(self.button_frame, text=self.button_text,command=self.pause)
		self.pause_button.pack(side='left')
		
		self.random_button = Button(self.button_frame, text='Random Play',command=self.random)
		self.random_button.pack(side='left')
		
		self.next_button = Button(self.button_frame, text='Next',command=self.next)
		self.next_button.pack(side='left')
		
		self.search_label = Label(self.button_frame,text="	Search Songs-->")
		self.search_label.pack(side='left')
		
		self.search = Entry(self.button_frame)
		self.search.pack(side='left')
		
		self.search_button = Button(self.button_frame, padx=30, text='Search',command=self.search_song)
		self.search_button.pack(side='left')
		
		self.button_frame.pack(side='top')
		
		self.label_frame = Frame()
		
		self.volume = DoubleVar()
		self.volume_scale = Scale(self.label_frame, variable=self.volume,from_=0.0,to=1.0,resolution=0.1,command=self.change_volume,label='Volume',orient=HORIZONTAL)
		sounds.music.set_volume(0.5)
		self.volume_scale.pack(side='top')
		
		self.label = Label(self.label_frame, textvariable=text)
		self.label.pack(side='top')
		
		self.status=StringVar()
		self.status.set('Music Player Status-->Stop')
		
		self.label2 = Label(self.label_frame, textvariable=self.status)
		self.label2.pack(side='top')
		
		self.label_frame.pack(side='top')
		
		self.f = Frame(app)
		self.f.pack()

		sY = Scrollbar(self.f,orient = 'vertical')
		sY.pack(side='right', fill=Y)

		self.lb = Listbox(self.f,width=1000,height=len(songs_list),yscrollcommand=sY.set)
		self.lb.pack(side=TOP,fill=BOTH,expand=TRUE)
		
		self.list_number = int((self.lb.bind('<<ListboxSelect>>', self.listbox_return))[0])
		
		if first_time == 0:
			first_time = 1
			self.update_list()
		
	
	def update_list(self):
		count = 0
		for fname in self.songs.keys():
			self.lb.insert(count,fname)
			count+=1
	
	def refresh(self):
		
		self.lb.delete(0,len(self.songs))
		self.status.set('Music Player Status-->Refreshing')
		
		self.songs = song_list_2.run()
		
		self.update_list()
		self.status.set('Music Player Status-->Song List Updated')
				
	def search_song(self):
		
		self.lb.delete(0,len(self.songs))
		s = self.search.get()
		
		count = 0
		for item in self.songs.keys():
			
			if item.find(s)>=0:
				self.lb.insert(count,item)
	 	
	
	def play(self):
		
		global  sounds, pause
		
		pause=0
		
		self.current_track_number = self.list_number
		self.list_name = str(self.lb.get(self.current_track_number))
		
		self.lb.activate(self.current_track_number)
		self.lb.see(self.current_track_number)
		
		text.set(self.list_name)
		
		sounds.music.load(self.songs[self.list_name])
		self.status.set('Music Player Status-->Playing')
		sounds.music.play()
		
	def stop(self):
		
		global sounds,pause
		
		self.status.set('Music Player Status-->Stop')
		pause=-1
		sounds.music.stop()
	
	def pause(self):
		
		global sounds, pause
		
		if pause==0:
			pause=1
			self.status.set('Music Player Status-->Paused')
		
			sounds.music.pause()
		elif pause==1:
			pause=0
			self.status.set('Music Player Status-->Playing')
		
			sounds.music.unpause()
	
	def previous(self):
		
		global sounds
		
		self.current_track_number-=1
		self.list_name = str(self.lb.get(self.current_track_number))
		
		self.lb.activate(self.current_track_number)
		self.lb.see(self.current_track_number)
		
		text.set(self.list_name)
		
		sounds.music.load(self.songs[self.list_name])
		self.status.set('Music Player Status-->Playing')
		sounds.music.play()
		
	
	def next(self):
		
		global sounds
		
		self.current_track_number+=1
		self.list_name = str(self.lb.get(self.current_track_number))
		
		self.lb.activate(self.current_track_number)
		self.lb.see(self.current_track_number)
		
		text.set(self.list_name)
		
		sounds.music.load(self.songs[self.list_name])
		self.status.set('Music Player Status-->Playing')
		sounds.music.play()
				
	def random(self):
		
		global sounds
		
		self.current_track_number = random.randrange(0,self.lb.size())
		self.list_name = str(self.lb.get(self.current_track_number))
		
		self.lb.activate(self.current_track_number)
		self.lb.see(self.current_track_number)
		
		text.set(self.list_name)
		
		sounds.music.load(self.songs[self.list_name])
		self.status.set('Music Player Status-->Playing')
		sounds.music.play()
			
	def listbox_return(self,e):
		
		self.list_number = int((self.lb.curselection())[0])
		#self.list_name = str(self.lb.get(self.list_number))
		
	def change_volume(self,v):
		global sounds
		
		sounds.music.set_volume(self.volume.get())	
			
def shutdown():
	if tkMessageBox.askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
		app.destroy()


app = Tk()
app.title("Music Player")
#app.geometry('600x600+500+200')
#app.minsize(600,600)
#app.maxsize(600,600)

text = StringVar()
text.set("Choose song and hit play")

panel = music_player(app)
#panel.update_list()
panel.pack()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()


