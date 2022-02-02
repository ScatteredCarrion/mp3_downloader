from yt_dlp import YoutubeDL


def download(lst):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outmpl': 'C:\\Users\\Hardal\\PycharmProjects\\spotify_to_mp3\\Musics\\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',}]
    }
    for video_id in lst:
        video = 'https://youtube.com/watch?v=' + video_id
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(video)

link = ''

if __name__ == '__main__':
    download([link])
