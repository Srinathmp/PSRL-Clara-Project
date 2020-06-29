#Effective detailed ift feedback implementation, prettify ift
#also provide comparison for some test case between correct implementation output and incorrect implementation output

import sys
from New_functions.documenting import conditional_statement, ift_explanation, boolean
from Documentation.doc_testing import if_statement_func, else_statement_func
from Documentation.python_doc_testing import if_statement_func, else_statement_func, elif_statement_func, python_nested_if_statements_func

def ift_feedback(clara_feedback,cleaned_feedback, ins,args, lang):
	print("1 : Brief explanation\n")
	print("2 : Detailed complete explanation\n")
	print("3 : To look at repair directly\n")
	print("Enter the option number from above for kind of explanation, else any other key to continue : ")
	reply = input()
	reply_1 = '0'
	if reply == '1':
		print("\n------------------------------------------------------------------------------------\n")
		print(ift_explanation.__doc__)
		ift_explanation()
		print("To know what is conditional statement, press 1, else press any number to continue\n")
		reply_1 = int(input())
		if reply_1 == 1:
			print(conditional_statement.__doc__)
			conditional_statement()
		print("\n------------------------------------------------------------------------------------\n")
		print("Press 1 if you need detailed explanation, else press any key to continue\n")
		reply_1 = input()
	if reply == '2' or reply_1 == '1':
		if lang == 'c':
			print("\n---------------------------------------------------------------------------------------------------\n")
			if_statement_func()
			print("\n\n***Continue reading about else keyword***\n\n")
			else_statement_func()
			print("\n---------------------------------------------------------------------------------------------------\n")
		elif lang == 'py':
			print("1 : IF statements")
			print("2 : ELSE statements")
			print("3 : ELIF statements")
			print("4 : Nested IF statements")
			print("Choose one of the options from above, to continue reading about it, else press 0 to quit reading :")
			try:		
				choice = int(input())
				while(choice):
					print("\n---------------------------------------------------------------------------------------------------\n")
					if choice == 1:
						if_statement_func()
					elif choice == 2:
						else_statement_func()
					elif choice == 3:
						elif_statement_func()
					elif choice == 4:
						python_nested_if_statements_func()
					else:
						print('Invalid choice, choose one from above options')
					print("Select choice to further continue reading, else 0 to quit\n")
					choice = int(input())
					print("\n---------------------------------------------------------------------------------------------------\n")
			except exception as err:
				print("Exception arosed is :", err)

	if reply == '3':
		print(cleaned_feedback,"\n")
		print("****************************************************\n")
		return 

	print("Press 1 to look at repair generated, else 0 to exit\n")
	reply = int(input())
	if reply == 1:
		print(cleaned_feedback,"\n")
		print("****************************************************\n")
	elif reply == 0:
		print("*** Happy Coding!!! ***\n")
		return 0

def incorrect_conditional_exp(clara_feedback, ins, args):
	print("\nLooks like you have used incorrect conditional expression.\n")
	print("**To know what is conditional expression in brief press 1, else press 0 to exit**\n")
	reply = int(input())
	if reply == 0:
		print("*** Happy Coding!!! ***\n")
		return reply
	elif reply == 1:
		print("----------------------------------------------------------------------\n")
		print(conditional_statement.__doc__)
		conditional_statement()
		print("To know about what is boolean, press 1, else press any key to continue\n")
		reply = input()
		if reply == '1':
			print(boolean.__doc__)
			print("\n----------------------------------------------------------------------\n")
			boolean()
		else:
			return
