from tkinter import *
from PIL import Image, ImageTk  # Import the necessary modules from Pillow
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+20")
root.configure(bg="#0F1A2B")
root.resizable(False, False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
#    print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)


def play_song():
    music_name = playlist.get(ACTIVE)
    #print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text="Now Playing : "+music_name[0:-4])

# Load the images and resize them
image_icon = Image.open("pngegg.png")  # Load the image
image_icon = image_icon.resize((32, 32), Image.ANTIALIAS)  # Resize to your desired dimensions
image_icon = ImageTk.PhotoImage(image_icon)  # Convert it to a PhotoImage

Top = Image.open("Cover.png")
#Top = Top.resize((300, 200), Image.ANTIALIAS)
Top = ImageTk.PhotoImage(Top)

Logo = Image.open("pngegg.png")
Logo = Logo.resize((140, 140), Image.ANTIALIAS)
Logo = ImageTk.PhotoImage(Logo)

play_button = Image.open("Play_button.png")
play_button = play_button.resize((100, 100), Image.ANTIALIAS)
play_button = ImageTk.PhotoImage(play_button)

pause_button = Image.open("Pause_button.png")
pause_button = pause_button.resize((100,100), Image.ANTIALIAS)
pause_button = ImageTk.PhotoImage(pause_button)

resume_button = Image.open("Resume_button.png")
resume_button = resume_button.resize((100,100), Image.ANTIALIAS)
resume_button = ImageTk.PhotoImage(resume_button)

stop_button = Image.open("Stop_button.png")
stop_button = stop_button.resize((100,100), Image.ANTIALIAS)
stop_button = ImageTk.PhotoImage(stop_button)

#VSK_Logo
vsk_logo = Image.open("logo.png")
vsk_logo = vsk_logo.resize((120,80), Image.ANTIALIAS)
vsk_logo = ImageTk.PhotoImage(vsk_logo)
Label(root, image=vsk_logo, background="#0F1A2B",bd=0).place(x=70, y=570)

# Use the resized images in your labels and buttons
Label(root, image=Top, background="#0F1A2B",bd=0).pack()
Label(root, image=Logo, background="#0F1A2B",bd=0).place(x=58, y=120)
Button(root, image=play_button, background="#0F1A2B", bd=0, command=play_song).place(x=78, y=300)
Button(root, image=pause_button, background="#0F1A2B",bd=0, command = mixer.music.pause).place(x=0, y=375)
Button(root, image=resume_button, background="#0F1A2B",bd=0, command= mixer.music.unpause).place(x=158, y=375)
Button(root, image=stop_button, background="#0F1A2B",bd=0, command= mixer.music.pause).place(x=78, y=450)
 
#label
music=Label(root,text="",font=("arial",10),fg="white",bg="#0f1a2b")
music.place(x=15,y=265, anchor="w")

player=Label(root,text=" MUSIC PLAYER ",font=("times new roman",40),fg="white",bg="#0f1a2b")
player.place(x=350,y=100, anchor="w")


#music
Menu = Image.open("Menu.png")
Menu = Menu.resize((600,350), Image.ANTIALIAS)
Menu = ImageTk.PhotoImage(Menu)
Button(root, image=Menu, background="#00000f",bd=0).place(x=285, y=275)

musci_fram = Frame(root,bg="#00002B", bd=2,relief=RIDGE)
musci_fram.place(x=330,y=350, width= 510, height=250)

Button(root,text="Open Folder", width=15, height=2, font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=330, y=300)

scroll = Scrollbar(musci_fram)
playlist = Listbox(musci_fram, width=100,font=("arail",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command = playlist.yview)
scroll.pack(side = RIGHT, fill = Y)
playlist.pack(side = LEFT, fill = BOTH)

root.mainloop()
