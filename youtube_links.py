from re import findall
from urllib.request import urlopen


def toSec(time):
    iki_nokta = time.find(':')
    return int(time[:iki_nokta]) * 60 + int(time[iki_nokta + 1:])

def toMin(time):
    return f'{time // 60}:{time % 60}'


def time_substractor(time1, time2):
    toSec1 = toSec(time1)
    toSec2 = toSec(time2)
    if toSec2 < toSec1: # make real_time2 bigger time always
        toSec1, toSec2 = toSec2, toSec1
    return toMin(toSec2 - toSec1)


def songs_youtube_id(liste, real_times):
    lst = []
    i = 0
    print('-----------------------------------------------------------------------------------------------------------')
    print('Program is taking youtube links right now. This might take a long time depends on how many songs you have, '
          'please be patient...')
    print('-----------------------------------------------------------------------------------------------------------\n')
    p = 0
    problems = []
    # for song_name in liste:
    while i < len(liste):
        song_name = liste[i]
        name = song_name.replace(' ', '+').encode('utf-8')
        html = urlopen(f'https://www.youtube.com/results?search_query={name}')
        video_ids = findall(r'watch\?v=(\S{11})', html.read().decode())
        html_again = urlopen(f'https://www.youtube.com/results?search_query={name}')  # i don't know why but i can't use re.findall second time for same string.
        video_times_tuple = findall(r'"simpleText":"(\S{2}):(\S{2})|"simpleText":"(\S):(\S{2})', html_again.read().decode())[::2]
        video_times_tuple_without_empty = [(tuple(int(x) if x.isdigit() else x for x in _ if x)) for _ in video_times_tuple]
        video_times_list = []
        for element in video_times_tuple_without_empty:
            video_times_list.append(f'{element[0]}:{element[1]}')
        i += 1
        print(f'Video ids: {video_ids[0]}')
        lst.append(video_ids[0])
    return lst


