from pytube import YouTube


#Asks for the url using user input
get_url_user_input = str((input("Enter the URL:- ")))

#Asks for the download location using user input
download_location = str(input("Enter the location where you want to download the videos:- "))

youtube_video = YouTube(get_url_user_input)

youtube_video = youtube_video.streams.get_highest_resolution()

print("Video Title:- ", youtube_video.title)

youtube_video.download(download_location)

print("Video Downloaded")


