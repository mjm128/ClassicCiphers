from CipherInterface import CipherInterface

class Playfair(CipherInterface):
	
	def __init__(self):
		self.key = []
		self.matrix = []
		self.ALPHABET = "abcdefghijklmnopqrstuvwxyz"
		
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
					if 'i' not in self.key:
						self.key.append('i')
				elif character not in self.key:
					self.key.append(character)	
			
			m = []
			#Create the matrix from the distinct elements in the self.key list
			for i in self.key:
				m.append(i)
				
			for character in self.ALPHABET:
				if character == 'i' or character == 'j':
					if 'i' not in m: #using i only to represent i/j
						m.append('i')
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
		
		
				
			
		
		
		return cipherText
		
	def decrypt(self, cipherText):
		plainText = ""
		cipherText = cipherText.lower()
		
		return plainText
		
	def getIndex(self, character):
		for i in range(5):
			for j in range(5):
				if self.matrix[i][j] == character:
					return (i, j)