import math

class Row:

	def __init__(self):
		self.key = None
		self.matrix = None

	def setKey(self, key):
		error = ""
		if len(key) > 0:
			l = []
			for index, element in enumerate(key):
				l.append((element, index))
				if not element.isalpha():
					error = "Key must be only alphabetical characters"
			if error == "":
				l.sort(key=lambda tup: tup[0])
				self.key = [None] * len(key)
				for index, pair in enumerate(l):
					self.key[pair[1]] = index
				return True
			try:
				l = []
				for index, element in enumerate(key):
					l.append((int(element), index))
				l.sort(key=lambda tup: tup[0])
				self.key = [None] * len(key)
				for index, pair in enumerate(l):
					self.key[pair[1]] = index
				return True
			except:
				error = "Key must contain only integers"
		else:
			error = "Must enter a key"
		print(error)
		return False

	def encrypt(self, plainText):
		cipherText = ''
		self.setMatrix(plainText)
		
		print(matrix)
		for element in self.key:
			cipherText += matrix[element]

		return cipherText
		
	def decrypt(self, cipherText):
		plainText = ""
		self.matrix = [''] * len(self.key)
		cardText = len(cipherText)
		cardKey = len(self.key)
		
		counter = 0
		for element in self.key:
			for c in range(counter, 1+counter+(cardText/cardKey)):
				self.matrix[element] += cipherText[c]
			counter = counter+(cardText/cardKey)
			if cardText % cardKey > element:
				#If this column contains an "extra" character
				self.matrix[element] += cipherText[c]
				counter += 1
					
		for x in range(0, cardText):
			plainText += self.matrix[x % cardKey][x / cardKey]
		return (plainText)
		
	def setMatrix(self, text):
		self.matrix = [''] * len(self.key)
		for columns in range(len(text)):
			self.matrix[columns % len(self.key)] += plainText[columns]
