#Batch processing to convert edge-detected images to ascii text

from PIL import Image
from edge_ascii import ascii_to_file
import edge_ascii
from os import listdir
from os.path import isfile, join
from ticktock import *
import cProfile
import charfreq

def begin():
    #reset time
	tick()

    #where source images are stored
    input_dir = './test/'

    #where resultant images will be stored
    output_dir = './result/'

    #Used if images are processed in chunks
    last_file = ''

    #Grab a list of the files in the input directory and sort them
    #Exclude files that have already been processed (as defined by last_file)
	edge_ascii.set_occurence(charfreq.get_most_frequent(input_dir))
	files = sorted([ f for f in listdir(input_dir) if isfile(join(input_dir,f)) and f > last_file])
	for f in files:
	    image = Image.open(input_dir + f)
	    print f
	    name,_ = f.split('.')

        #the real work happens here
	    ascii_to_file(image, output_dir + name+".txt")
	    print name+".txt"

        #output time
	    tock()

if(__name__ == "__main__"):
	cProfile.run("begin()")
