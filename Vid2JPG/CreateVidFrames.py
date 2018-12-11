import os

def MakeFramesFromVideo(pathToInputVideo,folderDir):
    os.system("ffmpeg -i "+pathToInputVideo+" "+folderDir+"frame%06d.jpg -hide_banner")
