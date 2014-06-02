a1=a2=a3=b1=b2=b3=c1=c2=c3= " "
'''
while a1==" " or a2==" " or a3==" " or b1 ==" " or b2==" " or b3==' ' or c1==' ' or c2==' ' or c3==' ':
'''
game='incomplete'
def game_state(a1,a2,a3,b1,b2,b3,c1,c2,c3):
	if a1 == a2 == a3 and a1 == 'x':
		game='win'
	elif 'b1'=='b2'=='b3' and 'b1' == 'x':
		game='win'
	elif 'c1'=='c2'=='c3' and 'c1' == 'x':
		game='win'
	elif 'a1'=='b1'=='c1' and 'a1' == 'x':
		game='win'
	elif 'a2'=='b2'=='c2' and 'a2' == 'x':
		game='win'
	elif 'a3'=='b3'=='c3' and 'a3' == 'x':
		game='win'
	elif 'a1'=='b2'=='c3' and 'a1' == 'x':
		game='win'
	elif 'a3'=='b2'=='c1' and 'a3' == 'x':
		game='win'
	else:
		game='incomplete'
	return game
#while z=='incomplete':
#while game=='incomplete':
while game != 'win':
	user1=input("Player 1, which spot would you like? ")
	if user1 == 'a1':
		a1='x'
	elif user1 == 'a2':
		a2='x'
	elif user1 == 'a3':
		a3='x'
	elif user1 == 'b1':
		b1='x'
	elif user1 == 'b2':
		b2='x'
	elif user1 == 'b3':
		b3='x'
	elif user1 == 'c1':
		c1='x'
	elif user1 == 'c2':
		c2='x'
	elif user1 == 'c3':
		c3='x'
	else:
		print("That was not a valid input; You lose a turn!")
	'''
	while user1 != a1 or 'a2' or 'a3' or 'b1' or 'b2' or 'b3' or 'c1' or 'c2' or 'c3':
		print("That's not a valid coordinate!")
		user1=input("Player 1, which spot would you like? ")
	'''
	user2=input("Player 2, which spot would you like? ")
	if user2 == 'a1':
		a1='o'
	elif user2 == 'a2':
		a2='o'
	elif user2 == 'a3':
		a3='o'
	elif user2 == 'b1':
		b1='o'
	elif user2 == 'b2':
		b2='o'
	elif user2 == 'b3':
		b3='o'
	elif user2 == 'c1':
		c1='o'
	elif user2 == 'c2':
		c2='o'
	elif user2 == 'c3':
		c3='o'
	else:
		print("That was not a valid input; You lose a turn!")
	def game_state(a1,a2,a3,b1,b2,b3,c1,c2,c3):
		if a1 == a2 == a3 and a1 == 'x':
			game='win'
		elif 'b1'=='b2'=='b3' and 'b1' == 'x':
			game='win'
		elif 'c1'=='c2'=='c3' and 'c1' == 'x':
			game='win'
		elif 'a1'=='b1'=='c1' and 'a1' == 'x':
			game='win'
		elif 'a2'=='b2'=='c2' and 'a2' == 'x':
			game='win'
		elif 'a3'=='b3'=='c3' and 'a3' == 'x':
			game='win'
		elif 'a1'=='b2'=='c3' and 'a1' == 'x':
			game='win'
		elif 'a3'=='b2'=='c1' and 'a3' == 'x':
			game='win'
		else:
			game='incomplete'
		return game
	game_status = game_state(a1,a2,a3,b1,b2,b3,c1,c2,c3)
	print(game_status)

	'''
	while user2 != 'a1' or 'a2' or 'a3' or 'b1' or 'b2' or 'b3' or 'c1' or 'c2' or 'c3':
		print("That's not a valid coordinate!")
		user2=input("Player 2, which spot would you like? ")
	'''
	def row1(a1, a2, a3):
		line1=str(" "+a1 + " | " + a2 + " | " + a3+ " ")
		return line1
	def row2(b1, b2, b3):
		line2=str(" "+b1 + " | " + b2 + " | " + b3+" ")
		return line2
	def row3(c1, c2, c3):
		line3=str(" "+c1 + " | " + c2 + " | " + c3+ " ")
		return line3
	def grid():
		a = row1(a1, a2, a3)
		b = row2(b1, b2, b3)
		c = row3(c1, c2, c3)
		print(a)
		print("-----------")
		print(b)
		print("-----------")
		print(c)
	grid()
