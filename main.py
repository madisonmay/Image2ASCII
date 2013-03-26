# http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
# Made by the illustrious Bill Warner, Madison May, Mitchell Kwock, and Jacob Kingery
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import time
import os

asciiGroup = [' ', '.', '-', 'o', '*', '%', '#']

def delete_f():
   try:
      s=raw_input('Enter a file name: ')
      os.remove(s)
   except AttributeError: print('Input is not a valid file in this directory.')

def get_agray(s):
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
         uncolored = weighted
         gray[y].append(uncolored)
   return gray

def scale(s, x = 144, y = -1):
   pic = get_agray(s)
   w = x
   if(y > 0):
      h = y
   else:
      print(len(pic), len(pic[0]))
      scaled = 0.5 * w * len(pic) // (len(pic[0]))
      h = int(scaled)
   xPortion = len(pic) / float(h)
   yPortion = len(pic[0]) / float(w)

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
               row.append(total // number)
            else:
               row.append(0)
      new_pic.append(row)
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

if(__name__ == '__main__'):
   start = time.clock()
   pic = raw_input("Name of Image: ")
   inverted = False
   typed = raw_input("Invert colors? [y for yes, default no]")
   if(typed.lower() == "y"):
      inverted = True
   ascii = scale(pic)
   printAscii(ascii, inverted)
   end = time.clock()
   print(end - start)