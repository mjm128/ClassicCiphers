from Playfair import Playfair
from Hill import Hill
from Caesar import Caesar
from Railfence import Railfence
from RowTransposition import RowTransposition
from Vigenre import Vigenre


class CipherInterface(Playfair, Hill, Caesar, Railfence, RowTransposition, Vigenre):
	
	def __init__(self):
		super(Hill, self).__init__()
	
	def setKey(self, key):
		return False;
		
	def encrypt(self, plainText):
		pass
		
	def decyprt(self, cipherText):
		pass