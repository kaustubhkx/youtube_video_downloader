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
    global label_progress, label_path, label_title
    time.sleep(1)
    label_downloading = Label(text="Processing...")
    label_downloading.pack()
    a = str(entry_url.get())
    youtube_video = YouTube(a)
    youtube_video = youtube_video.streams.get_highest_resolution()
    file = filedialog.askdirectory()
    file_path = file
    youtube_video.download(file_path)
    label_downloading.destroy()
    label_progress = Label(root,text="Video Downloaded Check Folder")
    label_progress.pack()
    label_path = Label(root,text=file_path)
    label_path.pack()
    title = youtube_video.title
    display_title = "Title :- " + title
    label_title = Label(text=display_title)
    label_title.pack()

def audio_download():
    global label_title_audio, label_path_audio, label_progress_audio
    time.sleep(1)
    label_downloading = Label(text="Processing...")
    label_downloading.pack()
    a = str(entry_url.get())
    youtube_video = YouTube(a)
    youtube_video = youtube_video.streams.filter(only_audio=True).first()
    file = filedialog.askdirectory()
    file_path = file
    youtube_video.download(file_path)
    label_downloading.destroy()
    label_progress_audio = Label(root,text="Audio Downloaded Check Folder")
    label_progress_audio.pack()
    label_path_audio = Label(root,text=file_path)
    label_path_audio.pack()
    title = youtube_video.title
    display_title = "Title :- " + title
    label_title_audio = Label(text=display_title)
    label_title_audio.pack()



def clear():
    entry_url.delete(0, END)
    label_progress.pack_forget()
    label_title.pack_forget()
    label_path.pack_forget()
    label_title_audio.pack_forget()
    label_path_audio.pack_forget()
    label_progress_audio.pack_forget()

button = Button(text="Download",command=threading.Thread(target=download).start)
button.pack() 
audio_download_button = Button(text="Download Audio Only",command=threading.Thread(target=audio_download).start)
audio_download_button.pack() 
button_clear = Button(text="Clear",command=clear)
button_clear.pack() 
root.mainloop()