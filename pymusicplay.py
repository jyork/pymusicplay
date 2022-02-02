#!/usr/bin/env python
import os
import tkinter as tk
from tkinter import DISABLED, Misc, Place, ttk, filedialog
from turtle import title
from pygame import mixer

class MusicPlayer():
    def __init__(self, master: Misc):
        self.window = master
        mixer.init()
        self.window.geometry('400x160')
        self.window.title('Mini Music Player')
        self.window.configure(bg='white')
        s = ttk.Style(self.window)
        s.theme_use('vista')
        self._varNowPlaying = tk.StringVar()
        self._varPlayingNext = tk.StringVar()
        self.create_widgets()
        self.set_now_playing('Puple Rain', 'Prince')
        self.set_playing_next('Istanbul', 'We Could Be Giants')

    def create_widgets(self):
        tk.Label(self.window, text='Now playing', font=('arial', 12, 'normal')).place(x=10, y=10)
        tk.Label(self.window, text='Next up', font=('arial', 12, 'normal')).place(x=10, y=60)
        tk.Label(self.window, text='Music directory', font=('arial', 12, 'normal')).place(x=10, y=90)
        self.txtNowPlaying = tk.Message(self.window, border='1', font=('arial', 12, 'normal'), textvariable=self._varNowPlaying, width=160, justify=tk.CENTER)
        #tk.Entry(self.window, background='#F0F8FF', font=('arial', 12, 'normal'))
        self.txtNowPlaying.place(x=130, y=10)
        self.txtPlayingNext = tk.Message(self.window,  border='1', font=('arial', 12, 'normal'), textvariable=self._varPlayingNext, width=160, justify=tk.CENTER)
        self.txtPlayingNext.place(x=130, y=60)
        self.dir = tk.Label(self.window, text='C:\\Users\\Obliv\\Music', font=('arial', 12, 'normal')).place(x=130, y=100)
        
    def change_music_dir(self, dir: str):
        self.dir.config(text=dir)
        # Load music from dir

    def set_now_playing(self, song: str, author: str):
        self._varNowPlaying.set(f'{song}\n{author}')

    def set_playing_next(self, song: str, author: str):
        self._varPlayingNext.set(f'{song} by {author}')

    def play(self):
        #mixer.music.load(play_list.get(tk.ACTIVE))
        #var.set(play_list.get(tk.ACTIVE))
        #mixer.music.play()
        pass

    def stop():
        mixer.music.stop()
            
    def pause():
        mixer.music.pause()
        
    def unpause():
        mixer.music.unpause()

# Create main window
music_player_frame = tk.Tk()
player = MusicPlayer(music_player_frame)
# mixer.init()
# music_player.geometry('300x160')
# music_player.title('PyMusicPlay')
# music_player.configure(bg='white')
# s = ttk.Style(music_player)
# s.theme_use('vista')

music_player_frame.mainloop()

# Add buttons
# ttk.Button(music_player, text='Play', width=10, command = play).Place(x=10, y=10)
# ttk.Button(music_player, text='Stop', width=10, command = stop).Place(x=10, y=40)
# ttk.Button(music_player, text='Pause', width=10, command = pause).Place(x=10, y=70)
# ttk.Button(music_player, text='Unpause', width=10, command = unpause).Place(x=10, y=100)

# directory = filedialog.askdirectory(title='Pick Music Directory', mustexist=True)
# os.chdir(directory) #it permits to chenge the current dir
# song_list = os.listdir() #it returns the list of files song

# var = tk.StringVar() 
# song_title = tk.Label(music_player, font='Helvetica 12 bold', textvariable=var)

# play_list = tk.Listbox(music_player, font='Helvetica 12 bold', bg='yellow', selectmode=tk.SINGLE)
# for item in song_list:
#     pos = 0
#     play_list.insert(pos, item)
#     pos += 1


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
# def getCheckboxValue():
# 	checkedOrNot = cbRecurse.get()
# 	return checkedOrNot


# # this is the function called when the button is clicked
# def btnClickFunction():
# 	print('clicked')


# # this is the function called when the button is clicked
# def btnStopFunction():
# 	print('clicked')


# # this is the function called when the button is clicked
# def btnPauseFunction():
# 	print('clicked')


# # this is a function which returns the selected spin box value
# def getSelectedSpinBoxValue():
# 	return spinVolume.get()

# # This is the section of code which creates the a label


# # This is the section of code which creates a checkbox
# recurse=Checkbutton(root, text='Recurse music directory', variable=cbRecurse, bg='#F0F8FF', font=('arial', 12, 'normal'))
# recurse.place(x=-695, y=-340)


# # This is the section of code which creates a button
# Button(root, text='Play', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=-695, y=-280)


# # This is the section of code which creates a button
# Button(root, text='Stop', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnStopFunction).place(x=-575, y=-270)


# # This is the section of code which creates a button
# Button(root, text='Pause', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnPauseFunction).place(x=-635, y=-280)


# # This is the section of code which creates a spin box
# spinVolume= Spinbox(root, from_=1, to=100, font=('arial', 12, 'normal'), bg = '#F0F8FF', width=10)
# spinVolume.place(x=-615, y=-210)


# # This is the section of code which creates the a label
# Label(root, text='Volume', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=-685, y=-210)


# root.mainloop()
