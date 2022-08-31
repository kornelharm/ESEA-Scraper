import time

# Used for timing 
class stopwatch:
	def __init__(self, startTime=time.time()):
		self.currTime = startTime

	# Ticks the stopwatch, returns seconds passed since last tick
	def tick(self):
		temp = self.currTime
		self.currTime = time.time()
		return self.currTime - temp
