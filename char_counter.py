in_dir = "./frames/Text_Frames/"

char_count = [0] * (126-32) #95 letters

def gen_list():
	for i in range(1,6572):
		n = str(i)
		zeros = (8-len(n)) * "0"
		name = in_dir + zeros + n + ".txt"

		f = open(name)
		chars = f.read()
		for c in chars:
			l = ord(c)
			if(l > 32 and l < 127):
	#			if(l == 34):
	#				print l, unichr(l)
				char_count[l - 33] = char_count[l-33] + 1 

	print char_count

def gen():
	filename = "movie_summary.txt"
	f = open(filename)
	chars = f.read()
	for c in chars:
		l = ord(c)
		if(l>32 and l < 127):
			char_count[l-33] = char_count[l-33] + 1
	return char_count



#occurences = [2752, 169985, 2270, 1283, 1957, 1889, 46903, 13180, 20501, 25992, 21039, 111538, 71911, 38426, 21018, 355, 4892, 1298, 1719, 3475, 1490, 711, 5120, 717, 1057, 32724, 33718, 30704, 67486, 30027, 7482, 1446, 2446, 738, 4623, 465, 2075, 12938, 1207, 1360, 1834, 10981, 1161, 43434, 1148, 589, 720, 7413, 2162, 691, 1313, 3530, 1054, 2799, 1501, 2558, 4907, 4964, 16970, 25153, 8518, 78178, 206387, 72310, 1312, 868, 7180, 1057, 1245, 7391, 2068, 1335, 3700, 9746, 2175, 6154, 1490, 2039, 1140, 1263, 1088, 16227, 2009, 2279, 1797, 7819, 1899, 4547, 4050, 4808, 5627, 19107, 7210, 61870]
occurences = gen()
original = list(occurences)

occurences.sort()
occurences.reverse()
order = []
characters = []
print occurences

for i in range(len(occurences)):
	order.append(original.index(occurences[i]) + 33)
	characters.append(chr(order[i]))

print order
print characters

print len(order)

ratios = [0] * len(occurences)

for i in range(len(occurences)):
	ratios[i] = occurences[i] / float(occurences[-1])

total = sum(occurences)
portion = sum(occurences[:20]) / float(total)
print portion
'''
[206387, 169985, 111538, 78178, 72310, 71911, 67486, 61870, 46903, 43434, 38426, 33718, 32724, 30704, 30027, 25992, 25153, 21039, 21018, 20501, 19107, 16970, 16227, 13180, 12938, 10981, 9746, 8518, 7819, 7482, 7413, 7391, 7210, 7180, 6154, 5627, 5120, 4964, 4907, 4892, 4808, 4623, 4547, 4050, 3700, 3530, 3475, 2799, 2752, 2558, 2446, 2279, 2270, 2175, 2162, 2075, 2068, 2039, 2009, 1957, 1899, 1889, 1834, 1797, 1719, 1501, 1490, 1490, 1446, 1360, 1335, 1313, 1312, 1298, 1283, 1263, 1245, 1207, 1161, 1148, 1140, 1088, 1057, 1057, 1054, 868, 738, 720, 717, 711, 691, 589, 465, 355]
[95, 34, 44, 94, 96, 45, 61, 126, 39, 76, 46, 59, 58, 60, 62, 42, 92, 43, 47, 41, 124, 91, 114, 40, 70, 74, 106, 93, 118, 63, 80, 102, 125, 99, 108, 123, 55, 90, 89, 49, 122, 67, 120, 121, 105, 84, 52, 86, 33, 88, 65, 116, 35, 107, 81, 69, 103, 110, 115, 37, 119, 38, 73, 117, 51, 87, 53, 53, 64, 72, 104, 83, 97, 50, 36, 112, 101, 71, 75, 77, 111, 113, 57, 57, 85, 98, 66, 79, 56, 54, 82, 78, 68, 48]
['_', '"', ',', '^', '`', '-', '=', '~', "'", 'L', '.', ';', ':', '<', '>', '*', '\\', '+', '/', ')', '|', '[', 'r', '(', 'F', 'J', 'j', ']', 'v', '?', 'P', 'f', '}', 'c', 'l', '{', '7', 'Z', 'Y', '1', 'z', 'C', 'x', 'y', 'i', 'T', '4', 'V', '!', 'X', 'A', 't', '#', 'k', 'Q', 'E', 'g', 'n', 's', '%', 'w', '&', 'I', 'u', '3', 'W', '5', '5', '@', 'H', 'h', 'S', 'a', '2', '$', 'p', 'e', 'G', 'K', 'M', 'o', 'q', '9', '9', 'U', 'b', 'B', 'O', '8', '6', 'R', 'N', 'D', '0']

'''