#interactive feedback for operator errors
#Challenge to give a good explanation and reason behind the operator error occured, would like to look at 
#test case output for giving comparison between change in output with operator change

import sys

def feedback_comp_operator(segments, operator,line_no, clara_feedback,ins, args):
	print("Looks like you have used an incorrect comparison operator")
	print("The operator you have used is :", operator, ",at line number :", line_no)
	print("Because of this the conditional expression is incorrectly evaluated and led to incorrect output")
	#provide better explanation for reason behind this
	print("Do you wanna look at the repair generated")
	print("yes/no")
	reply = input()
	if(reply == 'no' or reply == 'No' or reply == 'NO'):
		sys.exit("Looks like you would be able to debug it now. Happy coding!")
	else:
		print("The feedback generated is : ")
		print(clara_feedback, "\n")

def feedback_arth_operator(segments,operator,line_no,clara_feedback,ins, args): #depending on whether args passed or ins passed use accordingly
	print("Looks like you have used an incorrect arithmetic operator")			#accordingly one of them will be None
	if operator in segments[0]:
		print("The incorrect operator used in program is :", operator, ",at line number :", line_no)
	else:
		print("There is a requirement for an operation to be performed by operator :",operator,",at line number :", line_no)
	#provide better explanation for reason behind this
	print("Do you wanna look at the repair generated")
	print("yes/no")
	reply = input()
	if(reply == 'no' or reply == 'No' or reply == 'NO'):
		sys.exit("Looks like you would be able to debug it now. Happy coding!")
	else:
		print("The feedback generated is : ")
		print(clara_feedback, "\n")

def feedback_logic_operator(segments, operator, line_no, clara_feedback,ins, args):
	print("Logical operator error : ", operator)


def feedback_incorrect_value(n1, n2, line_no, clara_feedback,ins, args):
	print("Looks like you have used incorrect constant value, at line number :", line_no)
	print("Literal :",n1,",might have been assigned to a variable or used as one of the operand")
	print("This might be one of the reason for incorrect output")
	print("It is suggested that you analyze the expression")
	#provide better explanation for reason behind this
	print("Do you wanna look at the repair generated")
	print("yes/no")
	reply = input()
	if(reply == 'no' or reply == 'No' or reply == 'NO'):
		sys.exit("Looks like you would be able to debug it now. Happy coding!")
	else:
		print("The feedback generated is : ")
		print(clara_feedback, "\n")