class Playfair():
	
	def __init__(self):
		self.key = []
		self.matrix = []
		self.ALPHABET = "abcdefghijklmnopqrstuvwxyz"
		self.IorJ = 'i' #Used to set use of I/J in program
		
	def setKey(self, key):
		key = key.lower() #convert key to lower case
		m = []
		if len(key) > 0:
			for character in key:
				if not character.isalpha():
					print("Error: Key must contain only characters")
					return False
				if character == 'i' or character == 'j':
					#Representing i and j as just i
					if self.IorJ not in self.key:
						self.key.append(self.IorJ)
				elif character not in self.key:
					self.key.append(character)	
			
			#Create the matrix from the distinct elements in the self.key list
			for i in self.key:
				m.append(i)
				
			for character in self.ALPHABET:
				if character == 'i' or character == 'j':
					if self.IorJ not in m: #using i only to represent i/j
						m.append(self.IorJ)
				elif character not in m:
					m.append(character)
			
			#Create the final matrix
			self.matrix.append(m[0:5]) 
			self.matrix.append(m[5:10]) 
			self.matrix.append(m[10:15])
			self.matrix.append(m[15:20])
			self.matrix.append(m[20:25])		
			return True
				
		print("Error: Key must be at least one character")
		return False
		
	def encrypt(self, plainText):
		cipherText = ""
		plainText = plainText.lower() #convert to lower case
		text = []
		for c in plainText:
			if c == "i" or c == "j":
				text.append(self.IorJ)
			else:
				text.append(c)
		
		i = 0
		while i < len(text)-1:#keeps checking len of text in case insertion happens
			if text[i] == text[i+1]:
				#insert 'x' between duplicate characters
				text.insert(i+1, 'x')
			i+=2
						
		if len(text)% 2 == 1:
			#append 'x' at end for padding
			text.append('x')
			
		#pass through 2 characters at a time
		for i in range(0, len(text), 2):
			cipherText += self.cipherRules(text[i], text[i+1], True)
			
		for row in self.matrix:
			print(row)
			
		return cipherText
		
	def decrypt(self, cipherText):
		plainText = ""
		cipherText = cipherText.lower()
		text = []
		
		for c in cipherText:
			if c == "i" or c == "j":
				text.append(self.IorJ)
			else:
				text.append(c)
				
		if len(text)% 2 == 1:
			#append 'x' at end for padding
			text.append('x')
		
		#pass through 2 characters at a time
		for i in range(0, len(text), 2):
			plainText += self.cipherRules(text[i], text[i+1], False)
		
		return plainText

	def cipherRules(self, c1, c2, isEncrypt):
		#first/second[Row=1, Column=0]
		first = self.getIndex(c1) #index of first 
		second = self.getIndex(c2) #index of second
		
		#Different Column
		if first[0] != second[0]:
			#Different Row
			if first[1] != second[1]:
				#Rule 1: Different Column & Row
				#[Row][Column] first/second[Row=1, Column=0]
				x1 = self.matrix[first[1]][second[0]]
				x2 = self.matrix[second[1]][first[0]]
				pair = str(x1)+str(x2)
			else:
				#Rule 2: Same Row
				if isEncrypt:
					#[Row][Column] first/second[Row=1, Column=0]
					x1 = self.matrix[first[1]][(first[0]+1)%5]
					x2 = self.matrix[second[1]][(second[0]+1)%5]
					pair = x1+x2
				else:
					x1 = self.matrix[first[1]][(first[0]-1)%5]
					x2 = self.matrix[second[1]][(second[0]-1)%5]
					pair = x1+x2
		#Same Column
		else:
			#Rule 3: Same Column
			if isEncrypt:
				#[Row][Column] first/second[Row=1, Column=0]
				x1 = self.matrix[(first[1]+1)%5][first[0]]
				x2 = self.matrix[(second[1]+1)%5][second[0]]
				pair = x1+x2
			else:
				x1 = self.matrix[(first[1]-1)%5][first[0]]
				x2 = self.matrix[(second[1]-1)%5][second[0]]
				pair = x1+x2
		
		return pair
	
		
	def getIndex(self, character):
		for y in range(5):
			for x in range(5):
				if self.matrix[y][x] == character:
					return (x,y)
