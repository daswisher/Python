import math

class vector(object):
	
	def  __init__(self, list1, list2):
		# the first parameter gives the difference between points
		self.difference=(list2[0]-list1[0], list2[1]-list1[1])
		print (self.difference)
	
	def distance(self):
		self.a=self.difference[0]
		self.b=self.difference[1]
		return math.sqrt(self.a**2 + self.b**2)
x=(20.0, 25.0)
y=(40.0, 55.0)
thing=vector(x,y)
print (thing.distance())
