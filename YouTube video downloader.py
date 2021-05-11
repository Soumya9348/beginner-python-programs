from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")


# for downloading multiple videos, store the links in a list and use 'for' loop.
# Sometimes we want only the audio from the YouTube video URL. We can use the get_audio_only() function for this.
