from PIL import Image, ImageOps, ImageDraw, ImageFont
from os.path import isfile

ub_m = ImageFont.truetype("./fonts/Ubuntu-M.ttf", 12, encoding = 'unic')
FOREGROUND = (255,255,255)

def imagify(filename):
	f = open(filename)
	img = Image.new("L", (107 * 9, 40 * 18), "black")
	draw = ImageDraw.Draw(img)
	y = 1

	for line in f.readlines():
		line = line[0:-1]
		x = 1
		for char in line:
			draw.text((x, y * 18), char, font = ub_m, fill = 255)
			x = x + 9
		y = y + 1

	img.show()
	save = "." + filename.split('.')[1] + ".jpg"
	print save
	img.save(save)

def imagify_all():
	for i in range(1,6573):
		num = str(i)
		zeros = (8 - len(num)) * "0"
		name = "./out/" + zeros + num + ".txt"
		if(isfile(name[0:17] + ".jpg")):
			continue
		imagify(name)

if(__name__ == "__main__"):
	imagify_all()
#	imagify("./result/00000100.txt")
