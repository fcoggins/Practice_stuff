

def count(max, incr):
	i = 0
	numbers = []
	print max
	print type(max)

	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)

		i += incr
		print "Numbers now: ", numbers
		print "At the bottom i is %d"  % i

	print "The numbers: "

	for num in numbers:
		print num


def count_for(max, incr):
	numbers = []
	for i in range(0, max, incr):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d"  % i

	print "The numbers: "

	for num in numbers:
		print num




print "Enter a number"
number = int(raw_input("> "))
print "Enter an increment"
increment = int(raw_input("> "))
count(number, increment)
count_for(number, increment)