#1-6572
from PIL import Image
from edge_ascii import ascii_to_file
from os import listdir
from os.path import isfile, join
input_dir = './test/'
output_dir = './result/'
last_file = ''
files = sorted([ f for f in listdir(input_dir) if isfile(join(input_dir,f)) and f > last_file])
for f in files:
    image = Image.open(input_dir + f)
    name,_ = f.split('.')
    print name+".txt"
    ascii_to_file(image, output_dir + name+".txt")
