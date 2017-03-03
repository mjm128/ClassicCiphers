import math

class RowTransposition:

    def __init__(self):
        self.key = None

    def setKey(self, key):
        
		# if all items in key are numbers, just use the key as it is
		if all(isinstance(item, int) for item in key):
			print("Error: Please use a keyword for the key and not numbers!")
			return True
		elif key.isalpha():
			self.key = self.convertKey(key)
			return True

		else:
			print("Error: Key contains either numbers and/or letters!")
			return False

    def convertKey(self, key):

        List = []
        colNumber = len(key)

        # Convert letters to their numeric position in the alphabet
        for letter in key:
            if letter >= 'a' and letter <= 'z':
                x = int(ord(letter) - ord('a'))

            elif letter >= 'A' and letter <= 'Z':
                x = int(ord(letter) - ord('A'))

            List.append(x)

        tempList = [0 for x in range(len(List))]

        for x in range(len(List)):
            maxIndex = List.index(max(List))
            List[maxIndex] = -1 # Found and then replaced by -1, indicating that it has found it
            tempList[maxIndex] = colNumber
            colNumber -= 1

        del(List)

        return (tempList)

    def encrypt(self, plainText):

        position = 0
        result = ""
        endCharacter = "$"

        List = [[] for x in range(len(self.key))] 

        # Incase if spaces need to be ignored
        #plainText = ''.join(letter for letter in plainText if letter.isalnum())

        # Remove /n and add end character
        #plainText = plainText[0:-1]
        plainText = plainText + endCharacter

        # Sorted key that will be used for encryption
        modifiedKey = sorted(self.key)

        for colNumber in self.key:
            # Insert key for first row to help identify the columns
            List[position].append(str(colNumber))
            position += 1
   
            if position == len(self.key):
                position = 0

        for letter in plainText:
            if letter == " ":
                List[position].append("#")
            else:
                # append by List[position][0] - ROW
                List[position].append(letter)

            position += 1

            # Reset position
            if position == len(self.key):
                position = 0
      
            # If it reaches the end of the string, place pad letters
            if letter == str(plainText[-1:]):
                while(position < len(self.key)):
                    List[position].append("$")    
                    position += 1

        for i in range(len(self.key)):
            for j in range(len(self.key)):
                # Create string when the List key equals to the modifiedKey
                if(int(modifiedKey[i]) == int(List[j][0])):
                    tempString = ''.join(List[j])
                    result += tempString
        
        # Create cipherText: Remove letters in the result string
        cipherText = ''.join(letter for letter in result if not letter.isdigit())

        del(List)

        return (cipherText)

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