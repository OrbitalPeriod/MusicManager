import youtube_dl
import subprocess
import sys
import os
from shutil import move
from argumentHandler import argumentHandler

destinationFolder= "Y:\Music"

def main():
    handler = argumentHandler(sys.argv, {
        add : {
            "-l" : [True, str],
            "-n" : [True, str]
        },
        remove : {
            "-n" : [True , str]
        },
        listFiles : {
        },
        version : {
        },
        help : {
           "-f" : [False, str] 
        }
    }, {'add' : add, 'remove' : remove, 'listfiles' : listFiles, '--version' : version, 'help' : help})
    handler.startFunction()

def add(args):
    link = args['-l']
    name = args['-n']

    downloadSong(link)
    for item in os.listdir():
        if item.endswith(".mp3"):
            move(item, destinationFolder + "/" + str(name) + ".mp3")
            

def downloadSong(link):
    ydl_opts = {'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def remove(args):
    songname = args['-n']

    try:
        os.remove(destinationFolder + "/" + songname)
    except IndexError:
        print("No argument given for removal")
        return
    except FileNotFoundError:
        print("File not found")
        return
    print("File succesfully removed")

def listFiles(args):
    for file in os.listdir(destinationFolder):
        print(file.replace(".mp3", ""))    

def version(args):
    print("version 1.0.0")

def help(args):
    function = None
    try:
        function = args['-f']
    except:
        pass
    
    if (function == None):
        print("Commands: \nadd - add music to library\nremove - remove song from library\nlistfiles - list current music files\n--version - list function\nuse the '-f' argument to get more information on each function")
    elif(function == 'add'):
        print("add")
    elif(function == 'remove'):
        print("remove")
    elif(function == 'listfiles'):
        print("listifles")
    elif(function == '--version'):
        print('--version')
    else:
        print("Commands: \nadd - add music to library\nremove - remove song from library\nlistfiles - list current music files\n--version - list function\nuse the '-f' argument to get more information on each function")

if __name__ == "__main__":
    main()
        
