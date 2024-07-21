import yt_dlp as youtube_dl

def download_video(url):
    ydl_opts = {
        'format': 'best',  
        'age_limit': 18,   
        'outtmpl': '%(title)s.%(ext)s', 
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except youtube_dl.DownloadError as e:
        print(f"Error downloading video: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)
