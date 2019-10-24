#kolton wesson
#2nd period 10/21/19
mystery = "arizona"
mystery = list(mystery)
guessWord = []
for a in mystery:
	guessWord.append("_")

score = 0
print(guessWord)
while score < 7:
	guess = input("Enter a letter: ")

	if guess in mystery:
		count = 0
		for letter in mystery:
			if letter == guess:
				guessWord[count] = guess
			count = count + 1

	print(guessWord)

	myWord = "arizona"
	myList = list(myWord)

	mysteryList = []

	for letter in myList:
		mysteryList.append("_")

	print(mysteryList)




	choice = input("type a word: ")

	if choice == myWord:
		print("its a match")
	else:
		print("not a match")

	# how to check if letter is in the word

	letter = input("Type a letter ")
	if letter in myWord:
		print("letter is in the word ")
		for l in myWord:
			if l == letter:
				mysteryList[count] = letter
			else:
				print("letter is not in the word ")
				score = score + 1
