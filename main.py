# http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import time
import os

asciiGroup = [' ', '.', '-', 'o', '*', '%', '#']

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

def delete_f():
   try:
      s=raw_input('Enter a file name: ')
      os.remove(s)
   except AttributeError: print('Input is not a valid file in this directory.')

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
         uncolored = weighted
         gray[y].append(uncolored)
        #f = open(s+'-array.txt','w')
        #f.write(str(rgb))
        #f.close()
   return gray

def scale(s, x = 144, y = -1):
   w = x
   if(y > 0):
      h = y
   else:
      h = w // 2
   pic = get_agray(s)
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
            row.append(total // number)
      new_pic.append(row)
   return new_pic

def printAscii(pic):
   printed = ''
   for row in pic:
#      printed = ''
      for pixel in row:
         printed = printed + asciiGroup[int((pixel * len(asciiGroup)//256))]
#         printed = printed + asciiGroup[int(len(asciiGroup) - (pixel * len(asciiGroup))//256 - 1)]
      printed = printed + '\n'
   print(printed)



#pic = get_agray('smiley')

if(__name__ == '__main__'):
   start = time.clock()
   pic = scale('Georgy')
   printAscii(pic)
   end = time.clock()
   print(end - start)


'''
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
'''
