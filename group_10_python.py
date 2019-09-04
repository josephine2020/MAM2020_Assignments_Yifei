import math



def question_1():
	answer_a = 'The \"=\" operator assigns the value on the right to the variable name on the left. The "==" operator compares the variable on the left to the variable on the right. The former stores a variable in the memory and the latter produces a boolean variable that contains the result of the logical operation.'
	answer_b = 'Operator precedence is the order at which operators of different priorities are evaluated. Operator associativity is the order at which operators of the same priority level are evaluated, the default of which is from left to right. No. The majority of the operators have left-to-right associativity.'
	print('For question 1')
	print('The answer to a is')
	print(answer_a)
	print('The answer to b is')
	print(answer_b)

def question_2():
	pv, r, n, t = 100, 0.05, 2, 3
	fv = pv * (1 + r / n) ** (n * t)
	fv_con = pv * math.exp(r * t)
	print('For question 2')
	print('The answer to a is')
	print('Future value of compounding 3 years is ' + str(fv))
	print('The answer to b is')
	print('Future value of compounding continuously is ' + str(fv_con))
	print('The answer to c is')
	print('The number of items in the math library is ' + str(len(dir(math))))

def question_3():
	x = 'abc'
	L = 1, 2, 3
	print('For question 3')
	print('The answer to a is')
	print('identity: ' + str(id(x)))
	print('type: ' + str(type(x)))
	print('value: ' + str(x))
	print('The answer to b is')
	print('The third one actually create a tuple because a tuple has to contain a sequence of values even when the length of the sequence is one')
	print('The answer to c is')
	print('No it does not. The data type of variable L is ' + str(type(L)))
	print('The answer to d is')
	print('The first line of code means a list variable of length 1 called L is created')
	print('The second line of code performs a slicing operation on L in the first position')

def question_4():
	sum = 0
	for i in range(1, 101):
		sum = sum + i
	print('For question 4')
	print('The answer to a is')	
	print('Whether the task requires a condition to be satisfied or a number of iterations to be satisfied will be the criterion to select which loop to use')
	print('The answer to a i is')
	print('For loop is used when a index variable is required in the computation and a specified number of iterations need to be achieved')
	print('While loop is used when a certain condition needs to be satisfied before the iterative process stops')
	print('The answer to a ii is')
	print('Yes it is correct')
	print('The answer to b is')
	print('The sum is ' + str(sum))
	print('The answer to d is')
	print('Nothing gets printed because the list contains only null')
	
def main():
	question_1()
	question_2()
	question_3()
	question_4()





if __name__ == '__main__':
	main()
