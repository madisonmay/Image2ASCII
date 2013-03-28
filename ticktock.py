import time
TIME_BEGIN = time.time()

def tick():
	global TIME_BEGIN
	TIME_BEGIN = time.time()

def tock():
	print time.time()-TIME_BEGIN

def ticktock(fun):
	tick()
	fun
	tock()