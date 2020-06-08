#To create a dictionary of all builtins with their explanation
#To store the document string of builtin modules as its value in dictionary 
# And key as the module name


import sys
import struct
'''
for keywords:
	import keyword
	keyword.kwlist
blt_ins = {}

for fns in dir(__builtins__):
	blt_ins[fns] = eval(fns).__doc__  
print(blt_ins['range'])
'''

#Python 2 version
def Interaction_module(clara_feedback,blt, args):
	print(blt +":- This is the function where you have gone wrong")
	print("Probably you might have passed incorrect values as parameter")
	print("Would you prefer having a quick glance at the explanation about the " + blt+"?")
	print("yes/no\n")
	reply_2 = input()
	if(reply_2 == 'no' or reply_2 == 'No' or reply_2 == 'NO'):
		sys.exit("Looks like you would be able to debug it now. Happy coding!")
	elif(reply_2 == 'yes' or reply_2 == 'Yes' or reply_2 == 'YES'):
		print("Here is the standard document string of "+blt +" method:\n")
		print(eval(blt).__doc__)
		print("\nIf finished reading, type yes")
		reply_3 = input()
		if(reply_3 == 'Yes' or 'yes' or 'YES'):
			print("If this reading was sufficient, would you like to debug on your own?")
			print("yes/no")
			reply_4 = input()
			if(reply_4 == 'no' or reply_4 =='No' or reply_4 == 'NO'):
				print("We are providing you with the repair feedback generated, please analyse it and try reading it from prescribed reference books\n")
				print(clara_feedback,"\n")
			elif(reply_4 == 'yes' or reply_4 == 'Yes' or reply_4 == 'YES'):
				sys.exit("Never Give Up!!!")
