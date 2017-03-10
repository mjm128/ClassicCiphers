class Railfence():
	
	def __init__(self):
		self.key = None
		
	def setKey(self, key):
		try:
			self.key = int(key)
			if self.key > 0:
				return True
		except:
			print("\nError: Key must be an integer")
			return False
		print("\nError: Key must be larger than 0")
		return False
		
	def encrypt(self, plainText):
		cipherText = ""
		rowLength = int(len(plainText) / self.key)
		extra = len(plainText) % self.key	
		railfence = [None] * self.key
		for i in range(0, self.key):
			if i < extra:
				railfence[i] = [None] * (rowLength + 1)
			else:
				railfence[i] = [None] * (rowLength)
				
		#Add text column by column until no more characters
		for index, char in enumerate(plainText):
			railfence[index % self.key][int(index / self.key)] = char

		#Get the cipherText by reading rail by rail
		for rail in railfence:
			for element in rail:
				cipherText += element
				
		return cipherText
		
	def decrypt(self, cipherText):
		plainText = ""
		bucket = [None] * len(cipherText)
		rowLength = int(len(cipherText) / self.key)
		extra = len(cipherText) % self.key
		railfence = [None] * self.key
		for i in range(0, self.key):
			if i < extra:
				railfence[i] = [None] * (rowLength + 1)
			else:
				railfence[i] = [None] * (rowLength)
				
		#Add text rail by rail until no more characters
		counter = 0
		for rail in railfence:
			for i in range(0, len(rail)):
				rail[i] = cipherText[counter]
				counter+= 1
		
		#Get plaintext by reading column by column
		for index, char in enumerate(cipherText):
			bucket[index] = railfence[index % self.key][int(index / self.key)]
			
		for i in bucket:
			plainText += i
			
		return plainText
