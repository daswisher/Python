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
	#this gives the percentage of change in x and y
	def unit_vector(self):
		distance=self.distance()
		self.a_unit=self.a/distance
		self.b_unit=self.b/distance
		return self.a_unit, self.b_unit
		
x=(20.0, 25.0)
y=(40.0, 55.0)
thing=vector(x,y)
print (thing.distance())
#prints the x and y unit vectors if they were out of 1 unit
print (thing.unit_vector())
