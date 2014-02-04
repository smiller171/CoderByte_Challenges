def LetterChanges(str):
	length=len(str)
	str=str.lower()
	i=0
	while i < length:
		str[i]=ChangeLetter(str[i])
		i=i+1
	return str
	
def ChangeLetter(char):
	if char.isalpha():
		char=chr(ord(char)+1)
		char=VowelChange(char)
		return char
	else:
		return char

def VowelChange(char):
	if isVowel(char):
		char=char.upper()
		return char
	else:
		return char

def isVowel(char):
    return char.lower() in 'aeiou'

print LetterChanges(raw_input())