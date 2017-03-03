#!/usr/bin/env python
import sys
from Hill import Hill
from Caesar import Caesar
from Vigenre import Vigenre
from Railfence import Railfence
from Hill import Hill
from Playfair import Playfair
from RowTransposition import RowTransposition

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
	
	options = [None] * 2
	while options[0] != 'y' and options[0] != 'n':
		if sys.version[0] == '3':
			options[0] = input("Strip input file of non alphabetical characters? (Y/N): ").lower()
		elif sys.version[0] == '2':
			options[0] = raw_input("Strip input file of non alphabetical characters? (Y/N): ").lower() 
	while options[1] != 'y' and options[1] != 'n': 
		if sys.version[0] == '3':
			options[1] = input("Convert to lower case? (Y/N): ").lower()
		elif sys.version[0] == '2':
			options[1] = raw_input("Convert to lower case? (Y/N): ").lower()

		
	#Open data from inputString file
	with open(inFile,"r") as f:
		if options[0] == options[1] == 'n':
			#Both no
			inputString = f.read()
		elif options[0] == 'n':
			#lower case
			inputString = f.read().lower()
		elif options[1] == 'n':
			#strip non-alpha
			inputString = ''.join([c for c in f.read() if c.isalpha()])
		
		else:
			#strip non-alpha characters and lower case
			inputString = ''.join([c.lower() for c in f.read() if c.isalpha()])
			
	print("\nINPUT: " + inputString)
	if cipherName == "PLF":
		cipher = Playfair()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(inputString)
			elif encOrDec == "DEC":
				output = cipher.decrypt(inputString)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure: Invalid Key")
			quit()
	
	elif cipherName == "RTS":
		cipher = RowTransposition()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(inputString)
			elif encOrDec == "DEC":
				output = cipher.decrypt(inputString)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure: Invalid Key")
			quit()
		
	elif cipherName == "RFC":
		cipher = Railfence()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(inputString)
			elif encOrDec == "DEC":
				output = cipher.decrypt(inputString)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure: Invalid Key")
			quit()
		
	elif cipherName == "VIG":
		cipher = Vigenre()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(inputString)
			elif encOrDec == "DEC":
				output = cipher.decrypt(inputString)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure: Invalid Key")
			quit()
		
	elif cipherName == "CES":
		cipher = Caesar()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(inputString)
			elif encOrDec == "DEC":
				output = cipher.decrypt(inputString)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure: Invalid Key")
			quit()
		
	elif cipherName == "HIL":
		cipher = Hill()
		if cipher.setKey(key):
			if encOrDec == "ENC":
				output = cipher.encrypt(inputString)
			elif encOrDec == "DEC":
				output = cipher.decrypt(inputString)
			else:
				print("Invalid Encryption/Decryption Option")
				quit()
		else:
			print("Failure: Invalid Key")
			quit()
		
	else:
		print("Cipher Name Error / Unsupported Cipher")
		quit()
		
	print("\nOUTPUT: " + output)
	with open(outFile, "w") as f:
		f.write(output)
		print("\nSuccess!")

if __name__ == '__main__':
	main(*sys.argv)
