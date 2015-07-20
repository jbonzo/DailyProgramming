#wordInput = raw_input("What is the word that you want balanced?\nInput: ").upper()

def weight(distance, letter):
	return distance * (ord(letter) - 64)

def balance(word):
	left = 0
	right = 0
	for bp in range(1, len(word) - 2):
		print "\nMiddle is ", word[bp]
		for i in range(bp):
			left += weight(abs(bp - i), word[i])
		for i in range(bp + 1, len(word)):
			right += weight(abs(bp - i), word[i])
			print "bp=", str(bp), "i=", str(i), "letter=", word[i], "weight of letter=" + str(weight(abs(bp - i), word[i]))
		print "left ", str(left), "right ", str(right), "\n"
		if left == right:
			return word[:bp] + " " + word[bp] + " " + word[bp + 1:] + " - " + str(left)
	return word + " DOES NOT BALANCE"

print balance("STEAD")
print balance("CONSUBSTANTIATION")
	