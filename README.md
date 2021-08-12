# Music Organizer (Work in progress)
Uses embeded tags and hard links to create a music folder structure compatible with Jellyfin, Plex, and Emby based on embeded metadata without changing the originals, or making copies

## Features
* Creates music folder structure compatible with Jellyfin, Plex, Emby, and other similar apps and store it in its own separate folder
* Uses hard links to prevent file duplication and prevent the original files from being moved around
* Uses embeded tags from the files to create the folder structure (if your tags are a mess, this isn't for you)

Current behavior is to create a folder called "Jellyfin Music" in whatever destination folder ends up being and creating the organized folder structure there.
Folder name can be changed by modifying the `dest_dirname` variable in the `organizer.py` file

Future versions will add support for custom folders and such without having to edit anything...and will be less of a mess.

## TODO
* Cleanup. Lots and lots of cleanup
* Command interface improvements
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

## Arguments

Argument | Action
-------- | ------
`-s` , `--source` , `--src` , `--from` | Set source directory
`-d` , `--destination` , `--dest` , `--to` | Set destination directory


## Usage


#### 1. Using both source and destination

    py organizer.py --source "C:\Users\Foo\Music" --destination "C:\Users\Foo\Desktop\MusicLib"

Creates hard links for all supported music files inside `C:\Users\Foo\Music` and puts them in `C:\Users\Foo\Desktop\MusicLib\Jellyfin Structures`

#### 2. Using only source

    py organizer.py --source "C:\Users\Foo\Music"

Creates hard links for all supported music files inside `C:\Users\Foo\Music` and puts them in `C:\Users\Foo\Music\Jellyfin Structures`

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
    
#### 4. Run from `organizer.py` as shown [above](#Arguments)
    
