import arithmetic

print "Welcome to our calculator"

while True:
	problem = raw_input(" --> ")
	problem = problem.strip()
	numbers = problem.split(" ")
	operand = numbers[0]
	numbers = numbers[1:]
	for i in range(len(numbers)):
		numbers[i] = int(numbers[i])

	if operand == 'q':
		break

	elif len(numbers)<1:
		print "too few numbers"
		continue

	elif operand == 'square':
		ans = arithmetic.multiply(numbers[0], numbers[0])
		print ans

	elif operand == 'cube':
		ans = arithmetic.power(numbers[0], 3)
		print ans

	elif len(numbers)<2:
		print "Too few numbers"
		continue

	elif operand == '+':
		ans = 0
		for i in range(len(numbers)):
			ans = arithmetic.add(ans, numbers[i])
		print ans

	elif operand == '-':
		ans = numbers[0]
		for i in range(1,len(numbers)):
			ans = arithmetic.subtract(ans, numbers[i])
		print ans

	elif operand == '*':
		ans = 1
		for i in range(len(numbers)):
			ans = arithmetic.multiply(ans, numbers[i])
		print ans

	elif operand == '/':
		ans = float(numbers[0])
		for i in range(1,len(numbers)):
			ans = arithmetic.divide(ans, numbers[i])
		print ans

	elif operand == 'power':
		ans = arithmetic.power(float(numbers[0]), numbers[1])
		print ans

	elif operand == 'mod':
		ans = arithmetic.mod(numbers[0], numbers[1])
		print ans

	else:
		print "Invalid Input"

	
