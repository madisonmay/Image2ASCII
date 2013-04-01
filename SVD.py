from PIL import Image
import numpy as np
import numpy.linalg as la
import scipy.misc

pic = "circle_test.jpg"
im = Image.open("photos/" + pic)
im = im.convert('L')
w, h = im.size
m = np.matrix(list(im.getdata()))
m = np.reshape(m, (h, w))
[u, s, v] = la.svd(m)
c = np.zeros((h, w))

k = w
for j in range(k):
    add = s[j]*u[:,j]*v[:,j].transpose()
    c += add

scipy.misc.imsave('outfile.jpg', c)
