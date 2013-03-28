import cv2
import cv
import time
from scipy import *
import numpy
import sys, os, random, hashlib
from math import *

manatee = cv.CaptureFromFile("manatee.mp4")
print manatee
print cv.GetCaptureProperty(manatee, cv.CV_CAP_PROP_FRAME_WIDTH)
print cv.GetCaptureProperty(manatee, cv.CV_CAP_PROP_FRAME_HEIGHT)

for i in xrange(10000):
    frame = cv.QueryFrame(manatee)
    if frame:
        print frame

#cv.NamedWindow("camera", 1)
#capture = cv.CaptureFromCAM(0)
# capture = cv.VideoCapture("manatee.mp4")

# for i in range(100):
#     img = cv.RetrieveFrame(capture)
#     cv.ShowImage("manatee.mp4", img)

# cv.DestroyAllWindows()

# vidFile = cv.CaptureFromFile( 'manatee.mp4' )

# nFrames = int(  cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FRAME_COUNT ) )
# fps = cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FPS )
# waitPerFrameInMillisec = int( 1/fps * 1000/1 )

# print 'Num. Frames = ', nFrames
# print 'Frame Rate = ', fps, ' frames per sec'

# for f in xrange( nFrames ):
#   frameImg = cv.QueryFrame( vidFile )
#   cv.ShowImage( "My Video Window",  frameImg )
#   cv.WaitKey( waitPerFrameInMillisec  )

# # When playing is done, delete the window
# #  NOTE: this step is not strictly necessary, 
# #         when the script terminates it will close all windows it owns anyways
# cv.DestroyWindow( "My Video Window" )

# # Load the image from designated filepath
# img = cv.LoadImageM( "dog.jpg" )

# # Create a window with given title (also used as unique identifier of this window)
# #   and insert the loaded image into this window
# cv.ShowImage( "My Photo Window",img )

# # Call graphics manager to update display 
# #  and keep displaying until user closes the window (which triggers buttonID = -1 )
# buttonID = cv.WaitKey(-1)
# while (buttonID >= 0):
#   buttonID = cv.WaitKey(-1)
#   print buttonID