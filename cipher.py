import sys
from CipherInterface import CipherInterface
from Hill import Hill
from Caesar import Caesar
from Vigenre import Vigenre

def main(*arguments):
	#Display instructions if improper argument length is given
	if len(arguments) != 6:
		print("\nINVALID ARGUMENTS:")
		print("./cipher <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>")
		print("\n- PLF: Playfair\n- RTS: Row Transposition\n"
		+ "- RFC: Railfence\n- VIG: Vigenre\n- CES: Caesar\n- HIL: Hill")
		quit()
	
	cipherName = arguments[1].upper()
	key = arguments[2].upper()
	encOrDec = arguments[3].upper()
	inFile = arguments[4]
	outFile = arguments[5]
	
	#Open data from input file
	with open(inFile,"r") as f:
		input = f.read()
	
	if cipherName == "PLF":
		pass
	
	elif cipherName == "RTS":
		pass
		
	elif cipherName == "RFC":
		pass
		
	elif cipherName == "VIG":
		cipher = Vigenre()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(input)
			elif encOrDec == "DEC":
				output = cipher.decrypt(input)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		
	elif cipherName == "CES":
		cipher = Caesar()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(input)
			elif encOrDec == "DEC":
				output = cipher.decrypt(input)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure!")
			quit()
		
	elif cipherName == "HIL":
		pass
		
	else:
		print("Cipher Name Error / Unsupported Cipher")
		quit()
		
		
	with open(outFile, "w") as f:
		f.write(output)
		print("Success!")


if __name__ == '__main__':
	main(*sys.argv)