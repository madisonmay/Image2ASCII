from __future__ import print_function
from math import log
from math import atan2 as atan
from math import pi
from math import hypot
from math import acos
from math import exp
import edge_test as edge
import main
import numpy
from ticktock import *
from PIL import Image


import pylab



def begin():
	name = "photos/" + raw_input("Name of Image: ")
	tick()
	e = edge.get_edge(name)
	new_pic = main.scale_pic(e)
	main.printAscii(new_pic)
	tock()

def angle(a, b):
	v = [b[0] - a[0], b[1] - a[1]]
	return atan(v[1], v[0])

def log_d(a, b):
	return log(hypot(a[0] - b[0], a[1] - b[1]))

def section_shape_graph(im_sec):
	l = len(im_sec)
	w = len(im_sec[0])
	c = [(w-1)/2.0, (l-1)/2.0]
	print(c)
	points = []
	for y in range(l): #Goes by rows
		for x in range(w): #Then by columns
			if(im_sec[y][x] == 0): #If the color is black...?
				p = [x, y]
				points.append([angle(c, p), log_d(c, p)])
	return points

def nine_by_ten(pic):
	im = Image.open("photos/" + pic)
	im.draft("L", im.size)
	piece = []
	for i in range(30):
		piece.append([])
		for j in range(30):
			piece[i].append(im.getpixel((i,j)))
	height = len(piece)
	width = len(piece[0])
	x_por = width / 12.0
	y_por = height / 12.0

	density = []

	for y in range(10):
		density.append([])
		for x in range (9):
			total = 0
			number = 0
			for i in range(int(x * x_por), int((x+1) * x_por)):
				for j in range(int(y * y_por), int((y+1) * y_por)):
					total = total + piece[j][i]
					number = number + 1
			val = total / float(number) / 255.0

			if(total / number < 128):
				density[y].append("#")
			else:
				density[y].append(" ")
	for i in range(len(density)):
		print(density[i])

def plot(points):
	pylab.plot([[0]],[[0]])
	for point in points:
		pylab.scatter([point[0]], [point[1]])
	pylab.show()

def graph_test(s):
	tick()
	im = Image.open("photos/" + s)
	im.draft("L", im.size)
	w = im.size[0]
	h = im.size[1]

	values = []
	for j in range(h):
		values.append([])
		for i in range(w):
			if(im.getpixel((i, j)) > 127):
				values[j].append(255)
			else:
				values[j].append(0)
	all_p = section_shape_graph(values)
	tock()
	print(len(all_p))
	plot(all_p)

def unicode_chars():
	'''Used to generate every single unicode character.  Prints them in groups of 2^13 in order to keep it manageable.'''
	string = ""
	for i in range(2**0, 2**16):
		char = unichr(i)
		string = string + char

	spacing = 2**13
	for i in range(8):
		print(string[i * spacing:(i + 1) * spacing])
		raw_input("")

def compare1(im1, im2):
	im1.draft("L", im1.size)
	im2.draft("L", im2.size)
	size = im1.size

	delta = 0
	for i in range(size[0] * size[1]):
		loc = (i %size[0], i // size[0])
		val1 = im1.getpixel(loc)
		val2 = im2.getpixel(loc)

		gray1 = get_gray_val(val1)
		gray2 = get_gray_val(val2)
		if(gray1 > gray2):
			delta = delta + gray1 - gray2
		else:
			delta = delta + gray2 - gray1
	return delta

def compare(im1, im2):
	im1.draft("L", im1.size)
	im2.draft("L", im2.size)
	size = im1.size

	bright_a = 0 #Overall brightness for im1
	bright_b = 0 #Overall brightness for im2

	delta = 0
	for i in range(size[0]):
		for j in range(size[1]):

			val1 = im1.getpixel((i,j))
			low = 255
			for dx in range(0, 1):
				for dy in range(0, 1):
					if(i + dx > 0 and i + dx < size[0] and j + dy > 0 and j + dy < size[1]):

						val2 = im2.getpixel((i + dx, j + dy))
						a = get_gray_val(val1)
						b = get_gray_val(val2)
						if(dx == 0 and dy == 0):
							bright_a = bright_a + a
							bright_b = bright_b + b
						comp = a - b
						if(comp < 0):
							comp = -50 * comp
						comp = comp + (dx * dx + dy * dy * 0.7) * 100
						if comp < low:
							low = comp
					if(low == 0):
						break
				if(low == 0):
					break
			delta = delta + low
	delta_bright = (bright_a-bright_b)# / (size[0] * size[1])
	if(delta_bright < 0):
		delta_bright = -delta_bright

	delta = delta * 1 + delta_bright * 1
	return delta

def get_gray_val(pixel):
	if type(pixel) is int:
		return pixel
	if type(pixel) is tuple:
		val = pixel[0] * 0.21 + pixel[1] * 0.71 + pixel[2] * 0.07
		if(len(pixel) > 3):
			val = val * pixel[3] / 255
		return val

all_char = []
for i in range(32, 127):
	all_char.append(Image.open("photos/characters/" + str(i) + ".png"))
#for i in range(161, 256):
#	all_char.append(Image.open("photos/characters/" + str(i) + ".png"))

def compare_against_all(image):
	lowest_val = 255 * 9 * 18
	best = 32

	total = 0
	num_pix = 0
	size = image.size
	for i in range(size[0] * size[1]):
		total = total + get_gray_val(image.getpixel((i%size[0],i/size[0])))
		num_pix = num_pix + 1
	if(total / num_pix < 5):
		return 32

	for i in range(len(all_char)):
		c = compare(image, all_char[i])
		if(c < lowest_val):
			lowest_val = c
			if(i < 85):
				best = 32 + i
			else:
#				print(i)
				best = i - 85 + 161
	return best

def get_image_string(image):
	string = ""
	for y in range(0, image.size[1], 18):
		for x in range(0, image.size[0] - 7, 8):
			print((unichr(compare_against_all(image.crop((x, y, x + 8, y + 18))))), end='')
		print()
#	print string

if(__name__ == "__main__"):
	tick()
	image = Image.open("photos/result.jpg")
	get_image_string(image)
	tock()
#	tick()
#	im1 = Image.open("photos/characters/32.png")
#	im2 = Image.open("photos/characters/33.png")
#	print(compare(im2, im1))
#	tock()
	'''
	tick()
	images = []
	base = 75
	num = 20
	for i in range(0, num):
		images.append(Image.open("photos/characters/" + str(base + i) + ".png"))

	best_combo = [0, 0]
	lowest = 2**20
	for i in range(base,base + num):
		for j in range(base, base + num):
			if(i == j):
				continue
			comp = compare(images[i - base], images[j-base])
			if(comp < lowest):
				lowest = comp
				best_combo = [i, j]
	tock()
	print best_combo, lowest
	'''
