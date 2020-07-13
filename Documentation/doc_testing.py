# from Documentation.c_documentation import if_statement
# from Documentation.c_documentation import else_statement
# from Documentation.c_documentation import array_doc
from Documentation.c_documentation import *
import sys
### Using google text to speech
from gtts import gTTS
import os

def if_statement_func():
	speak = "The brief definition of if is."
	speak += if_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about if statement ?')
	print('The subcategories available are :')
	dict_keys = list(if_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in IF that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",if_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def else_statement_func():
	speak = "The brief definition of else statement is."
	speak += else_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about else statement ?')
	print('The subcategories available are :')
	dict_keys = list(else_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in ELSE that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",else_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

def array_doc_func():
	speak = "The brief definition of array data structure is."
	speak += array_doc['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about array  ?')
	print('The subcategories available are :')
	dict_keys = list(array_doc.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in array that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",array_doc[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')


def for_loop_func():
	speak = "The brief definition of for loop expression is."
	speak += for_loop['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about for loop ?')
	print('The subcategories available are :')
	dict_keys = list(for_loop.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in FOR loop that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",for_loop[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def while_loop_func():
	speak = "The brief definition of while loop expression is."
	speak += while_loop['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about while loop ?')
	print('The subcategories available are :')
	dict_keys = list(while_loop.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in while loop that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",while_loop[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
	

def break_and_continue_func():
	speak = "The brief definition of break and continue keywords are."
	speak += "Defintion of Break."
	speak += break_and_continue['definition of break']
	speak += "Now providing definition of continue"
	speak += break_and_continue['Defintion of continue']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about break and continue ?')
	print('The subcategories available are :')
	dict_keys = list(break_and_continue.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",break_and_continue[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def return_func():
	speak = "The brief definition of return expression is."
	speak += return_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	os.system("mpg321 wit_bot.mp3")

	print('What would you like to know about return statements?')
	print('The subcategories available are :')
	dict_keys = list(return_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in return that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",return_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')