from genericpath import exists
from os import link, mkdir, listdir, link
from os.path import join, isdir
from typing import List
from music_lib.track import Track
from music_lib.hierarchy import Hierarchy 

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

    folder_hierarchy: Hierarchy

    def __init__(self, src, dest, folder_hierarchy = Hierarchy.ARTIST_TRACK):
        self.src = src
        self.dest = dest
        self.folder_hierarchy = folder_hierarchy
        # self.read_music(self.src)

    def read_music(self, __src = None):
        if __src is None:
            __src = self.src
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
            linkpath = join(self.dest, track.artist) # dest/Artist
            if not isdir(linkpath):
                mkdir(linkpath)
            if track.album and self.folder_hierarchy in (Hierarchy.ARTIST_ALBUM_TRACK, Hierarchy.ARTIST_ALBUM_DISC_TRACK):
                linkpath = join(linkpath, track.album) # dest/Artist/Album
                if not isdir(linkpath):
                    mkdir(linkpath)
                if track.disc_number and self.folder_hierarchy == Hierarchy.ARTIST_ALBUM_DISC_TRACK:
                    linkpath = join(linkpath, f"Disc {track.disc_number}") # dest/Artist/Album/Disc #
                    if not isdir(linkpath):
                        mkdir(linkpath)
            linkpath = join(linkpath, track.gen_hardlink_name()) # dest/Artist/<Album/Disc #>/Track
            if not exists(linkpath):
                link(track.src_file, linkpath)