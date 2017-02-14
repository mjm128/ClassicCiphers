import numbers
from CipherInterface import CipherInterface

class Caesar(CipherInterface):
	
	def __init__(self):
		self.key = None
		
	def setKey(self, key):
		try:
			#If key is an int
			self.key = int(key)
			return True
		except:
			try:
				#If key is a character
				self.key = ord(key)
				return True
			except:
				print("Invalid Key: " + key)
		
		return False
		
	def encrypt(self, plainText):
		cypherText = ""
		for char in plainText:
			if char.isalpha():
				s = ord('a' if char.islower() else 'A')
				c = chr((ord(char) - s + self.key) % 26 + s)
				cypherText += c
			else:
				cypherText += char
				
		return cypherText
		
	def decrypt(self, cipherText):
		plainText = ""
		for char in cipherText:
			if char.isalpha():
				s = ord('a' if char.islower() else 'A')
				c = chr((ord(char) - s - self.key) % 26 + s)
				plainText += c
			else:
				plainText += char
		
		return plainText