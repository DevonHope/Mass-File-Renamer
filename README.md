# Mass-File-Renamer
Removes the long and unnecessary strings of text that come before and after media files when they're torrented or downloaded en mass.

A tool developed to change the name of a large number of files without having to manually edit them individually.  

The tool is focused on removing a beginning section of the name and an ending section. The sections are defined by the number of characters 
from the beginning of the string to the end of the section. It will ask for these values below, as well as a path to the folder containing 
the files, a file extension, and beginning text identifier that is commonly found at the beginning of each name.

## Requirments

  - python3
  - pip
    - download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
    - install with `python3 get-pip.py`


## Run

`python3 rename-media-files.py`


## Use

  ### Auto Mode
  Auto Mode takes a path to a folder with files to be renamed. The folder can contain other folders, only filenames will be renamed. <br />
  Auto Mode looks for four files with similar starting and ending character sequences (strings) in each folder and removes those character <br /> 
  sequences from each filename in that specific folder.

  EXAMPLE:  
  
  - filenames:  
    - 30 Rock (2005) - S01E01 - NAME01 (bitrate or someshit 1080p).mkv  
    - 30 Rock (2005) - S01E02 - NAME02 (bitrate or someshit 1080p).mkv  
    - 30 Rock (2005) - S01E03 - NAME03 (bitrate or someshit 1080p).mkv   

  - input:  
    - path: 'C:\some\path\to\the\folder\with\your\files'  

  - output:  
    - E01 - NAME01.mkv  
    - E02 - NAME02.mkv  
    - E03 - NAME03.mkv  
  
  ### Standard Mode
  Standard mode requires the input of several key variables such as the path to the folder with the files to be renamed,  
  the extension of the files to be renamed, specifically video files for now, the beginning string to get rid of,  
  and the end string to get rid of.
  
  EXAMPLE:  
  
  - filenames:  
    - 30 Rock (2005) - S01E01 - NAME01 (bitrate or someshit 1080p).mkv  
    - 30 Rock (2005) - S01E02 - NAME02 (bitrate or someshit 1080p).mkv  
    - 30 Rock (2005) - S01E03 - NAME03 (bitrate or someshit 1080p).mkv 
  
  - input:  
    - path: 'C:\some\path\to\your\files'  
    - extension: '.mkv'  
    - front string: '30 Rock (2005) - '  
    - back string: ' (bitrate or someshit 1080p)'

  - output:  
    - E01 - NAME01.mkv  
    - E02 - NAME02.mkv  
    - E03 - NAME03.mkv 
  
