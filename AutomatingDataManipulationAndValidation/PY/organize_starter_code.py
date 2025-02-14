import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png'],
    "PY" :['.py'],
    "JAVA":['.java'],
    "TXT":['.txt'],
    "JSON":['.json'],
    "CSV":['.csv'],
    "XML":['.xml']
    }

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "No subdirectory"

# test out the pickDirectory() function
# uncomment this line and write your code

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            print(item.name)
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory() 
