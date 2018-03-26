# # Given a string with special characters, reverse the string in a way that special characters are not affected.

def isAlphabet(x):
	return x.isalpha();

def reverse(string):
	stringList = toList(string)
	size = len(stringList) - 1
	i = 0
	while i < size:
			if not isAlphabet(stringList[size]):
				size -= 1
			elif not isAlphabet(stringList[i]):
				i += 1
			else:
				stringList[i], stringList[size] = stringList[size], stringList[i]
				size -= 1
				i += 1
	return toString(stringList)

def toList(string):
	list = []
	for s in string:
		list.append(s)
	return list

def toString(list):
	return ''.join(list)