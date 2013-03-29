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
	print c
	points = []
	for y in range(l): #Goes by rows
		for x in range(w): #Then by columns
			if(im_sec[y][x] == 0): #If the color is black...?
				p = [x, y]
				points.append([angle(c, p), log_d(c, p)])
	return points

def twelve_by_twelve_density(pic):
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

	for y in range(12):
		density.append([])
		for x in range (12):
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
		print density[i]

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
	print len(all_p)
	plot(all_p)

def unicode_chars():
	'''Used to generate every single unicode character.  Prints them in groups of 2^13 in order to keep it manageable.'''
	string = ""
	for i in range(2**0, 2**16):
		char = unichr(i)
		string = string + char

	spacing = 2**13
	for i in range(8):
		print string[i * spacing:(i + 1) * spacing]
		raw_input("")
tick()
graph_test("circle_test.jpg")
tock()