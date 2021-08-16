# POSSIBLE HIERARCHIES
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
from enum import Enum, auto

class Hierarchy(Enum):
    ARTIST_TRACK = auto()
    ARTIST_ALBUM_TRACK = auto()
    ARTIST_ALBUM_DISC_TRACK = auto()

