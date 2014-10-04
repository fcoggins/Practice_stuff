print "You enter a dark room with two doors Do you enter through door #1 or door #2"

door = raw_input("> ")

if door == "1":
	print "There is a giant bear"
	print "1, Take the cake"
	print "2, Scream at the bear."

	bear = raw_input('> ')

	if bear == "1":
		print "The bear eats your face off. Good job"
	elif bear == "2":
		print "The bear eats your legs off. Good job"
	else:
		print "Well doing %s is better because the bear runs away." % bear

elif door =="2":
	print "You stare int the abyss."
	print "1. Cafe au lait."
	print "2. Yellow squash."
	print "3. Sing a lullaby"

	insanity = raw_input('****')

	if insanity == 1:
		print "You drown in a pool of coffee. Yay!"
	else:
		print "You melt into a puddle of goo.  Whoppee!"

# else:
# 	print "Well, I don't want to play either!!!"
