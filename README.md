# Music Organizer (Work in progress)
Uses the embeded tags from music files to create a music directory with a structure compatible with Jellyfin, Plex, and Emby libraries. Works without changing the original files and directories, or making copies (uses hard links basically).

## Features
* Creates a music directory with a structure compatible with Jellyfin, Plex, Emby, and other similar apps and stores it in its own separate folder
* Uses hard links to prevent file duplication and to keep the original files and directory structures intact
* Uses embeded tags from the music files to create the folder structure (if the tags are a mess, this won't work well)

Current behavior is to create a folder called "Jellyfin Music" in whatever destination folder ends up being and creating the organized folder structure there.
Folder name can be changed by modifying the `dest_dirname` variable in the `organizer.py` file

Future versions will add support for custom folders and such without having to edit anything...and will be less of a mess.

## TODO
* Cleanup. Lots and lots of cleanup
* CLI improvements
* `--help` argument
* Make an actual GUI maybe

## Supported formats

* `.aac`
* `.aiff`
* `.dsf`
* `.flac`
* `.m4a`
* `.mp3`
* `.ogg`
* `.opus`
* `.wav`
* `.wv`

(Basically any format supported by the [music-tag library](https://pypi.org/project/music-tag/))

## Expected Result Formats (Final Directory Structure)
#### 1. Artist → Track (Default)

    /Music
        /Artist
            01 - Song.flac
            02 - Song.flac
#### 2. Artist → Album → Track

    /Music
        /Artist
            /Album
                01 - Song.ogg
                02 - Song.ogg
#### 3. Artist → Album → Disc → Track

    /Music
        /Artist
            /Album
                /Disc 1
                    01 - Song.mp3
                    02 - Song.mp3
                /Disc 2
                    01 - Song.mp3
                    02 - Song.mp3
## Arguments

Argument | Action
-------- | ------
`-s` , `--source` , `--src` , `--from` | Set source directory
`-d` , `--destination` , `--dest` , `--to` | Set destination directory
`--aa` , `--aat`, `--artistalbum`, `--artistalbumtrack` | Set mode to **Artist → Album → Track**
`--aad` , `--aadt`, `--artistalbumdisc`, `--artistalbumdisctrack` | Set mode to **Artist → Album → Disc → Track**

*Arguments listed in the same cell are interchangeable*

## Usage
#### 1. Using both source and destination

    py organizer.py --source "C:\Users\Foo\Music" --destination "C:\Users\Foo\Desktop\MusicLib"

Creates hard links for all supported music files inside `C:\Users\Foo\Music` and puts them in `C:\Users\Foo\Desktop\MusicLib\Jellyfin Structures` organized in the **Artist → Track** format
#### 2. Using only source

    py organizer.py --source "C:\Users\Foo\Music"

Creates hard links for all supported music files inside `C:\Users\Foo\Music` and puts them in `C:\Users\Foo\Music\Jellyfin Structures` organized in the **Artist → Track** format
#### 3. Using only source with the `--artistalbum` argument

    py organizer.py --artistalbum --source "C:\Users\Foo\Music"

Creates hard links for all supported music files inside `C:\Users\Foo\Music` and puts them in `C:\Users\Foo\Music\Jellyfin Structures` organized in the **Artist → Album → Track** format
#### 4. Using only source with the `--aadt` argument

    py organizer.py --aadt --source "C:\Users\Foo\Music"

Creates hard links for all supported music files inside `C:\Users\Foo\Music` and puts them in `C:\Users\Foo\Music\Jellyfin Structures` organized in the **Artist → Album → Disc → Track** format 

## Requrements
* Python 3.8.4 or newer
* [music-tag](https://pypi.org/project/music-tag/) library
* [pathvalidate](https://pypi.org/project/pathvalidate/) library

## Instructuins
#### 1. Clone the repository

    git clone https://github.com/BigusBeckus/music-organizer.git
    
#### 2. Install music-tag

    pip install music-tag
    
#### 3. Install pathvalidate

    pip install pathvalidate
    
#### 4. Run from `organizer.py` as shown [above](#Usage)
    
