#1-6572
from PIL import Image
#from edge_ascii import ascii_to_file
from txt_to_pic import imagify
from os import listdir
from os.path import isfile, join
input_dir = './result'
#output_dir = './result/'
last_file = ''
files = sorted([ f for f in listdir(input_dir) if isfile(join(input_dir,f)) and f > last_file])
for f in files:
	imagify(input_dir + "/" + f)
	name = f.split('.')[1]
#    ascii_to_file(image, output_dir + name+".txt")
	print name+".jpg is completed"
