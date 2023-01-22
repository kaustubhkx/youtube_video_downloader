from pathlib import Path
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import threading
import time
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("1000x400")
root.iconphoto(True, PhotoImage(file="images/downloading.png"))

Header = Label(root, text="YouTube Video Downloader", font='Ariel')
Header.pack()

label1 = Label(root, text="Enter the YouTube Video URL")
label1.pack()

entry_url = Entry(root, width=50)
entry_url.pack()

def download():
    time.sleep(1)
    label_downloading = Label(text="Processing...")
    label_downloading.pack()
    a = str(entry_url.get())
    youtube_video = YouTube(a)
    youtube_video = youtube_video.streams.get_highest_resolution()
    file = filedialog.askdirectory()
    youtube_video.download(file)
    label_downloading.destroy()
    label_progress = Label(root,text="Video Downloaded Check Folder")
    label_progress.pack()
    label_path = Label(root,text=file)
    label_path.pack()
    title = youtube_video.title
    label_title = Label(text=title)
    label_title.pack()

def clear():
    entry_url.delete(0, END)


button = Button(text="Download",command=threading.Thread(target=download).start)
button.pack() 
button_clear = Button(text="Clear",command=clear)
button_clear.pack() 
root.mainloop()