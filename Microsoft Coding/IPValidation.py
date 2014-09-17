def validation(firstIP, secondIP, thirdIP):
	num = 0
	withinRange = "InRange"
	first = firstIP.split(".")
	second = secondIP.split(".")
	third = thirdIP.split(".")
	if len(third)!=4:
		withinRange="InValid"
	else:
		while num < 4:
			if not (int(first[num])<=int(third[num])<int(second[num])) or not int((second[num])<=int(third[num])<int(first[num])):
				withinRange="OutRange"
			elif third[num]=="" or third[num]=="." or int(third[num]) > 255:
				withinRange="InValid"
			num=num+1
	print(withinRange)
'''
def main():
	print("THIS IS FUCKING AWESOME")
'''

#print("This is fucking AWESOME!!!")		
#validation("110.0.0.1", "11.199.88.254", "10.107.18.143")

fo = open("PracticeInput.txt","r")
print("Opening file")
count=0
#fo.readline()
for line in fo:
	count=count+1
	line = line.rstrip('\n')
	line = line.rstrip('\t')	
	line = line.rstrip('\r')
	values = line.split(" ")

#	print(values)
	validation(values[0], values[1], values[2])
#	print(count)
fo.close()


