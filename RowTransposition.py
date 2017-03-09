import math

class RowTransposition:

	def __init__(self):

		self.key = None

	def hasNumbersInString(self, key):
		passInspection = False
		counter = 0

		for i in key:
			if i.isdigit():
				passInspection = True
				counter += 1

			# Must have two digits in order for "," to passInspection
			elif i == "," and counter > 2:
				passInspection = True

			elif i.isalpha():
				passInspection = False

			else:

				passInspection = False

		return (passInspection)

	def setKey(self, key):

		# if all items in key are numbers, change string key into int list
		if self.hasNumbersInString(key):
			key = [int(s) for s in key.split(',')]

			self.key = self.trueKey(key)
			return True

		# if all items are letters:
		elif key.isalpha():
			self.key = self.trueKey(self.convertKey(key))

			return True

		else:

			return False

	def convertKey(self, key):

		List = []

		colNumber = len(key)
		modifiedList = sorted(List)

		# Convert letters to their numeric position in the alphabet
		for letter in key:
			if letter >= 'a' and letter <= 'z':
				x = int(ord(letter) - ord('a'))

			elif letter >= 'A' and letter <= 'Z':
				x = int(ord(letter) - ord('A'))

			List.append(x)

		return (List)

	def trueKey(self, key):
		colNumber = len(key)
		tempList = [0 for x in range(len(key))]

		for x in range(len(key)):
			# Find max value's index by checking right to left
			maxIndex = len(key) - key[::-1].index(max(key)) - 1
			# Found and then replaced by -1, indicating that it has found it
			key[maxIndex] = -1
			tempList[maxIndex] = colNumber
			colNumber -= 1

		return (tempList)

	def encrypt(self, plainText):

		position = 0
		counter = 0
		cipherText = ''
		endOfString = False

		List = [[] for x in range(len(self.key))] 

        # Remove /n from plainText if it exists.
		plainText = plainText.replace('\n', '')

		for letter in plainText:
			List[position].append(letter)

			position += 1
			counter += 1

			if counter == len(plainText):
				endOfString = True

			# Check to see if padding is needed
			if abs(len(plainText)) % abs(len(self.key)) != 0:
				# If it reaches the end of the string, place pad letters
				if endOfString:
					while(position < len(self.key)):
						List[position].append('$')    
						position += 1

			# Reset position
			if position == len(self.key):
				position = 0

		for i in range(len(self.key)):
			placement = self.key[i] - 1
			tempString = ''.join(List[placement])
			cipherText += tempString

		del(counter)
		del(List)

		return (cipherText)

	def decrypt(self, cipherText):

		position = 0
		counter = 0
		tempString = ''
		plainText = ''

		List = [[] for x in range(len(self.key))]

		# Determines how many letters per column
		splitStringValue = math.ceil(len(cipherText)/len(self.key))
		x = splitStringValue

		for i in self.key:
			placement = i - 1
			for letter in cipherText[position:]:
				List[placement].append(letter)
				counter += 1

				if counter == x:
					position += splitStringValue
					break

			counter = 0

			if position == len(cipherText):
				position = 0

		for i in range(splitStringValue):
			for j in range(len(List)):
				tempString2 = ''.join(List[j][i])
				plainText += tempString2

		del(List)

		plainText = plainText.replace('$', '')
		return (plainText)
