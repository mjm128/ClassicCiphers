
class CipherInterface:
	
	def setKey(self, key):
		raise NotImplementedError()
		
	def encrypt(self, plainText):
		raise NotImplementedError()
		
	def decyprt(self, cipherText):
		raise NotImplementedError()