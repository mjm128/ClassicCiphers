from CipherInterface import CipherInterface

class Hill(CipherInterface):
	
	def __init__(self):
		self.key = ""
		
	def setKey(self, key):
		self.key = key
		
	def encrypt(self, plainText):
		
		return self.ciphertext
		
	def decrypt(self, cipherText):
		
		return self.plaintext