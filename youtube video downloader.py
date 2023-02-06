from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    video = yt.streams.first()
    video.download(path)
    print("Video downloaded successfully!")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    path = input("Enter the directory path to download the video: ")
    download_video(url, path)
