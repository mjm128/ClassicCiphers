class Vigenre():
	
	def __init__(self):
		self.key = None
		
	def setKey(self, key):
		if len(key) == 0:
			print("\nError: Key cannot be empty")
			return False
		for c in key:
			if not c.isalpha():
				print("\nError: Key must contain only characters a-z or A-Z")
				return False
		self.key = key
		return True
		
	def encrypt(self, plainText):
		return self.crypt(plainText, True)
		
	def decrypt(self, cipherText):
		return self.crypt(cipherText, False)

	def crypt(self, text, isEncrypt):
		newText = ""
		keyCounter = 0
		for c in text:
			if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
				newText += self.shiftLetter(c, self.key[keyCounter % len(self.key)], isEncrypt)
				keyCounter += 1
			else:
				newText += c
				
		return newText
		
	def shiftLetter(self, c, shift, direction):
		if direction:#enc/dec flag
			mult = 1
		else:
			mult = -1
		shift = ord(shift.lower()) - ord('a')
		if c >= 'a' and c <= 'z':
			x = (((ord(c) - ord('a')) + mult*shift) % 26) + ord('a')

		elif c >= 'A' and c <= 'Z':
			x = (((ord(c) - ord('A')) + mult*shift) % 26) + ord('A')

		return chr(x)
