from Documentation.python_documentation import if_statement
from Documentation.python_documentation import else_statement
from Documentation.python_documentation import elif_statement
from Documentation.python_documentation import python_nested_if_statements
from Documentation.python_documentation import range_function
from Documentation.python_documentation import break_and_continue_statements_and_else_clauses_on_loops
from Documentation.python_documentation import while_loop
from Documentation.python_documentation import for_loop
from Documentation.python_documentation import list_doc
import sys
def if_statement_func():
	print('What would you like to know about if statement ?')
	print('The subcategories available are :')
	dict_keys = list(if_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in IF that you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",if_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

#if_statement_func()

def else_statement_func():
	print('What would you like to know about else statement ?')
	print('The subcategories available are :')
	dict_keys = list(else_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in ELSE that you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",else_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

#else_statement_func()


def elif_statement_func():
	print('What would you like to know about elif statement ?')
	print('The subcategories available are :')
	dict_keys = list(elif_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in ELIF that you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",elif_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

# elif_statement_func()

def python_nested_if_statements_func():
	print('What would you like to know about nested if statement ?')
	print('The subcategories available are :')
	dict_keys = list(python_nested_if_statements.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in Nested IF that you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",python_nested_if_statements[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		
	sys.exit("\nHappy Coding!!!\n")

# python_nested_if_statements_func()
def range_function_func():
	print('What would you like to know about range function ?')
	print('The subcategories available are :')
	dict_keys = list(range_function.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",range_function[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')


# python_nested_if_statements_func()
def break_and_continue_statements_and_else_clauses_on_loops_func():
	print('What would you like to know about break and continue statements and else clauses on loops ?')
	print('The subcategories available are :')
	dict_keys = list(break_and_continue_statements_and_else_clauses_on_loops.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",break_and_continue_statements_and_else_clauses_on_loops[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def while_loop_func():
	print('What would you like to know about while loop ?')
	print('The subcategories available are :')
	dict_keys = list(while_loop.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",while_loop[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')


def for_loop_func():
	print('What would you like to know about for loop ?')
	print('The subcategories available are :')
	dict_keys = list(for_loop.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",for_loop[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
	
def list_doc_func():
	print('What would you like to know about list ?')
	print('The subcategories available are :')
	dict_keys = list(list_doc.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to continue to look at repair')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",list_doc[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		