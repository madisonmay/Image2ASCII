# http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
# Made by the illustrious Bill Warner, Madison May, Mitchell Kwock, and Jacob Kingery
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import time
import os

'''
Currently, this works at converting any type of picture to an
ASCII gradient-based text.  Only contains 7 different characters
or shades, so be sure to modify that if necessary.
'''

###### CONFIGURATIONS #####

#The Dictionary for the ASCII gradient.  Order from LEAST dense to MOST dense
asciiGroup = [' ', '.', '-', 'o', '*', '%', '#']

#Display the total time it requires to convert the image from image to ASCII
display_run_time = False

#Whether or not the program asks for a resolution of the image
ask_for_res = True

#Scale the gradient so that it ranges from 0 to 255 regardless of the original color range
scale_gray = True

def get_agray(s):
   '''
   Takes an image and returns the GRAY SCALE version of the image regardless of the file type.
   The GRAY SCALE version is a 2-Dimensional array of the GRAYdient.  (A single value 0-255)
   '''
   im = Image.open(s)
   imageW = im.size[0]
   imageH = im.size[1]
   gray = []
   for y in range(imageH):
      gray.append([])
      for x in range(imageW):
         xy = (x, y)
         colored = im.getpixel(xy)
         if(type(colored) is int):
            weighted = colored
         else:
            weighted = colored[0] * 0.21 + colored[1] * 0.71 + colored[2] * 0.07
         gray[y].append(weighted)
   return gray

def scale(s, x = 144, y = -1):
   pic = get_agray(s)
   if(x < 1):
      w = 144
   else:
      w = x
   if(y > 0):
      h = y
   else:
      scaled = 0.5 * w * len(pic) // (len(pic[0]))
      h = int(scaled)
   xPortion = len(pic) / float(h)
   yPortion = len(pic[0]) / float(w)

   highest = 0
   lowest = 255

   new_pic = []
   for j in range(h): #Goes through each row
      row = []
      for i in range(w): #Goes through portion of a row
         total = 0
         number = 0
         ended = False
         for n in range(int(j * xPortion), int((j + 1) * xPortion)):
            for m in range(int(i * yPortion),int((i + 1) * yPortion)):
               try:
                  total = total + pic[n][m]
               except IndexError:
                  print('Error')
                  ended = True
               number = number + 1
         if not ended:
            if(number > 0):
               value = total / float(number)
               row.append(value)
            else:
               value = 0
               row.append(value)
            if(value > highest):
               highest = value
            if(value < lowest):
               lowest = value
      new_pic.append(row)
   if(scale_gray):
         for i in range(len(new_pic)):
            for j in range(len(new_pic[i])):
               new_pic[i][j] = int((new_pic[i][j] - lowest) * 255 / (highest - lowest))
   return new_pic

def printAscii(pic, isInverted = False):
   printed = ''
   for row in pic:
      for pixel in row:
         if(type(pixel) is str):
            print pixel
         if(not isInverted):
            printed = printed + asciiGroup[int((pixel * len(asciiGroup)//256))]
         else:
            printed = printed + asciiGroup[int(len(asciiGroup) - (pixel * len(asciiGroup))//256 - 1)]
      printed = printed + '\n'
   print(printed)

def ask_for_int(s):
   valid = False
   while not valid:
      typed = raw_input(s)
      if(len(typed) == 0):
         return -1
      try:
         value = int(typed)
         valid = True
      except ValueError:
         valid = False
         print("NaN")
   return value

if(__name__ == '__main__'):
   pic = raw_input("Name of Image: ")
   inverted = False
   typed = raw_input("Invert colors? [y for yes, default no]")
   if(typed.lower() == "y"):
      inverted = True
   width = -1
   height = -1
   if(ask_for_res):
      width = ask_for_int("What width? ")
      height = ask_for_int("What height? ")
   start = time.clock()
   if(width > 0 or height > 0):
      ascii = scale(pic, width, height)
   else:
      ascii = scale(pic)
   printAscii(ascii, inverted)
   if(display_run_time):
      print(time.clock() - start)
