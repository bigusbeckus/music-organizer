import sys, getopt
import os
#from os import name, sep, getcwd
#from os.path import isdir
from elevate import elevate
from pathvalidate import is_valid_filename
from working_dir import WorkingDirs
from music_lib.track import Track
from music_lib.library import Library

ERR_ARGS = "ERROR: Invalid arguments"
ERR_DIRS = "ERROR: Invalid source or destination directory"
ERR_PERMISSION = "ERROR: Can not gain required privileges. Try running the program again as administrator"

# dest_dirname =  sep + "Organized Music"

class MusicOrganizer:
    dest_dirname: str = os.sep + "Jellyfin Music"
    src: str = ''
    dest: str = ''

    def handle_args(self, argv):
        try:
            opts, args = getopt.getopt(argv, "s:d:", ["src=", "dest=", "source=", "destination=", "from=", "to="])
        except:
            print(ERR_ARGS)
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-s", "--src", "--source", "--from"):
                self.src = arg
            elif opt in ("-d", "--dest", "--destination", "--to"):
                self.dest = arg
        
        if self.src == '':
            self.src = os.getcwd()
        if self.dest == '':
            self.dest = self.src + self.dest_dirname

        if not os.path.isdir(self.src):
            print(ERR_DIRS)
            sys.exit(3)
        
        return WorkingDirs(self.src, self.dest)

    def main(self, argv):
        if os.name == 'nt':
            elevate()
        os.system("color")
        warningcolor = '\033[91m'
        colorend = '\033[0m'
        directories = self.handle_args(argv)
        library = Library(directories.src, directories.dest)
        try:
            library.create_hardlinks()
        except Exception as e:
            print(e)
        input("Press any key to close")
        # track = Track("mp3", "GOMD", "J. Cole", "Forest Hill Drive", "1")
        # print(track.gen_symlink_path(directories.dest))
        # print('...')
        



if __name__ == "__main__":
    program = MusicOrganizer()
    program.main(sys.argv[1:])