import time

# Used for timing 
class Stopwatch:
	def __init__(self, startTime=time.time()):
		self.currTime = startTime

	# Ticks the stopwatch, returns seconds passed since last tick
	def tick(self):
		temp = self.currTime
		self.currTime = time.time()
		return self.currTime - temp

def strGMTtoStruct(str):
	return time.strptime(str, "%Y-%m-%dT%H:%M:%SZ")

def hoursUntil(_time):
	currTime = time.localtime()
	return (time.mktime(_time) - time.mktime(currTime)) / 3600