#19) How Do You Handle Exceptions With Try/Except/Finally In Python?


def divide(x, y):
	try:
		result = x // y
		print("Yes ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

divide(6, 3)
divide(9, 0)

def divide(x, y):
	try:
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yes ! Your answer is :", result)
divide(69, 2)
divide(7, 0)