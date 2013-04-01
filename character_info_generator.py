from PIL import Image
chars = []

val_list = []

for i in range(32, 127): #Gets all photos
	char = Image.open("photos/characters/" + str(i) + ".png")
	size = char.size
	chars.append(char)
	char_vals = char.getdata()
	vals = []
	for j in range(len(char_vals)):
		vals.append(char_vals[j][0])
	val_list.append(vals)
	print(len(char_vals))

#print(val_list)