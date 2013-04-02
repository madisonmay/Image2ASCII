from os.path import isfile
import os
import edge_ascii
import Image
directory = "poke_in/"

char_count = [0] * 95
ten_frames = "fr.txt"

def get_name(i):
	n = str(i)
	return directory + (8-len(n)) * "0" + n + ".jpg"

def gen():
	filename = ten_frames
	f = open(filename)
	chars = f.read()
	for c in chars:
		l = ord(c)
		if(l>32 and l < 127):
			char_count[l-33] = char_count[l-33] + 1
	return char_count

def get_most_frequent(path):
	directory = path
	if(isfile(ten_frames)):		#Removes the frames if already occupied
		os.system("rm " + ten_frames)
	num_files = 0
	while(isfile(get_name(num_files + 1))):	#Finds every file and counts them
		num_files = num_files + 1
	print("There are a total of " + str(num_files) + " Frames")
	images = []
	for j in range(1,num_files,num_files//10):
		images.append(Image.open(get_name(j)))
	edge_ascii.multi_file(images,ten_frames)

	occurence = gen()
	original = list(occurence)
	characters = []
	order = []
	occurence.sort()
	occurence.reverse()
	for i in range(len(occurence)):
		order.append(original.index(occurence[i]) + 33)
		characters.append(chr(order[i]))
	characters = [32] + characters[:20]
	return order

#if(__name__ == "__main__"):
#	print begin()
