#1-6572
from PIL import Image
from edge_ascii import ascii_to_file
import edge_ascii
from os import listdir
from os.path import isfile, join
from ticktock import *
import cProfile
import charfreq

def begin():
	tick()
	input_dir = './poke_in/'
	output_dir = './poke_out/'
	last_file = ''
	edge_ascii.set_occurence(charfreq.get_most_frequent(input_dir))
	files = sorted([ f for f in listdir(input_dir) if isfile(join(input_dir,f)) and f > last_file])
	for f in files:
	    image = Image.open(input_dir + f)
	    print f
	    name,_ = f.split('.')
	    ascii_to_file(image, output_dir + name+".txt")
	    print name+".txt"
	    tock()

if(__name__ == "__main__"):
	cProfile.run("begin()")