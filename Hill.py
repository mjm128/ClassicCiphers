import sys
try:
	from numpy import linalg, matrix
	import numpy as np
except ImportError as error:
	print("\nImport Error: Please install numpy")
	if sys.version[0] == '2':
		version = ""
	if sys.version[0] == '3':
		version = "3"
	print("Example: sudo pip"+version+ " install numpy")
	quit()
from math import sqrt

class Hill():
	
	def __init__(self):
		self.key = None

	def setKey(self, key):

		stringIntro = "\nThe Hill Cipher is a polygraphic substitution cipher based on linear algebra. This cipher was invented by Lester S. Hill in 1929." \
					  "\nThe cipher uses an n*n invertible matrix as the key, which cannot be divisible by any factors of the total length of the alphabet scheme used." \
					  "\nWe will be using the english alphabet as the scheme (which is 26). This means that the determinant cannot be divisible by 13 or 2." \
					  "\n\n"
		print(stringIntro)

		print("--Checking Key--")
		#make a copy of the key to manipulate
		preKey = key
		#switch to lowercase if applicable
		preKey = preKey.lower()

		#check for both alphas and numbers

		#alpha conversion
		if preKey.isalpha():
			newKey = [int(ord(i) - 97) for i in preKey]

		#number conversion, split by commas
		else:
			try:
				newKey = []
				for i in preKey.split(','):
					temp = int(i)
					if temp >= 0 and temp <= 25:
						newKey.append(temp)
					else:
						print("Error adding in key.")
						raise Exception

			except Exception:
				#invalid character
				print("Error. Please enter the following for the key:"\
					  "\n -Alpha characters (a-z, A-Z)"
					  "\n -Numbers (between 0-25)"
					  "\n --If you're using numbers, add commas (',') to separate numbers within your key")
				exit()

		print("Your inputted key in number form: \n",newKey)

		print("\nConverting key to a matrix and performing checks...")
		#check if it's an m*m matrix
		m = sqrt(len(newKey))
		if m * m != len(newKey):
			print("Invalid Key. Please enter an m * m invertible matrix.\n")
			return False
		print("  --Valid m*m matrix: Yes")

		#create the matrix
		matrix = []
		matrixSize = int(m)
		while len(newKey) != 0:
			matrix.append(newKey[:matrixSize])
			newKey = newKey[matrixSize:]

		#check if it's invertible
		try:
			linalg.inv(matrix)
			print("  --is Invertible: Yes")
		except Exception:
			print("Error: Key is not an invertible matrix\n")
			return False

		#grab the determinant and check if it's equal to 0 or if it's divisible by 2 or 13
		det = int(linalg.det(matrix))
		print("  --Valid determinant: Yes")
		if det == 0 or det % 2 == 0 or det % 13 == 0:
			print("The determinant of your matrix is: ", det)
			print("\nError: The key must have a determinant of 0 and must not be divisible by 2 or 13")
			return False

		print("\nThe key is valid. Proceeding...\n")
		#return True if it passes all check
		self.key = matrix
		return True

	def encrypt(self, plainText):
		print("---Encrypting---")

		#change to lowercase
		plainText = plainText.lower()

		#convert plaintext to int and place into cipherText
		cipherText = [int(ord(i)) - 97 for i in plainText]

		#grab matrixSize
		matrixSize = int(len(self.key))

		#Check if the plainText has a length divisible by the matrixSize
		if len(cipherText) % matrixSize != 0:
			print("Plaintext is not long enough. Adding fluff.")
			while len(cipherText) % matrixSize != 0:
				cipherText.append(23)

		#Create Matrix from cipherText
		cMatrix = []
		#for plaintext larger than matrixSize
		if len(cipherText) > matrixSize:
			colCounter = 0

			#For odd matrice
			if matrixSize % 3 == 0:
				while len(cMatrix) < matrixSize:
					oCount = 0
					tempMatrix = []
					while oCount < len(cipherText):
						tempMatrix.append(cipherText[colCounter + oCount])
						oCount += 3
					cMatrix.append(tempMatrix)
					colCounter += 1

			# For even matrices
			else:
				while len(cMatrix) < matrixSize:
					eCount = 0
					tempMatrix = []
					while eCount < len(cipherText):
						tempMatrix.append(cipherText[colCounter + eCount])
						eCount +=2
					cMatrix.append(tempMatrix)
					colCounter+=1

		#for plaintext length equal to the matrixSize
		else:
			for i in range(0, matrixSize):
				tempMatrix = []
				tempMatrix.append(cipherText[i])
				cMatrix.append(tempMatrix)

		#Multiple the matrices and mod by 26
		cipherMatrix = np.dot(self.key, cMatrix) % 26

		#convert to list and manipulate back to text
		cipherMatrix = cipherMatrix.tolist()
		cipherMatrix = [list(i) for i in zip(*cipherMatrix)]
		cipherMatrix = [chr(i + 97) for inner in cipherMatrix for i in inner]
		cipherText = ''.join(i for inner in cipherMatrix for i in inner)

		return cipherText
		
	def decrypt(self, cipherText):
		print("---Decrypting---")

		#change to lowercase
		cipherText = cipherText.lower()

		#convert cipherText to int and place into plainText
		plainText = [int(ord(i)) - 97 for i in cipherText]

		#grab the matrixSize
		matrixSize = len(self.key)

		#Create Matrix for plainText
		pMatrix = []

		#For plainText larger than MatrixSize
		if len(plainText) > matrixSize:
			colCounter = 0

			#for odd matrices
			if matrixSize % 3 == 0:
				while len(pMatrix) < matrixSize:
					oCount = 0
					tempMatrix = []
					while oCount < len(plainText):
						tempMatrix.append(plainText[colCounter + oCount])
						oCount += 3
					pMatrix.append(tempMatrix)
					colCounter += 1

			#for even matrices
			else:
				while len(pMatrix) < matrixSize:
					eCount = 0
					tempMatrix = []
					while eCount < len(plainText):
						tempMatrix.append(plainText[colCounter + eCount])
						eCount +=2
					pMatrix.append(tempMatrix)
					colCounter+=1

		#for plaintext length equal to the matrixSize
		else:
			for i in range(0, matrixSize):
				tempMatrix = []
				tempMatrix.append(plainText[i])
				pMatrix.append(tempMatrix)

		#Find the inverse matrix and inverse determinant to calculate modular matrix multiplication with mod 26
		newKey = matrix(self.key).round().T

		#find the determinant
		determinant = int(linalg.det(self.key))

		#multiply by the determinant and convert to list
		newKey = matrix(newKey.getI() * determinant).round()
		newKey = newKey.tolist()
		newKey = [int(i) for inner in newKey for i in inner]

		#find the inverse determinant
		invdeterminant = 0
		for i in range(10000):
			if (determinant * i % 26) == 1:
				invdeterminant = i
				break

		#start constructing the inverse matrix
		inverse = []
		while len(inverse) < matrixSize:
			tempMatrix = []
			for i in range(0, matrixSize):
				tempMatrix.append((newKey[i] * invdeterminant) % 26)
			newKey = newKey[matrixSize:]
			inverse.append(tempMatrix)
		inverse = [list(i) for i in zip(*inverse)]

		#multiple the ciphertext matrix by the inverse matrix, then mod 26
		pMatrix = np.dot(inverse, pMatrix) % 26

		#convert to list and manipulate back to text
		pMatrix = [list(i) for i in zip(*pMatrix)]
		pMatrix = [chr(i + 97) for inner in pMatrix for i in inner]
		plainText = ''.join(i for inner in pMatrix for i in inner)
		return plainText

