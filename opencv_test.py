import cv

#cv.NamedWindow('Window Test', cv.CV_WINDOW_AUTOSIZE)
image = cv.LoadImage("drag.jpg", cv.CV_LOAD_IMAGE_COLOR)

cv.ShowImage("Dragon", image)
cv.WaitKey()