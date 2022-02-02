from spotify_list import real_limit_remover
from youtube_links import songs_youtube_id
from downloader import download
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from os import system


sp = Spotify(auth_manager=SpotifyOAuth())
# --------------------------------------------------------------------------------------------------------------
playlist1 = 'https://open.spotify.com/playlist/3zPVh9fcGkLxj64t4h1VgK?si=ef3c939bbe174f9c'  # depressive
playlist2 = 'https://open.spotify.com/playlist/3qQtS2YT10cxVbBneuoaSG?si=dc013f0958b04ae2'  # asd
playlist3 = 'https://open.spotify.com/playlist/4RdWu4fz3lyvue87a5QgG8?si=01c4c8f173c8498a'  # qwe
playlist4 = 'https://open.spotify.com/playlist/0y0C5XTdCMmYe4XmMLNkre?si=ca59d5b381f54460'  # anadolu
function = sp.playlist_items  # sonuna () koymadan yap krdşm
limit = 100
# --------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print('Which playlist do you want?')
    choose = input('asd, qwe, depressive, anadolu:\n')
    if choose.lower() == 'asd':
        liste = playlist2
    elif choose.lower() == 'anadolu':
        liste = playlist4
    elif choose.lower() == 'depressive':
        liste = playlist1
    elif choose.lower() == 'qwe':
        liste = playlist3
    else:
        print('This playlist is not in database. Please input your playlist link yourself.')
        liste = input('')
    total = function(liste)['total']
    print('')
    song_number = input('How many song do you want? (Send empty string for all list.)\n')
    if song_number == '':
        song_number = total
    else:
        song_number = int(song_number)
    print('')
    offset_inpt = str(input('Which song do you want to start? (Send empty string for 0.)\n'))
    if offset_inpt == '':
        offset = total - song_number
    else:
        offset = total - int(offset_inpt)
    f = real_limit_remover(song_number, function, liste, limit=limit, offset=offset)
    download(songs_youtube_id(f[0], f[1]))
    system('move C:\\Users\\Hardal\\PycharmProjects\\spotify_to_mp3\\*.mp3 C:\\Users\\Hardal\\PycharmProjects\\spotify_to_mp3\\Musics')
    # songs_youtube_id(f[0], f[1])
