import os
import time

directory = "out/"
FPS 	= 30
start 	= 1
end 	= 6572

wait_time = 1.0 / FPS
lasttime = time.time()
timer = 0
for i in range (start, end + 1, 1):
	n = str(i)
	f = open(directory + ((8-len(n)) * "0" + n + ".txt"))
	os.system("clear")
	print f.read()
	print i
	while(time.time() < lasttime + wait_time):
		timer = timer + 1
	lasttime = time.time()