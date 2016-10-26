import string

def hexXOR(char,key):
#	Function to XOR two hexadecimal input numbers and 
#	output the correct ascii character.
	return int(char,16) ^ ord(str(key))

def mtpCrack(cipherTxt, key, position):
#   Function for cracking a Multi-Time Pad Cipher 
#	Input: Cipher Text, proposed Key and column Number to crack
#	Output: Plain Text Character for each of the sentences
	cSentences = cipherTxt.split("*")	
	compareList=[]
	asciiList=[]

	printableASCII = string.printable
	#acceptableChars = list(printableASCII)
	acceptableChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', ' ']

	# Generate the Characters from the specified column and print to console
	for j in range(0,len(cSentences)):
		currSentence = cSentences[j]
		charList = [currSentence[k:k+2] for k in range(0, len(currSentence), 2)]
		compareList.append(charList[position-1])
	if key == chr(0):
		print("Current Column to compare:", compareList)
		print("Acceptable Ascii Characters:", acceptableChars)
		print("Possible solutions:")
	
	corrKey = hexXOR(compareList[0],key)
	corrKey = chr(corrKey)
	# Run hexXOR on all elements of the compareList and output results	
	printList = False 
	for tok in compareList:
		val = hexXOR(tok,corrKey)
		asciiList.append(chr(val))
	
	for i in asciiList:
		if i in acceptableChars:
			printList = True
	if printList:
		print(key,":",asciiList)

def runMtpCrack(position):
	for i in range(0,127):
		mtpCrack(ctxt,chr(i),position)

# run
ctxt = "72ABFD6498E2FDCAD71545F12DCC9FAA523D3CA0E03A0441B445*64A2F374D6E4AFDB851A53F62DC892B9456D68AAE1751949A845*64A2E46893A5BEDFD1071CE165DA89BD533D29EFE275195DA545*7EAFE06884A5B1D7C05453F02DD99FF853743BA7E074095DB445*67A2F37F93A5B9D7C15448EA689B9FB4526D20AEE16E4C49AF54*67ABE46199F7B9CD85154EE72DC89FB45B7426A8AF7B1E43B345*7FBCF37F97E9B19ED11C59A269DE9BB417743BEFE9731F46B945"
runMtpCrack(15)
# GIVEN TEXT: 26 Wide ; 7 Tall
#	----------------------------------------------------
#	72ABFD6498E2FDCAD71545F12DCC9FAA523D3CA0E03A0441B445
#	64A2F374D6E4AFDB851A53F62DC892B9456D68AAE1751949A845
#	64A2E46893A5BEDFD1071CE165DA89BD533D29EFE275195DA545
#	7EAFE06884A5B1D7C05453F02DD99FF853743BA7E074095DB445
#	67A2F37F93A5B9D7C15448EA689B9FB4526D20AEE16E4C49AF54
#	67ABE46199F7B9CD85154EE72DC89FB45B7426A8AF7B1E43B345
#	7FBCF37F97E9B19ED11C59A269DE9BB417743BEFE9731F46B945
#	----------------------------------------------------