from PIL import Image
import sys
import os
import GetMeta
import CreateVidFrames

videoHeight = 0
videoWidth = 0
videoCodec = ""
videoFPS = 0.0
videoURL = sys.argv[1]
currentFrame = 0
workingDir = "frameFold"

#os.remove("frameFold/*.*")

# Check for enough command arguments
if (len(sys.argv) < 2):
    print("Not enough CL arguments!")
    exit()

# Use video metadata for frame generation
videoHeight, videoWidth, videoCodec, videoFPS = GetMeta.findVideoMetada(videoURL)
CreateVidFrames.MakeFramesFromVideo(videoURL,"./frameFold/")

# Extract audio for the final video
print("Extracting audio...")
os.system("ffmpeg -i "+videoURL+" vidAudio.opus")

# Walk through the frame directory, and compress all frames beyond recognition
print("\nCompresing saved frames. This might take a while.")
for root, dirs, files in os.walk("./frameFold/", topdown=False):
   for name in files:
      if (".jpg" in os.path.join(root, name)):
          frameImg = Image.open(os.path.join(root, name))
          frameImg.save(os.path.join(root, name), quality=1)
          currentFrame += 1
          if (currentFrame % 100 == 0):
              print("Current Frame: "+str(currentFrame))

# combine all streams back into the final product
os.system("ffmpeg -framerate "+str(videoFPS)+" -i ./"+workingDir+"/frame%06d.jpg out.mp4")
os.system("ffmpeg -i out.mp4 -i vidAudio.opus finalJPG.mp4")
