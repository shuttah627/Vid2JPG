#!/usr/local/bin/python3
import subprocess
import shlex
import json

# function to find the resolution of the input video file
def findVideoMetada(pathToInputVideo):
    cmd = "ffprobe -v quiet -print_format json -show_streams"
    args = shlex.split(cmd)
    args.append(pathToInputVideo)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    ffprobeOutput = subprocess.check_output(args).decode('utf-8')
    ffprobeOutput = json.loads(ffprobeOutput)

    # prints all the metadata available:
    #import pprint
    #pp = pprint.PrettyPrinter(indent=2)
    #pp.pprint(ffprobeOutput)

    # for example, find height and width
    height = ffprobeOutput['streams'][0]['height']
    width = ffprobeOutput['streams'][0]['width']
    codec_name = ffprobeOutput['streams'][0]['codec_name']
    fps = ffprobeOutput['streams'][0]['avg_frame_rate']

    if ('/' in fps):
        temp = fps.split('/')
        fps = int(temp[0]) / int(temp[1])
    
    return height, width, codec_name, fps
