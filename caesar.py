def alphabet_position(letter):
	letter = letter.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alphalist = list(alphabet)
	position = alphalist.index(letter)
	return(position)

def rotate_character(char, rot):
	if char.isupper():
		charposition = alphabet_position(char)
		newposition = (charposition + rot) % 26
		newchar = chr(newposition + 65)
		return(newchar)
	elif char.islower():
		charposition = alphabet_position(char)
		newposition = (charposition + rot) % 26
		newchar = chr(newposition + 97)
		return(newchar)
	else:
		return(char)

def encrypt(text, rot):
	rot = int(rot)
	textblock = list(text)
	newtext = []
	for character in textblock:
		newchar = rotate_character(character, rot)
		newtext.append(newchar)
	glue = ""
	encryption = glue.join(newtext)
	return(encryption)
