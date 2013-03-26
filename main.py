# http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import os

asciiGroup = [' ', '.', '-', 'o', '*', '%', '#']

def menu():
   order = raw_input('?: ')
   if (order=='grayify'):
      grayify()
      menu()
   elif(order=='delete'):
      delete_f()
      menu()
   elif(order=='array'):
      s=raw_input('Enter a file name: ')
      get_array(s)
      menu()
   elif (order=='exit'): return
   else: menu()
def grayify():
   try: get_gray(s=raw_input('Enter a file name: '))
   except IOError: print('Input is not a valid image in this directory.')
def get_gray(s):
   im = Image.open(s+'.jpg')
   i = ImageOps.grayscale(im)
   i.save(s+'-grayscale.jpg')
   print('A grayscale version of your image is now saved as '+s+'-grayscale.jpg.')

def get_array(s):
   im = Image.open(s+'.jpg')
   imageW = im.size[0]
   imageH = im.size[1]
   rgb = []
   for y in range(imageH):
      rgb.append([])
      for x in range(imageW):
         xy = (x, y)
         rgb[y].append(im.getpixel(xy))
        #f = open(s+'-array.txt','w')
        #f.write(str(rgb))
        #f.close()
   return rgb

def get_agray(s):
   im = Image.open(s+'.jpg')
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
#                        print(colored)
         uncolored = weighted
         gray[y].append(uncolored)
        #f = open(s+'-array.txt','w')
        #f.write(str(rgb))
        #f.close()
   return gray

def scale(s, height, width):
   pic = get_agray(s)
   xPortion = len(pic) / float(width)
   yPortion = len(pic[0]) / float(height)

   new_pic = []
   for i in range(height): #Goes through each row
      row = []
      for j in range(width): #Goes through portion of a row
         total = 0
         number = 0
         for m in range(int(i * yPortion),int((i + 1) * yPortion)):
            for n in range(int(j * xPortion), int((j + 1) * xPortion)):
               total = total + pic[m][n]
               number = number + 1
         row.append(total // number)
      new_pic.append(row)
   return new_pic

def printAscii(pic):
   for row in pic:
      printed = ''
      for pixel in row:
#         print(type(pixel), type(asciiGroup))
         printed = printed + asciiGroup[len(asciiGroup) - 1 - (pixel * len(asciiGroup))//256]
      print(printed)

def delete_f():
   try:
      s=raw_input('Enter a file name: ')
      os.remove(s)
   except AttributeError: print('Input is not a valid file in this directory.')

def test_f(arr):
   d = set()
   dist = {}
   for r in range(len(arr)):
      for c in range(len(arr[r])):
         d.add(str(arr[r][c]))
         try:
            dist[arr[r][c]]+=1
         except KeyError:
            dist[arr[r][c]]=1
   print(d)
   print(len(d))
   test = []
   for k,v in dist.items():
      test.append((v,k))
   test.sort()
   print(test)


#pic = get_agray('smiley')
pic = scale('smiley', 20, 35)
printAscii(pic)
'''
for row in pic:
   printed = ''
   for pixel in row:
      if(pixel > 127):
         printed = printed + ' '
      else:
         printed = printed + '#'
   print(printed)
