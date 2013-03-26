from skimage import data
from skimage import measure
from scipy import ndimage
import numpy as np
#import matplotlib.pyplot as plt

import pylab
import time

name = raw_input("Name of Picture: ")

im = ndimage.imread(name, True)

height = len(im)

num = 9
multiple = 25

all_cont = []

for i in range(0, num, 1):
	contours = measure.find_contours(im, i * multiple)
	all_cont.append(contours)
	num_cont = 0
	pylab.subplot(300 + 10 * num / 3 + i + 1)
	for n, contour in enumerate(contours):
		pylab.plot(contour[:, 1], height - contour[:, 0], linewidth=2)
	pylab.title("Value of sigma: " + str(i * multiple))
	pylab.draw()
	start = time.time()
	counter = 0
	pylab.draw()
	print(i)

pylab.figure(2)
for i in range(2, len(all_cont)):
	for n, contour in enumerate(all_cont[i]):
		pylab.plot(contour[:, 1], height - contour[:, 0], linewidth=2)

pylab.show()
