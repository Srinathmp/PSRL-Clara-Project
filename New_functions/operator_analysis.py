#interactive feedback for operator errors
#Challenge to give a good explanation and reason behind the operator error occured, would like to look at 
#test case output for giving comparison between change in output with operator change
from New_functions.documenting import arithmetic_op, relational_op
#import sys

def feedback_comp_operator(segments, operator,clara_feedback,ins, args):
	op = operator.split(' (')[1].split(')')[0]
	if op in segments[0]:
		print("Looks like you have used an incorrect relational operator")
		print("Press 1 to know about relational operators, else press any key to continue\n")
		reply = input()
		if reply == '1':
			print("\n------------------------------------------------------------------------------------\n")
			print(relational_op.__doc__)
			relational_op()
			print("\n------------------------------------------------------------------------------------\n")
		print("The operator you have used is :", operator)
		print("Because of this the conditional expression is incorrectly evaluated and led to incorrect output")
		#provide better explanation for reason behind this
	else:
		print("There is a requirement for a comparison be performed between operands, for expression to be evaluated as True or False.")
		print("The relational operator required is :", operator)
	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = int(input())
	if (reply == 1):
		print("\nThe feedback generated is : ")
		print(clara_feedback, "\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0

def feedback_arth_operator(segments,operator,clara_feedback,ins, args): #depending on whether args passed or ins passed use accordingly
	op = operator.split(' (')[1].split(')')[0]																		#accordingly one of them will be None
	if op in segments[0]:
		print("Looks like you have used an incorrect arithmetic operator")
		print("Press 1 to know about arithmetic operators, else press any key to continue\n")
		reply = input()
		if reply == '1':
			print("\n------------------------------------------------------------------------------------\n")
			print(arithmetic_op.__doc__)
			arithmetic_op()
			print("\n------------------------------------------------------------------------------------\n")
		print("The incorrect operator used in program is :", operator)
	else:
		print("There is a requirement for an",operator,"operation to be performed")
	#provide better explanation for reason behind this
	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = int(input())
	if (reply == 1):
		print("\nThe feedback generated is : ")
		print(clara_feedback,"\n")
		print("****************************************************\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0

def feedback_logic_operator(segments, operator, clara_feedback,ins, args):
	if operator in segments[0]:
		print("Looks like you have used an incorrect logical operator")
		print("The incorrect operator used in program is :", operator)
	else:
		print("A logical operation is to be performed by the operator :",operator)
	#provide better explanation for reason behind this
	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = int(input())
	if (reply == 1):
		print("\nThe feedback generated is : ")
		print(clara_feedback,"\n")
		print("****************************************************\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0

def feedback_incorrect_value(n1, n2, clara_feedback,ins, args):
	print("Looks like you have used incorrect constant value")
	print("Literal :",n1,",might have been assigned to a variable or used as one of the operand")
	print("This might be one of the reason for incorrect output")
	print("It is suggested that you analyze the expression")
	#provide better explanation for reason behind this
	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = int(input())
	if (reply == 1):
		print("\nThe feedback generated is : ")
		print(clara_feedback,"\n")
		print("****************************************************\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0
