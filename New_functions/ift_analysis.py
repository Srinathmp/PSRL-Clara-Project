#Effective detailed ift feedback implementation, prettify ift
#also provide comparison for some test case between correct implementation output and incorrect implementation output

import sys
from New_functions.documenting import conditional_statement, ift_explanation, boolean

def ift_feedback(clara_feedback, ins,args):
	# print("Press 1 to know about if-then-else(represented as 'ift' here), else press any number to continue\n")
	print("\n------------------------------------------------------------------------------------\n")
	print(ift_explanation.__doc__)
	ift_explanation()
	print("To know what is conditional statement, press 1, else press any number to continue\n")
	reply = int(input())
	if reply == 1:
		print(conditional_statement.__doc__)
		conditional_statement()
	print("\n------------------------------------------------------------------------------------\n")
	print("Press 1 to look at repair generated, else 0 to exit\n")
	reply = int(input())
	if reply == 1:
		print(clara_feedback,"\n")
		print("****************************************************\n")
	elif reply == 0:
		sys.exit("*** Happy Coding!!! ***\n")

def incorrect_conditional_exp(clara_feedback, ins, args):
	print("\nLooks like you have used incorrect conditional expression.\n")
	print("**To know what is conditional expression in brief press 1, else press 0 to exit**\n")
	reply = int(input())
	if reply == 0:
		sys.exit("*** Happy Coding!!! ***\n")
	elif reply == 1:
		print("----------------------------------------------------------------------\n")
		print(conditional_statement.__doc__)
		conditional_statement()
		print("To know about what is boolean, press 1, else press any number to continue\n")
		reply = int(input())
		if reply == 1:
			print(boolean.__doc__)
			print("\n----------------------------------------------------------------------\n")
			boolean()
		else:
			return
