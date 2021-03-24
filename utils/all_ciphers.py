import string
import base64 as b64
import string
import re

alphabet = string.ascii_lowercase
alphabet_upper = alphabet.upper()


bacon_dict_complete = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB', 'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA', 'Z': 'BBAAB'}


bacon_dict_standard = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAA', 'K': 'ABAAB', 'L': 'ABABA', 'M': 'ABABB', 'N': 'ABBAA', 'O': 'ABBAB', 'P': 'ABBBA', 'Q': 'ABBBB', 'R': 'BAAAA', 'S': 'BAAAB', 'T': 'BAABA', 'U': 'BAABB', 'V': 'BAABB', 'W': 'BABAA', 'X': 'BABAB', 'Y': 'BABBA', 'Z': 'BABBB'}


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-' , ' ':'/'} 

tap_code_dict={'A':'. .' , 'B':'. ..', 'C':'. ...','K':'. ...', 'D':'. ....' , 'E':'. .....'
            ,'F':'.. .','G':'.. ..', 'H':'.. ...', 'I':'.. ....' , 'J':'.. .....'
            ,'L':'... .','M':'... ..', 'N':'... ...', 'O':'... ....' , 'P':'... .....'
            ,'Q':'.... .','R':'.... ..', 'S':'.... ...', 'T':'.... ....' , 'U':'.... .....'
            ,'V':'..... .','W':'..... ..', 'X':'..... ...', 'Y':'..... ....' , 'Z':'..... .....', ' ':'/ /'}



def atbash(text):
	if text==None:
		response="You didn't enter the test. Please enter the command with the text"
		return response
	else:
		alphabets=list(string.ascii_lowercase)
		decrypt=''
		for i in text:
				try:
						decrypt=decrypt+(alphabets[25-alphabets.index(i.lower())])
				except:
						decrypt=decrypt+str(i)
		return decrypt



def caesar(text,s): 
		if s != None:
			result = "" 
			s=26-s
			for i in range(0,len(text)): 
					char = text[i] 
					if char.isalpha():
							if char != " ":
									if (char.isupper()): 
											result += chr((ord(char) + s-65) % 26 + 65) 
					
									else: 
											result += chr((ord(char) + s - 97) % 26 + 97) 
							else:
									result=result+ char
					else:
							result += char
			return result			
		else:
			output_l=[]
			for i in range(1,27):
					decrypt=caesar(text,i)
					output_l.append(f"Key = {i}: {decrypt}")
			outp=''
			for i in output_l:
					outp=outp+i+"\n"
			return outp			



def vigenere(text, key, mode):
	if key != None and text != None:
		lowercase = text.lower()
		encrypted = ''
		index = None
		counter = 0
		alphabet = string.ascii_lowercase
		alphabet_upper=alphabet.upper()
		# First do the shifting thingy
		for char in lowercase:
			# Make sure the index does not exceed the key's length
			if counter == len(key): counter = 0

			if char not in alphabet:
				encrypted += char
			else:
				index = alphabet.index(char)
				
				if mode == 'encrypt':
					index += alphabet.index(key[counter])
				else:
					index -= alphabet.index(key[counter])

				index %= len(alphabet)
				encrypted += alphabet[index]
				counter += 1
		
		# Restore cases
		for x in range(len(encrypted)):
			encrypted = list(encrypted)
			if text[x] in alphabet_upper:
				encrypted[x] = encrypted[x].upper()
			
		return ''.join(encrypted)
	else:
		response="You have not entered the key or the code. Please enter the command with the key as well as the text to be decoded/encoded"
		return response


def base64(arg, mode):
  if mode == 'decode':
    padding_needed = len(arg) % 4
    if padding_needed:
      arg += '===' # See https://stackoverflow.com/a/49459036/14437456
    decrypt = b64.b64decode(arg).decode('utf-8')
    return decrypt
  
  elif mode == 'encode':
    message_bytes = arg.encode('ascii')
    base64_bytes = b64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def bacon_cipher(text, mode, variant):
    if mode == 'encode':
        if variant == 'complete':
            bacon_dict = bacon_dict_complete
        elif variant == 'standard':

            bacon_dict = bacon_dict_standard
        else:
            text = variant + ' ' + text
            bacon_dict = bacon_dict_standard

        text = text.upper()
        ciphertext = ''
        for char in text:
            try:
                ciphertext += bacon_dict[char] + ' '
            except:
                ciphertext += char + ' '

        return ciphertext
    elif mode == 'decode':
        if variant == 'complete':
            bacon_dict = bacon_dict_complete
        elif variant == 'standard':

            bacon_dict = bacon_dict_standard
        else:
            text = variant + ' ' + text
            bacon_dict = bacon_dict_standard

        text = text.split()
        bacon_dict = dict((v, k) for (k, v) in bacon_dict.items())  # See https://stackoverflow.com/a/50232911/14437456
        plaintext = ''
        for item in text:
            try:
                plaintext += bacon_dict[item]
            except:
                pass

        return plaintext



def morse_encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else: 
            cipher += ' / '
  
    return cipher 


def morse_decrypt(message):
	message=message.split()
	morse_dict=dict((v, k) for (k, v) in MORSE_CODE_DICT.items())
	decipher=''
	for i in message:
		decipher += morse_dict[i]
	return decipher

def morse(message):
	try:
		return morse_decrypt(message)
	except:
		return morse_encrypt(message)



def tap_encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += tap_code_dict[letter.upper()] + ' '
        else: 
            cipher += ' / '
  
    return cipher 

def tap_decrypt(message):
    message = message.replace('/', ' / / ')
    message_pair = []
    i = 0
    while i < len(message.split()) - 1:
        temp_str = message.split()[i] + ' ' + message.split()[i + 1]
        message_pair.append(temp_str)
        i = i + 2
    decipher = ''
    for letter in message_pair:
        #decipher += \
        decipher = decipher + list(tap_code_dict.keys())[list(tap_code_dict.values()).index(letter)] 
    return decipher


def tap(text):
	
	if len(text.split())==1:
		return tap_encrypt(text)
	else:
		try:
			return tap_decrypt(text)
		except:
			return tap_encrypt(text)

def a1z26(message):

	alphabets=list(string.ascii_lowercase)
	cont=message
	encrypt=''
	num_list=[]
	for i in cont[0:]:
		encrypt=encrypt  + str(i) + " "
		try:
			num_list.append(int(i))                
		except:
			pass
	decrypt=''
	if cont[0].isalpha():
		for i in encrypt:
			try:
				z=i.lower()
				decrypt=decrypt+' '+str(alphabets.index(z)+1)
			except:
				decrypt=decrypt+str(i)
	else:
		for i in num_list:
			decrypt=decrypt + " " + str(alphabets[i-1])
	return decrypt

def null(string): 
    res = ''
    string = string.split()

    for word in string:
      for x in range(len(word)):
        if word[x].isalpha(): res += word[x]; break
  
    return res

def polybius_encrypt(string, square):
  string = re.sub(r'[^A-Za-z]', '', string)
  string = string.lower()
  
  encrypted = []
  for i in string:
    n = square.find(i) + 1
    row,col = divmod(n,5)
    encrypted.append(str(row+1)+str(col))
  

  return ' '.join(encrypted)

def polybius_decrypt(string, square):
  plain = []
  string = string.split()

  for i in range(len(string)):
      row = int(string[i][0])
      col = int(string[i][1])
      letter = square[(row-1)*5 + col-1]
      plain.append(letter)

  return ''.join(plain)
