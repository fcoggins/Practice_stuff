def make_a_guess(number):
	number_of_guesses = 0
	while True:
		guess = raw_input('Your guess? > ')
		guess = str(guess)
		guess = check_input_type(guess)
		guess = int(guess)
		check_input_range(guess)
		number_of_guesses += 1
		if guess < number:
			print "Your guess is too low, try again."
		if guess > number:
			print "Your guess is too high, try again."
		if guess == number:
			return number_of_guesses


def check_input_type(guess):
	for char in guess:
		if char.isdigit() == False:
			guess = raw_input("Please enter a valid number. Your guess? >  ")
			guess = check_input_type(guess)
			break
	return guess

def check_input_range(guess):
	if guess < 0 or guess > 100:
		guess = raw_input("Please enter a valid number. Your guess? >  ")
		guess = int(guess)
		guess = check_input_range(guess)
	return guess		

def main():
	import random
	best_trys = 1000000

	print "Welcome to the guessing game. What is your name?"
	name = raw_input(" > ")
	print "Hello %s, guess a number between 1 and 100." % name	

	while True:
		the_num = random.randint(0, 100)
		
		trys = make_a_guess(the_num)
		if trys < best_trys:
			best_trys = trys
		print "Great job %s! You guessed the number in %d trys. Your best score is %d" % (name, trys, best_trys)
		


		keep_on = raw_input ("If you want to stop playing type 'q' > ") 
		if keep_on == 'q':
			break
		else:
			print "Great, let's play again."


main()