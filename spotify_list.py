from spotipy import Spotify, SpotifyException
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError
from cred import *


def ms_to_min_and_sec(ms):
    minute = ms / 60000
    minute_exact_part = ms // 60000
    second = (minute - minute_exact_part) * 60
    return '{}:{:.0f}'.format(minute_exact_part, second)


def real_limit_remover(number_of_song, func, playlist_id, limit=50, offset=0):
    liste = []
    duration_list = []
    track_number = 0
    print('Getting musics from Spotify playlist.')
    if number_of_song > limit:
        total_repeat = number_of_song // limit
        for i in range(total_repeat):
            results = func(playlist_id, limit=limit, offset=offset)
            offset += limit
            for item in results['items']:
                track_number += 1
                track = item['track']
                duration = ms_to_min_and_sec(track['duration_ms'])
                print(track_number, track['artists'][0]['name'], " - ", track['name'])
                liste.append('{} - {}'.format(track['artists'][0]['name'], track['name']))
                duration_list.append(duration)
    else:
        results = func(playlist_id, limit=number_of_song, offset=offset)
        for item in results['items']:
            track_number += 1
            track = item['track']
            duration = ms_to_min_and_sec(track['duration_ms'])
            print(track_number, track['artists'][0]['name'], " - ", track['name'])
            liste.append('{} - {}'.format(track['artists'][0]['name'], track['name']))
            duration_list.append(duration)
    print('\n')
    return liste, duration_list



# sp = Spotify(auth_manager=SpotifyOAuth())
sp = Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret= SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))
# --------------------------------------------------------------------------------------------------------------
playlist = 'https://open.spotify.com/playlist/3zPVh9fcGkLxj64t4h1VgK?si=ef3c939bbe174f9c'  # depressive
playlist2 = 'https://open.spotify.com/playlist/3qQtS2YT10cxVbBneuoaSG?si=dc013f0958b04ae2'  # asd
playlist3 = 'https://open.spotify.com/playlist/4RdWu4fz3lyvue87a5QgG8?si=01c4c8f173c8498a'  # qwe
function = sp.playlist_items
total = function(playlist)['total']
song_number = 30
# --------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print(real_limit_remover(song_number, function, playlist, offset=total - song_number))


