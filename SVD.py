from PIL import Image
import numpy as np
import numpy.linalg as la

pic = "circle_test.jpg"
im = Image.open("photos/" + pic)
im = im.convert('1')
w, h = im.size
m = np.matrix(list(im.getdata()))
m = np.reshape(m , (w, h))
[u, s, v] = la.svd(m)
C = np.zeros((w, h))
k = 20
for j in range(k):
    add = s[j]*u[:,j]*v[:,j].transpose()
    C += add

for row in C:
    print [int(x) for x in row]

img = Image.fromarray(C, 'L')
img.save('my.jpg')
