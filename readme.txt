   _____ _               _         _____ _       _                   
  / ____| |             (_)       / ____(_)     | |                  
 | |    | | __ _ ___ ___ _  ___  | |     _ _ __ | |__   ___ _ __ ___ 
 | |    | |/ _` / __/ __| |/ __| | |    | | '_ \| '_ \ / _ \ '__/ __|
 | |____| | (_| \__ \__ \ | (__  | |____| | |_) | | | |  __/ |  \__ \
  \_____|_|\__,_|___/___/_|\___|  \_____|_| .__/|_| |_|\___|_|  |___/
                                          | |                        
                                          |_|                       
-----------------------------------------------------------------------
Classical Ciphers version 1.0 3/10/17
-----------------------------------------------------------------------


-----------------------------------------------------------------------
-----------------------------------------------------------------------
PROGRAMMING LANGUAGE

Programmed in Python utilizing numpy
	
Tested on Windows 10 and Ubuntu Linux

Should be fully compatible with python2.x or python3.x

-----------------------------------------------------------------------
-----------------------------------------------------------------------
EXECUTION INSTRUCTIONS:

	-Make sure you have both Python and numpy installed on the test machine

	-Download the zip folder and store it on your hard drive 
	
	-Open your terminal and navigate to the directory in which you stored the folder

	-type cipher.py and press enter

-----------------------------------------------------------------------
USING THE SOFTWARE:

	-Running the cipher.py file will display command line arguements

	./cipher <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE> <--OPTIONS/-O>

		Supported Ciphers:
		 - PLF: Playfair
		 - RTS: Row Transposition
		 - RFC: Railfence
		 - VIG: Vigenre
		 - CES: Caesar
		 - HIL: Hill

		 --OPTIONS - Optional setting: If enabled will ask for converting
				 to lowercase and removing non-alpha characters

	-Type ./cipher and do the following on the same line:

	-The abbreviation of the cipher name

	-The key (depending on the cipher the key format will be different) 
		Example: Key1 = cat Key2 = 12 Key3 = 1,2,3,5

	-Either type ENC to encrypt or DEC to decrypt

	-Type the name of the input file, including the extension

	-Type the name of the output file, including the extension

	-Optionally type -O to ask to convert the input file to lower case 
		and remove special characters

	-Press the enter key 

	-Within the terminal your input and output will be displayed along with 
		if execution was a success or any errors were found

	-Your encrypted or decrypted message will be stored in the output 
		file within the directory you are in

-----------------------------------------------------------------------

	-The following is an example of running the program with a Vigenre cipher,
		while using the key "security" and reading in from the file "in.txt"
		and outputing to the file "out.txt"

	./cipher VIG security ENC in.txt out.txt 

-----------------------------------------------------------------------
-----------------------------------------------------------------------
EXTRA CREDIT:

We did implement the extra-credit portion of the assignment

	-Our Hill cipher can be ran using the HIL abbreviation
-----------------------------------------------------------------------
-----------------------------------------------------------------------
SPECIAL INCLUSIONS:

	-Our software includes an option to convert all text to lowercase and
		strip the strings of non-alpha characters

	-Our software comes with a makeclean.py file that if ran will remove 
		all excess .pyc files in the directory that are created as a result
		of running the program

-----------------------------------------------------------------------
-----------------------------------------------------------------------
EXECUTION EXAMPLES FOR EACH CIPHER

-----------------------------------------------------------------------
PLAYFAIR

key = string of alpha characters

	C:\Users\Matth\Desktop\cipher>cipher PLF security ENC in.txt out.txt 

	INPUT: thequickbrownfoxjumpsoverthelazydog

	OUTPUT: afsvsargkbnxmgxuasnluletebfuoiwbhlhw

	Success!
	

-----------------------------------------------------------------------
ROW TRANSPOSITION 

key = list of integers or string of alpha characters

	C:\Users\Matt\Desktop\cipher>cipher RTS 1,4,2,6 ENC in.txt out.txt 

	INPUT: thequickbrownfoxjumpsoverthelazydog

	OUTPUT: tubnjsrldecoomvhzghirfuotaoqkwxpeey$

	Success!

-----------------------------------------------------------------------
RAILFENCE

key = integer

	C:\Users\Matt\Desktop\cipher>python cipher.py RFC 4 ENC in.txt output.txt

	INPUT: thequickbrownfoxjumpsoverthelazydog

	OUTPUT: tubnjsrldhirfuotaoecoomvhzgqkwxpeey

	Success!

-----------------------------------------------------------------------
VIGENRE

key = string

	C:\Users\Matt\Desktop\cipher>cipher VIG security ENC in.txt out.txt 

	INPUT: thequickbrownfoxjumpsoverthelazydog
			
	OUTPUT: llgklqvitvqqenhvbyojjwocjxjyciswvsi

	Success!
	
------------------------------------------------------------------------
CEASAR

key = integer or character

	C:\Users\Matt\Desktop\cipher>cipher CES 44 ENC in.txt out.txt

	INPUT: thequickbrownfoxjumpsoverthelazydog

	OUTPUT: lzwimauctjgofxgpbmehkgnwjlzwdsrqvgy

	Success!

-------------------------------------------------------------------------
HILL

string =  m * m invertible matrix.

	C:\Users\Matt\Desktop\cipher>python cipher.py HIL 1,2,3,5 ENC in.txt output.txt

	The Hill Cipher is a polygraphic substitution cipher based on linear algebra. 
		This cipher was invented by Lester S. Hill in 1929. The cipher uses an n*n
		invertible matrix as the key, which cannot be divisible by any factors of 
		the total length of the alphabet scheme used. We will be using the english
		alphabet as the scheme (which is 26). This means that the determinant cannot
		be divisible by 13 or 2.


	--Checking Key--
	Your inputted key in number form:
	 [1, 2, 3, 5]

	Converting key to a matrix and performing checks...
	  --Valid m*m matrix: Yes
	  --is Invertible: Yes
	  --Valid determinant: Yes

	The key is valid. Proceeding...

	---Encrypting---
	Plaintext is not long enough. Adding fluff.

	INPUT: thequickbrownfoxjumpsoverthelazydog

	OUTPUT: hokokwwejkgwxmibxxqhuudfdqpplhvnfbad

	Success!