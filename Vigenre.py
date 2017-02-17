from CipherInterface import CipherInterface

class Vigenre(CipherInterface):
	
	def __init__(self):
		self.key = None
		
	def setKey(self, key):
		for c in key:
			if not c.isalpha():
				return False
		self.key = key
		return True
		
	def encrypt(self, plainText):
		keyCounter = 0
		cipherText = ""
		for c in plainText:
			if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
				cipherText += shiftLetter(c, self.key[keyCounter % len(self.key)], True)
				keyCounter += 1
			else:
				cipherText += c
			
		return cipherText
		
	def decrypt(self, cipherText):
		keyCounter = 0
		plainText = ""
		for c in cipherText:
			if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
				plainText += shiftLetter(c, self.key[keyCounter % len(self.key)], False)
				keyCounter += 1
			else:
				plainText += c
		
		return plainText
		
def shiftLetter(c, shift, direction):
	if direction:#If it's decreption of not
		mult = 1
	else:
		mult = -1
	shift = ord(shift.lower()) - ord('a')
	if c >= 'a' and c <= 'z':
		x = (((ord(c) - ord('a')) + mult*shift) % 26) + ord('a')

	elif c >= 'A' and c <= 'Z':
		x = (((ord(c) - ord('A')) + mult*shift) % 26) + ord('A')

	return chr(x)