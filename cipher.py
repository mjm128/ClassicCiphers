import sys
from CipherInterface import CipherInterface

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
		
	cipher = CipherInterface()
		
	if cipherName == "PLF":
		cipher.setKey(5)
		print()
	
	
	elif cipherName == "RTS":
		pass
		
	elif cipherName == "RFC":
		pass
		
	elif cipherName == "VIG":
		pass
		
	elif cipehrName == "CIS":
		pass
		
	elif cipherName == "HIL":
		pass
		
	else:
		pass
		
		
	# with open(outFile, "r+") as f:
		# f.seek(0)
		# f.write(output)
		# f.truncate()
	
	print("Success!")


if __name__ == '__main__':
	main(*sys.argv)