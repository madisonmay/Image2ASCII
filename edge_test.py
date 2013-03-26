from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filter

name = raw_input("Name of Picture: ")

im = ndimage.imread(name, True)

while(True):
	temp = raw_input("Sigma Value?: ")
	sig = int(temp)
	edges2 = filter.canny(im, sigma = sig)


	plt.figure(figsize = (8,8))

	plt.imshow(edges2, cmap=plt.cm.gray)
	plt.axis('off')
	plt.title('Canny filter, $\sigma=$' + str(sig), fontsize=20)

	plt.show()
