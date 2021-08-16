import sys, getopt, os
from elevate import elevate
from working_dir import WorkingDirs
from music_lib.library import Library
from music_lib.hierarchy import Hierarchy

CURRENT_VERSION = "version 0.1.0a"

ERR_ARGS = "ERROR: Invalid arguments"
ERR_DIRS = "ERROR: Invalid/Missing source or destination directory"
ERR_PERMISSION = "ERROR: Can not gain required privileges. Try running the program again as administrator"
EXIT_MSG = "Press any key to continue"

# dest_dirname =  sep + "Organized Music"

class MusicOrganizer:
    dest_dirname: str = os.sep + "Jellyfin Music"
    src: str = ''
    dest: str = ''
    folder_hierarchy: Hierarchy = Hierarchy.ARTIST_TRACK

    VALID_ARGS_SHORT = "s:d:"
    VALID_ARGS_LONG = [
        "aa", "aat", "artistalbum", "artistalbumtrack",
        "aad", "aadt", "artistalbumdisc", "artistalbumdisctrack",
        "src=", "source=", "from=",
        "dest=",  "destination=", "to="
    ]

    def handle_args(self, argv):
        try:
            opts, args = getopt.getopt(argv, self.VALID_ARGS_SHORT, self.VALID_ARGS_LONG)
        except:
            print(ERR_ARGS)
            input(EXIT_MSG)
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("--aa", "--aat", "--aad", "--aadt", "--artistalbum", "--artistalbumtrack", "--artistalbumdisc", "--artistalbumdisctrack"):
                if (opt in ("--aa", "--aat", "--artistalbum", "--artistalbumtrack")):
                    self.folder_hierarchy = Hierarchy.ARTIST_ALBUM_TRACK
                elif (opt in ("--aad", "--aadt", "--artistalbumdisc", "--artistalbumdisctrack")):
                    self.folder_hierarchy = Hierarchy.ARTIST_ALBUM_DISC_TRACK
            elif opt in ("-s", "--src", "--source", "--from"):
                self.src = arg
            elif opt in ("-d", "--dest", "--destination", "--to"):
                self.dest = arg
        
        if self.src == '':
            print(ERR_DIRS)
            input(EXIT_MSG)
            sys.exit(3)
        if self.dest == '':
            self.dest = self.src + self.dest_dirname

        if not os.path.isdir(self.src):
            print(ERR_DIRS)
            sys.exit(3)
        
        return WorkingDirs(self.src, self.dest)

    def main(self, argv):
        if os.name == 'nt':
            elevate()
        # os.system("color")
        # warningcolor = '\033[91m'
        # colorend = '\033[0m'
        directories = self.handle_args(argv)
        library = Library(directories.src, directories.dest, self.folder_hierarchy)
        try:
            library.read_music()
            library.create_hardlinks()
        except Exception as e:
            print(e)
        input(EXIT_MSG)        



if __name__ == "__main__":
    program = MusicOrganizer()
    program.main(sys.argv[1:])