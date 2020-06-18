# Storing brief explanation of type of logical error recognised by the feedback_analysis function
import pyttsx3

# initialisation 
engine = pyttsx3.init() 

def boolean():
	"""An expression which evaluates to either true or false is called a boolean expression.
Boolean expressions are used extensively in programming language constructs such as if-then-else commands and while loops.\n"""
	print("\nPress 1 for speech based explanation of above text, else press any key to continue\n")
	reply = input()
	if reply == '1':
		engine.say("An expression which evaluates to either true or false is called a boolean expression.") 
		engine.say("Boolean expressions are used extensively in programming language constructs such as if-then-else commands and while loops.") 
		engine.runAndWait() 

def conditional_statement():
	"""In computer science, conditional statements, conditional expressions and conditional constructs are features of a programming language.\n
This perform different computations or actions depending on whether a programmer-specified 'boolean' condition evaluates to true or false."""
	print("\nPress 1 for speech based explanation of above text, else press any key to continue\n")
	reply = input()
	if reply == '1':
		engine.say("In computer science, conditional statements, conditional expressions and conditional constructs are features of a programming language.") 
		engine.say("This perform different computations or actions depending on whether a programmer-specified 'boolean' condition evaluates to true or false.") 
		engine.runAndWait() 

def ift_explanation():
	"""The if-then-else statement is the most basic of all the control flow statements.\n 
It tells your program to execute a block of code under 'if' section of code only if condition specified in it evaluates to true,
otherwise the 'else' block of code is executed if condition specified evaluates to false.\n"""
	print("\nPress 1 for speech based explanation of above text, else press any key to continue\n")
	reply = input()
	if reply == '1':
		engine.say("The if-then-else statement is the most basic of all the control flow statements.")
		engine.say("It tells your program to execute a block of code under 'if' section of code only if condition specified in it evaluates to true,otherwise the 'else' block of code is executed if condition specified evaluates to false.")
		engine.runAndWait()

def return_explanation():
	"""In computer programming, a return statement causes execution to leave the current subroutine and resume at the point in the code immediately after the instruction which called the subroutine, known as its return address.
The return address is saved by the calling routine, today usually on the process's call stack or in a register. Return statements in many languages allow a function to specify a return value to be passed back to the code that called the function."""
	print("\nPress 1 for speech based explanation of above text, else press any key to continue\n")
	reply = input()
	if reply == '1':
		engine.say("In computer programming, a return statement causes execution to leave the current subroutine and resume at the point in the code immediately after the instruction which called the subroutine, known as its return address.")
		engine.say("The return address is saved by the calling routine, today usually on the process's call stack or in a register. Return statements in many languages allow a function to specify a return value to be passed back to the code that called the function.")
		engine.runAndWait()

def arithmetic_op():
	"""An operator is an indicator, a symbol that shows that some specific operation needs to be performed within a computer program.\n
The basic arithmetic operations are addition(+), subtraction(-), multiplication(*), division(/), and modulus(%) operator(associated with integers) which gives the remainder of two integers.\n"""
	print("\nPress 1 for speech based explanation of above text, else press any key to continue\n")
	reply = input()
	if reply == '1':
		engine.say("An operator is an indicator, a symbol that shows that some specific operation needs to be performed within a computer program.")
		engine.say("The basic arithmetic operations are addition(+), subtraction(-), multiplication(*), division(/), and modulus(%) operator(associated with integers) which gives the remainder of two integers.")
		engine.runAndWait()

def relational_op():
	"""An operator is an indicator, a symbol that shows that some specific operation needs to be performed within a computer program.\n
In computer science, a relational operator is a programming language construct or operator that tests or defines some kind of relation between two entities. These include numerical equality (e.g., 5 = 5) and inequalities (e.g., 4 ≥ 3).\n
The relational operators are often used to create a test expression that controls program flow. This type of expression is also known as a Boolean expression because they create a Boolean answer or value when evaluated.\n"""
	print("\nPress 1 for speech based explanation of above text, else press any key to continue\n")
	reply = input()
	if reply == '1':
		engine.say("An operator is an indicator, a symbol that shows that some specific operation needs to be performed within a computer program.")
		engine.say("In computer science, a relational operator is a programming language construct or operator that tests or defines some kind of relation between two entities. These include numerical equality (e.g., 5 = 5) and inequalities (e.g., 4 ≥ 3).")
		engine.say("The relational operators are often used to create a test expression that controls program flow. This type of expression is also known as a Boolean expression because they create a Boolean answer or value when evaluated.")
		engine.runAndWait()

def built_in(blt):
	engine.say(eval(blt).__doc__)
	engine.runAndWait()
