#from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageEnhance
import time
import cProfile
from ticktock import *
import webbrowser

from PIL import Image, ImageSequence
import sys, os
filename = "photos/Freetiel.gif"#sys.argv[1]
im = Image.open(filename)
original_duration = im.info['duration']

frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
frames.reverse()

from images2gif import writeGif
writeGif("reverse_" + os.path.basename(filename), frames, duration=original_duration/1000.0, dither=0)