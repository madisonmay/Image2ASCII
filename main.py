# http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
# Made by the illustrious Bill Warner, Madison May, Mitchell Kwock, and Jacob Kingery
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import time
import cProfile


'''
/begin_author("Mitchell")

Currently, this works at converting any type of picture to an
ASCII gradient-based text.  Only contains 7 different characters
or shades, so be sure to modify that if necessary.

There are TWO versions.  Version 1 is reliable, but currently about
a factor of 70 times as slow.  Version 2 is also reliable and considerably
Faster.  I wouldn't even try Version 1 anymore.

Most of the general code can be changed in begin() for higher level options.
So make sure that that's where things are modified around the actual processor.

/end_author("Mitchell")
'''



##### BEGIN CONFIGURATIONS #####

#The Dictionary for the ASCII gradient.  Order from LEAST dense to MOST dense
# Padded spaces at the end of this dictionary can effectively "White Balance"
# Could also consider scaling gradient of only high and low values
asciiWeb = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'..........                "
asciiWeb = asciiWeb[::-1]
#asciiGroup = list(asciiWeb)
asciiGroup = [' ', '.', '-', 'o', '*', '%', '#']

#Display the total time it requires to convert the image from image to ASCII
display_run_time = True

#Whether or not the program asks for a resolution of the image
ask_for_res = True

#Scale the gradient so that it ranges from 0 to 255 regardless of the original color range
scale_gray = True

#Which version of the converter to use.
#Version 1: Opens the image and scales it down
#Version 2: Opens the image using draft to prescale it before hand
version = 2

##### END CONFIGURATIONS #####

start = time.time()


##### BEGIN VERSION 1 #####

def get_agray(s): #DEPRECATED, IMPROVED IN get_grayscale.  If you want to test, use VERION 1
   '''
   Takes an image and returns the GRAY SCALE version of the image regardless of the file type.
   The GRAY SCALE version is a 2-Dimensional array of the GRAYdient.  (A single value 0-255)
   '''
   im = Image.open(s)
   imHeight = im.size[1]
   imWidth = im.size[0]
   gray = []
   for y in range(imHeight):
      gray.append([])
      for x in range(imWidth):
         xy = (x, y)
         colored = im.getpixel(xy)
         if(type(colored) is int):
            weighted = colored
         else:
            weighted = colored[0] * 0.21 + colored[1] * 0.71 + colored[2] * 0.07
         gray[y].append(weighted)
   return gray

def scale(s, x = 144, y = -1):
   '''Scales and converts a picture into a suitable grayscale equivalent.  Can also scale the gradient if scale_gray is True.
   This is the primary function used to convert the picture.
   '''
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

##### END VERSION 1 #####

##### BEGIN VERSION 2 #####

def get_grayscale(s, x = -1, y = -1):
   im = Image.open(s)
   height = im.size[1]
   width = im.size[0]
   if(x < 1):
      w = 144
   else:
      w = x
   if(y > 0):
      h = y
   else:
      scaled = 0.5 * w * height // (width)
      h = int(scaled)

   size = (w, h)
   im.draft("L", im.size)
   im = im.resize(size)

   highest = 0
   lowest = 255
   gray = []
   for y in range(h):
      gray.append([])
      for x in range(w):
         val = im.getpixel((x,y))
         if(type(val) is int):
            weighted = val
         else: #Necessary for PNG's.  Weights the values then scales them according to the transparency
            weighted = val[0] * 0.21 + val[1] * 0.71 + val[2] * 0.07
            weighted = weighted * val[3] // 255
         gray[y].append(weighted)
         if(weighted > highest):
            highest = weighted
         if(weighted < lowest):
            lowest = weighted

   if scale_gray and highest != lowest:
      for i in range(len(gray)):
         for j in range(len(gray[i])):
            gray[i][j] = int((gray[i][j] - lowest) * 255 / (highest - lowest))
   return gray

##### END VERSION 2 #####

#### Misc. QOL functions useful for timing and testing


def printAscii(pic, isInverted = False):
   '''Uses ASCIIgroup and the grayscale obtained from scale to print the ascii picture'''
   printed = ''
   for row in pic:
      for pixel in row:
         if isInverted:
            printed = printed + asciiGroup[int(len(asciiGroup) - (pixel * len(asciiGroup))//256 - 1)]
         else:
            printed = printed + asciiGroup[int((pixel * len(asciiGroup)//256))]
      printed = printed + '\n'
   print(printed)

def ask_for_int(s):
   '''Purely here to ask for an integer in a condensed matter'''
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

def tick(): #Resets start time
   global start
   start = time.time()

def tock(): #Prints time since start time in seconds
   print(time.time() - start)

def begin():
   '''Using Configurations to process whatever image with needs in order
   to make the ASCII image.  Prints out in the terminal, but can be printed
   to a text file if pipelined into one.'''
   global scale_gray
   pic = raw_input("Name of Image: ")
   typed = raw_input("Invert colors? [y|N] ")
   if(ask_for_res):
      width = ask_for_int("What width? ")
      height = ask_for_int("What height? ")
   else:
      width = -1
      height = -1
   if(raw_input("Scale Gradient? [Y|n] ").lower() == "n"):
      scale_gray = False
   inverted = typed.lower() == "y"

   tick()
   if version is 2:
      ascii = get_grayscale(pic, width, height)
   elif version is 1:
      if(width > 0 or height > 0):
         ascii = scale(pic, width, height)
      else:
         ascii = scale(pic)

   printAscii(ascii, inverted)

   if(display_run_time):
      tock()

if(__name__ == "__main__"):
   begin()
