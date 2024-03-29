# Mass-File-Renamer
Removes the long and unnecessary strings of text that come before and after media files when they're torrented or downloaded en mass.

A tool developed to change the name of a large number of files without having to manually edit them individually.  

The tool is focused on removing a beginning section of the name and an ending section. The sections are defined by the number of characters 
from the beginning of the string to the end of the section. It will ask for these values below, as well as a path to the folder containing 
the files, a file extension, and beginning text identifier that is commonly found at the beginning of each name.

For security and debugging purposes, all files that are renamed are stored in a log file in a folder titled `log_rename` created in the same directory as the script is run in, with the log files names `log_rename_DATE_TIME.txt`. The log file stores the old and new file name for each file that is renamed, in case the automode renames files incorrectly.

## Requirments

  - python3
  - pip
    - download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
    - install with `python3 get-pip.py`


## Run

NOTE: 
  - You only need to download the `rename-media-files.py` file, `find-ext.py` is used to specifically find the extensions of all files in the specified folder, but is not used by `rename-media-files.py`.

`python3 rename-media-files.py`


## Use

  ### Auto Mode
  Auto Mode takes a path to a folder with files to be renamed. The folder can contain other folders, only filenames will be renamed. Auto Mode looks for four files with similar starting and ending character sequences (strings) in each folder and removes those character sequences from each filename in that specific folder.

  NOTE:
  
  This is in v1.0, automode may incorrectly rename files, all old file names and new file names will be logged in the log file under the `log_rename` folder that is created when files are renamed. If you are worried about renaming too many files incorrectly, you can always edit the script to stop it from autorenaming and just output the new file names to the log file in order to check the validity before renaming the files. To do this comment out line 413 so that `os.rename(f_path+f,f_path+new_f)` is `#os.rename(f_path+f,f_path+new_f)`, this way files will not be renamed, but their new file names will be stored in the log file. 

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
  Standard mode requires the input of several key variables such as the path to the folder with the files to be renamed, the extension of the files to be renamed, specifically video files for now, the beginning string to get rid of, and the end string to get rid of.
  
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
  
