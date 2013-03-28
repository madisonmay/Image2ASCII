from scipy import ndimage
import matplotlib.pyplot as plt 
import numpy as np
from scipy import misc
from pylab import *
from random import randint

#Opening and formating image
cRatio = 6
img = misc.imread('rainbow.jpg')
height,width = img.shape[0],img.shape[1]
print width,height
pixels = width*height
imgFlat = np.reshape(img,(-1,3))
imgFlat = np.floor((imgFlat/cRatio)*cRatio)

#Generating colors and positions dictionary
cDict = {}
for i in xrange(pixels):
	pixel = imgFlat[i][0],imgFlat[i][1],imgFlat[i][2]
	x = i%width
	y = i/width
	if pixel in cDict:
		cDict[pixel][0] += 1
		cDict[pixel][1] += x
		cDict[pixel][2] += y
	else:
		cDict[pixel] = [1,x,y]

#Normalizing x and y by color frequency
for key in cDict:
	cDict[key][1] = cDict[key][1]/cDict[key][0]
	cDict[key][2] = cDict[key][2]/cDict[key][0]

#Intializing figure so no frame/axes is drawn
fig = plt.figure(frameon=False)
fig.set_size_inches(width/300,height/300)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

#Reorganizing data for plotting
cData = []
for key in cDict:
	cData.append([cDict[key][0],cDict[key][1],height-cDict[key][2],[key[0]/255,key[1]/255,key[2]/255]])
cData = sorted(cData, reverse=True, key=lambda cData: cData[0]) #Sort by color frequency
x,y,scale,color = [],[],[],[]
for i in xrange(len(cData)):
	# x.append(cData[i][1]+randint(-25,25))
	# y.append(cData[i][2]+randint(-25,25))
	# if cData[i][0] < 25:
	# 	scale.append(cData[i][0]+randint(-cData[i][0]+1,25))
	# else:
	# 	scale.append(cData[i][0]+randint(-25,25))
	x.append(cData[i][1])
	y.append(cData[i][2])
	scale.append(cData[i][0])
	color.append(cData[i][3])

#Plotting
print "Plotting",len(cDict),"colors"
# plt.scatter(x,y,s=scale,c=color)
c = plt.scatter(x,y,s=scale,c=color,edgecolors="none")
show()
# c.set_alpha(0.25)
# savefig("timeIt.pdf",transparent=True)