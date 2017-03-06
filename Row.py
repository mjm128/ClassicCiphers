import math

class Row:

    def __init__(self):
        self.key = None

    def setKey(self, key):
		error = ""
		if len(key) > 0:
			l = [pair for pair in emumerate(key)]
			for pair in l:
				if !pair[0].isalpha():
					error = "Key must contain only alpha characters"
					break
			if error == "":
				self.key = l
				return True
			try:
				l = []
				for index, element in enumerate(key):
					l.append(int(element), index)
				self.key = l
				return True
			except:
				error = "Key must contain only integers"
				
		print(error)
		return False				

	def encrypt(self, plainText):
		text = [i for i in plainText]
		if len(text) % len(key) != 0:
			tmp = [None] * len(text) % len(key)
			text += tmp
		matrix = [None] * (len(text) / len(key))
		for index, value in enumerate(text):
			matrix[index%len(key)] = value
		
		
    def decrypt(self, cipherText):

        position = 0
        counter = 0
        tempString = ""
        plainText = ""

        List = [[] for x in range(len(self.key))]

        # Determines how many letters per column
        splitStringValue = math.ceil(len(cipherText)/len(self.key))
        x = splitStringValue
        # Split the cipherString based on the splitStringValue
        cipherText = [cipherText[i:i+splitStringValue] for i in range(0, len(cipherText), splitStringValue)]

        for i in self.key:
            temp = ''.join(cipherText[i-1]) # List starts at 0, thus i-1
            tempString += temp
    
        # Used to append to list
        cipherText = ''.join(letter for letter in tempString if not letter.isdigit())

        for letter in cipherText:
          # append by List[position][0] - ROW
          List[position].append(letter)
          counter += 1
          # check every nth letter, counter starts at 0 and goes up to x
          if(counter == x):
            position += 1
            x += splitStringValue
    
        # Max item count in a row
        maxItemLength = len(List[0])

        for i in range(maxItemLength):
          for j in range(len(List)):
            tempString2 = ''.join(List[j][i])
            plainText += tempString2
      
        del(List)

        return (plainText)

    # For display purposes
    def stripText(self, Text):
        Text = Text.replace("$", "")
        Text = Text.replace("#", " ")
        return(Text)