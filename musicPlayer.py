import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicPlayer = tkr.Tk()
musicPlayer.title("Simple Music Player")
musicPlayer.geometry("450x350")

#Mencari Direktori Musik
directory = askdirectory()
os.chdir(directory)
songList = os.listdir()

#Membuat Playlist
playlist = tkr.Listbox(musicPlayer, font = "Cambria 14 bold", bg = "cyan2", selectmode = "tkr.SINGLE")

#Menambah Lagu ke Playlist
for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#Inisialisasi Modul
pygame.init()
pygame.mixer.init()

#Fitur dalam MusicPlayer
def playMusic():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def exitMusicPlayer():
    pygame.mixer.music.stop()

def pauseMusic():
    pygame.mixer.music.pause()

def resumeMusic():
    pygame.mixer.music.unpause()

playButton = tkr.Button(
    musicPlayer,
    height = 3, width = 5, text = "Play Music", font = "Cambria 14 bold",
    command = playMusic, bg = "lime green", fg = "black")
stopButton = tkr.Button(
    musicPlayer,
    height = 3, width = 5, text = "Stop Music", font = "Cambria 14 bold",
    command = exitMusicPlayer, bg = "red", fg = "black")
pauseButton = tkr.Button(
    musicPlayer, height = 3, width = 5, text = "Pause Music", font = "Cambria 14 bold",
    command = pauseMusic, bg = "yellow", fg = "black")
resumeButton = tkr.Button(
    musicPlayer, height = 3, width = 5, text = "Resume Music", font = "Cambria 14 bold",
    command = resumeMusic, bg = "yellow", fg = "black")

playButton.pack(fill = "x")
stopButton.pack(fill = "x")
pauseButton.pack(fill = "x")
resumeButton.pack(fill = "x")

playlist.pack(fill = "both", expand = "yes")
var = tkr.StringVar()
songTitle = tkr.Label(musicPlayer, font = "Cambria 12 bold", textvariable = var)
songTitle.pack()
musicPlayer.mainloop()