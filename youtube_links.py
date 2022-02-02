from re import findall
from urllib.request import urlopen


def time_substractor(time1, time2):
    iki_nokta_1 = time1.find(':')
    iki_nokta_2 = time2.find(':')
    minute1 = int(time1[:iki_nokta_1])
    second1 = int(time1[iki_nokta_1 + 1:])
    minute2 = int(time2[:iki_nokta_2])
    second2 = int(time2[iki_nokta_2 + 1:])
    if minute2 > minute1:
        pass
    elif minute2 == minute1:
        if second2 > second1:  # make time2 bigger time always
            pass
        else:
            tmp = second1
            second1 = second2
            second2 = tmp
            temp = minute1
            minute1 = minute2
            minute2 = temp
    else:  # make time2 bigger time always
        tmp = second1
        second1 = second2
        second2 = tmp
        temp = minute1
        minute1 = minute2
        minute2 = temp
    minute = minute2 - minute1
    second = second2 - second1
    if second < 0:
        minute -= 1
        second += 60
    return abs(minute)

def songs_youtube_id(liste, real_times):
    lst = []
    i = 0
    print('-----------------------------------------------------------------------------------------------------------')
    print('Program is taking youtube links right now. This might take a long time depends on how many songs you have, '
          'please be patient...')
    print('-----------------------------------------------------------------------------------------------------------\n')
    p = 0
    avec_probleme = []
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
        try:  # checking video times.
            if time_substractor(real_times[i], video_times_list[0]) < 1:
                print(f'babuş ilk yere girdi\nspotify:{real_times[i]}\nyoutube:{video_times_list[0]}')
                lst.append(video_ids[0])
                print(f'{song_name}: {video_ids[0]}')
                print('------------------------------------\n')
                p = 0
            elif time_substractor(real_times[i], video_times_list[1]) < 1:
                print(f'babuş ikinci yere girdi\nspotify:{real_times[i]}\nyoutube:{video_times_list[1]}')
                lst.append(video_ids[1])
                print(f'{song_name}: {video_ids[1]}')
                print('------------------------------------\n')
                p = 0
            elif time_substractor(real_times[i], video_times_list[2]) < 1:
                print(f'babuş üçüncü yere girdi\nspotify:{real_times[i]}\nyoutube:{video_times_list[2]}')
                lst.append(video_ids[2])
                print(f'{song_name}: {video_ids[2]}')
                print('------------------------------------\n')
                p = 0
            else:
                print(video_times_list, '\n')
                print('kendisi:', real_times[i])
                print('Kardeş bir sorun var bu şarkıda kb.\n')
                p += 1
                if p < 4:
                    i -= 1
                else:
                    avec_probleme.append(song_name)
        except IndexError:
            print('AGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        except ValueError:
            print(video_times_tuple, '\n')
            print(video_times_list, '\n')
            print('real_time:', real_times[i])
            print('video_time:', video_times_list, '\n')
        i += 1
    return lst

