#Character Picture Generator
import Image

im = Image.open("photos/characters/chars.png")

for l in range(33,128):
	i = l - 33
	box = (i * 9 + 1, 0, (i + 1) * 9 + 1, 18)
	trim_char = im.crop(box)
	trim_char.save("photos/characters/" + str(l-1) + ".png")

for l in range(161,256):
	i = l-161
	box = (i * 9 + 1, 18, (i + 1) * 9 + 1, 36)
	trim_char = im.crop(box)
	trim_char.save("photos/characters/" + str(l) + ".png")