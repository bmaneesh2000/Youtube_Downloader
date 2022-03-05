from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
print(playlist[1].title().lower())