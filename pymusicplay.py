#!/usr/bin/env python
import os
import tkinter as tk
from tkinter import Place, ttk, filedialog
from pygame import mixer

# Create main window
root = tk.Tk()
mixer.init()
root.geometry('300x160')
root.title('Mini Music Player')
root.configure(bg='white')
s = ttk.Style(root)
s.theme_use('vista')

root.mainloop()

# Add buttons
ttk.Button(root, text='Play', width=10. command=play_song()).Place(x=10, y=10)
ttk.Button(root, text='Play', width=10. command=play_song()).Place(x=10, y=10)
ttk.Button(root, text='Play', width=10. command=play_song()).Place(x=10, y=10)
ttk.Button(root, text='Play', width=10. command=play_song()).Place(x=10, y=10)
