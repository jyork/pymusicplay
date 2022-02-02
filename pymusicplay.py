#!/usr/bin/env python
import os
import tkinter as tk
from tkinter import Place, ttk, filedialog
from pygame import mixer

def play():
    mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    mixer.music.play()

def stop():
    mixer.music.stop()
        
def pause():
    mixer.music.pause()
    
def unpause():
    mixer.music.unpause()

# Create main window
music_player = tk.Tk()
mixer.init()
music_player.geometry('300x160')
music_player.title('Mini Music Player')
music_player.configure(bg='white')
s = ttk.Style(music_player)
s.theme_use('vista')

music_player.mainloop()

# Add buttons
ttk.Button(music_player, text='Play', width=10, command = play).Place(x=10, y=10)
ttk.Button(music_player, text='Stop', width=10, command = stop).Place(x=10, y=40)
ttk.Button(music_player, text='Pause', width=10, command = pause).Place(x=10, y=70)
ttk.Button(music_player, text='Unpause', width=10, command = unpause).Place(x=10, y=100)

directory = filedialog.askdirectory(title='Pick Music Directory', mustexist=True)
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song

var = tk.StringVar() 
song_title = tk.Label(music_player, font='Helvetica 12 bold', textvariable=var)

play_list = tk.Listbox(music_player, font='Helvetica 12 bold', bg='yellow', selectmode=tk.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
