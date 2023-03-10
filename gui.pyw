from pytube import YouTube
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import threading
import time
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("1000x400")
#root.iconphoto(True, PhotoImage(file="images/downloading.png"))

Header = Label(root, text="YouTube Video Downloader", font='Ariel')
Header.pack()

label1 = Label(root, text="Enter the YouTube Video URL")
label1.pack()

entry_url = Entry(root, width=50)
entry_url.pack()

def download():
    global label_progress, label_path, label_title
    time.sleep(1)
    if not entry_url.get():
        messagebox.showerror("Empty field", "This field cannot be left blank")
    else:
        try:
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
        except:
            messagebox.showerror("Invalid URL", "Enter a valid YouTube Video URL")
            label_downloading.destroy()


def audio_download():
    global label_title_audio, label_path_audio, label_progress_audio
    time.sleep(1)
    if not entry_url.get():
        messagebox.showerror("Empty field", "This field cannot be left blank")
    else:
        try:
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
        except:
            messagebox.showerror("Invalid URL", "Enter a valid YouTube Video URL")
            label_downloading.destroy()
        

def clear():
    entry_url.delete(0, END)
    try:
        label_progress.pack_forget()
        label_title.pack_forget()
        label_path.pack_forget()
    except:
        pass
    try:
        label_title_audio.pack_forget()
        label_path_audio.pack_forget()
        label_progress_audio.pack_forget()
    except:
        pass

def start_download():
    download_thread = threading.Thread(target=download)
    download_thread.start()

button = Button(text="Download",command=start_download)
button.pack() 

def start_audio_download():
    audio_download_thread = threading.Thread(target=audio_download)
    audio_download_thread.start()

audio_download_button = Button(text="Download Audio Only",command=start_audio_download)
audio_download_button.pack() 

button_clear = Button(text="Clear",command=clear)
button_clear.pack() 
root.mainloop()
