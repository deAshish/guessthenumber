# A number guessing game
from random import randint

random_number = randint(1,20)
tries = 0
while True:
	heart_symbol = u'\u2764'
	heart = 'Total lives:' + (4-tries)*heart_symbol
	print heart
	if tries>3:
		print ("You lost. The number was:{}".format(random_number))
		break
	try:
		guess =int(raw_input("Guess a number: "))
		tries +=1
		if guess == random_number:
			print ("You won!! The number was {}".format(random_number))
			break
		elif guess < random_number:
			print "Its not the required number,  Go higher!"
		elif guess > random_number:
			print "Its not the required number, Go lower!"
	except:
		print"Wrong input!!"
