# POSSIBLE STRUCTURES
# ========================================
#
#  1.  Artist -> Track
#       /Music
#          /Artist
#              01 - Song.flac
#              02 - Song.flac
#          08 - Song.ogg
#          09 - Song.ogg
#
#  2.  Artist -> Album -> Track
#       /Music
#          /Artist
#              /Album
#                  01 - Song.mp3
#                  02 - Song.mp3
#
#  3.  Artist -> Album -> Disc # -> Track
#       /Music
#          /Artist
#              /Album
#                  /Disc 1
#                      01 - Song.mp3
#                      02 - Song.mp3
#                  /Disc 2
#                      01 - Song.mp3
#                      02 - Song.mp3

from genericpath import exists
from os import link, mkdir, listdir, link
from os.path import join, isdir
from typing import List
from music_lib.track import Track

import pathlib
import music_tag

class Library:
    SUPPORTED_FORMATS = [
        ".aac",
        ".aiff",
        ".dsf",
        ".flac",
        ".m4a",
        ".mp3",
        ".ogg",
        ".opus",
        ".wav",
        ".wv"
    ]
    tracks: List[Track] = []
    src: str
    dest: str

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.read_music(self.src)

    def read_music(self, __src):
        if not exists(join(__src, ".ignore")):
            for d in listdir(__src):
                current = join(__src, d)
                if (isdir(current)):
                    self.read_music(current)
                else:
                    ext = pathlib.Path(d).suffix
                    if ext.lower() in self.SUPPORTED_FORMATS:
                        # print(ext)
                        track = music_tag.load_file(current)
                        if track['artist']:
                            artist = str(track['artist'].first)
                            artist = artist.split(';')[0]
                            artist = artist.split('/')[0]
                            # print(artist)
                            self.tracks.append(Track(
                                current,
                                ext,
                                str(track['title'].first),
                                artist,
                                str(track['album'].first),
                                str(track.raw['tracknumber'].first),
                                str(track.raw['discnumber'].first)
                            ))

    def create_hardlinks(self):
        if not isdir(self.dest):
            mkdir(self.dest)
        for track in self.tracks:
            linkpath = join(self.dest, track.artist)
            if not isdir(linkpath):
                mkdir(linkpath)
            if track.album:
                linkpath = join(linkpath, track.album)
                if not isdir(linkpath):
                    mkdir(linkpath)
            linkpath = join(linkpath, track.gen_hardlink_name())
            if not exists(linkpath):
                link(track.src_file, linkpath)