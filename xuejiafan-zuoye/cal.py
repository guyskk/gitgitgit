while True:
	def cal():
		num1 = float(raw_input('Please enter a number: '))
		op = raw_input('Please enter a operator: ')
		num2 = float(raw_input('Please enter another number: '))
		if op == '+':
			print "result: ",num1+num2
		elif op == '-':
			print "result: ",num1-num2
		elif op == '/':
			print "result: ",num1/num2
		elif op == '*':
			print "result: ",num1*num2
		elif op == '**':
			print "result: ",num1**num2
		else:
			print "Unknown operator ",op
	cal()
