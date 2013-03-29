from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filter
from ticktock import *


def get_edge(name, sig = 8):
	im = ndimage.imread(name, True)
	edge = filter.canny(im, sigma = sig)
	modded = (255.0 / edge.max() * (edge - edge.min())).astype(np.uint8)
	edged = Image.fromarray(modded)
	edged.save("photos/edge.png")
	return edged

if(__name__ == "__main__"):
	name = raw_input("Name of Picture: ")

	im = ndimage.imread(name, True)

	while(True):
		temp = raw_input("Sigma Value?: ")
		sig = int(temp)
		edges2 = filter.canny(im, sigma = sig)

		print(type(edges2))

		modded = (255.0 / edges2.max() * (edges2 - edges2.min())).astype(np.uint8)
		edged = Image.fromarray(modded)
		edged.save("photos/edge.png")

		plt.figure(figsize = (8,8))

		plt.imshow(edges2, cmap=plt.cm.gray)
		plt.axis('off')
		plt.title('Canny filter, $\sigma=$' + str(sig), fontsize=20)

		plt.show()
