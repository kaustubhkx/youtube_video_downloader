from pathlib import Path
from pytube import YouTube
from tkinter import *
from tkinter import filedialog

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

def save_file(file):
    file = filedialog.askdirectory()

def download(file):
    a = str(entry_url.get())
    youtube_video = YouTube(a)
    youtube_video = youtube_video.streams.get_highest_resolution()
    # downloads_path = str(Path.home() / "Downloads")
    downloads_path = save_file(file)
    path = str(downloads_path)
    youtube_video.download(downloads_path)
    label_progress = Label(root,text="Video Downloaded \n Check Your Download Folder")
    label_progress.pack()
    title = youtube_video.title
    label_title = Label(text=title)
    label_title.pack()

def clear():
    entry_url.delete(0, END)


button = Button(text="Download",command=download)
button.pack() 
button_clear = Button(text="Clear",command=clear)
button_clear.pack() 
button_file = Button(text="Save",command=save_file)
button_file.pack() 
root.mainloop()