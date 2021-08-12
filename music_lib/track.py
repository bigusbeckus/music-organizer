from os import sep
from os.path import join
from pathvalidate import sanitize_filename

class Track:
    src_file: str
    extension: str
    title: str
    artist: str
    album: str
    track_number: str
    disc_number: str

    separator = " - "

    def __init__(self, src_file, extension, title, artist, album='', track_number='', disc_number=''):
        self.src_file = src_file
        self.extension = extension
        self.title = sanitize_filename(title)
        self.artist = sanitize_filename(artist)
        self.album = sanitize_filename(album)
        self.track_number = track_number
        self.disc_number = disc_number

    def gen_hardlink_name(self) -> str:
        return f"{self.track_number + self.separator if self.track_number else ''}{self.title}{self.extension}"

    # Possible results:
    #   <dir>/Artist/Track
    #   <dir>/Artist/Album/Track
    #   <dir>/Artist/Album/Disc #/Track    
    def gen_hardlink_path(self, dest) -> str:
        path = join(dest, self.artist)
        if (self.album):
            path = join(path, self.album)
            # if (self.disc_number):
            #     path = join(path, f"Disc {self.disc_number}")
        path = join(path, self.gen_hardlink_name())
        return path