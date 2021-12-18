# A python tic tac toe
# by Tan Shi Sian


import random as rand



class TTT:


	def __init__(self, name, xo, board, pcxo, count):
		self.name = name
		self.xo = xo
		self.board = board
		self.pcxo = pcxo
		self.count = count
	

	def sayHi(self):
		print("Hi",self.name,".You choose ",self.xo,".\n\n")
		return
		

	def gameStart(self):
		print("The game start now !!!\n\n")	
		return


	def guidelines(self):
		print("Guideline : ")
		print(" ____________\n")
		print("|", 0, "|", 1, "|", 2, "|",)
		print("|", 3, "|", 4, "|", 5, "|",)
		print("|", 6, "|", 7, "|", 8, "|",)
		print(" ____________\n")

		print("Guideline : ")
		print(" ____________\n")
		print("|", 1, "|", 2, "|", 3, "|",)
		print("|", 4, "|", 5, "|", 6, "|",)
		print("|", 7, "|", 8, "|", 9, "|",)
		print(" ____________\n")

		print("Enter 1 - 9 to choose the place.\n\n")
		return


	def printBoard(self):
		#self.board[0].append(1)

		# 0 1 2
		# 3 4 5
		# 6 7 8
		#self.board[0] = 'x'
		#self.board[1] = 'o'

		print(" ____________\n")
		print("|", self.board[0], "|", self.board[1], "|", self.board[2], "|",)
		print("|", self.board[3], "|", self.board[4], "|", self.board[5], "|",)
		print("|", self.board[6], "|", self.board[7], "|", self.board[8], "|",)
		print(" ____________\n\n")
		return


	def choosePlace(self):
		num = int(input("Choose a slot (1-9) : "))
		self.board[num-1] = self.xo
		self.count = self.count + 1
		print("You have choosen :",num)
		self.checkWinLose()
		return


	def PC(self):
		num = rand.randint(0,8)

		while(self.board[num] == self.xo or self.board[num] == self.pcxo):
			num = rand.randint(0,8)
		
		self.board[num] = self.pcxo
		self.count = self.count + 1
		print("PC have choosen :",num+1)
		self.checkWinLose()
		return

		
	#useless now	
	def check(self,num):
		if (self.board[num] != self.xo):
			self.board[num] = self.pcxo
		else:
			num = int(input("Choose a slot (0-8) : "))
			self.check(num)


	#useless now	
	def full(self):
		if (self.count == 9):
			print("The board is full !!!")
			return
		else:
			print("Not full yet")
			return
		

	def issame(self, a, b, c):
		if (a == b == c):
			return True
		else:
			return False

	
	def whowin(self, x):
		if (x == self.xo):
			print("Player win !!!")
		else:
			print("PC win !!!")
		


	def checkWinLose(self):
		#heng
		if(self.issame(self.board[0], self.board[1], self.board[2])):
			self.whowin(self.board[0])
			self.count = 99
			return
		elif(self.issame(self.board[3], self.board[4], self.board[5])):
			self.whowin(self.board[3])
			self.count = 99
			return
		elif(self.issame(self.board[6], self.board[7], self.board[8])):
			self.whowin(self.board[6])
			self.count = 99
			return

		#shu
		elif(self.issame(self.board[0], self.board[3], self.board[6])):
			self.whowin(self.board[0])
			self.count = 99
			return
		elif(self.issame(self.board[1], self.board[4], self.board[7])):
			self.whowin(self.board[1])
			self.count = 99
			return
		elif(self.issame(self.board[2], self.board[5], self.board[8])):
			self.whowin(self.board[2])
			self.count = 99
			return

		#xie
		elif(self.issame(self.board[0], self.board[4], self.board[8])):
			self.whowin(self.board[0])
			self.count = 99
			return
		elif(self.issame(self.board[2], self.board[4], self.board[6])):
			self.whowin(self.board[2])
			self.count = 99
			return
			
		


		
			
#board = ["*","*","*","*","*","*","*","*","*"]
#choices = [0,1,2,3,4,5,6,7,8]


# Initialize board and count
board = ["1","2","3","4","5","6","7","8","9"]
count = 0


# Welcome
print("\n\nWelcome to my tic tac toe game!!!")
name = input("What is your name ---> ")
xo = input("x or o  ---> ")
print("\n\n")


# Choose marker for pc player
# pcxo is marker of pc player
if (xo == 'x'):
	pcxo = 'o'
else:
	pcxo = 'x'


# Instantiate a game
a = TTT(name, xo, board, pcxo, count)


# useless
#a.sayHi()
#a.guidelines()
#a.gameStart()

a.printBoard()
while(a.count <= 9):
	print("Your turn : ")
	a.choosePlace()
	a.printBoard()

	print("PC turn : ")
	a.PC()
	a.printBoard()




a.printBoard()

print("\n\nGame Over.")










