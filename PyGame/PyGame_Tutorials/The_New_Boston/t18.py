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
		
	def add(self, one, two):
		#The sum of the x components and the sum of the y components
		self.vector_sum=(one[0]+two[0], one[1]+two[1])
		return self.vector_sum
		
x=(20.0, 25.0)
y=(40.0, 55.0)
thing=vector(x,y)
vector1=(20,20)
vector2=(-10,10)
print ("The sum of the two vectors is", thing.add(vector1, vector2))

