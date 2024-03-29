'''
Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:
def function_name(parameters):
  pass
  # Code and Statements
Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
Any parameters and arguments should be placed within the parentheses.
Rules to naming function are similar to that of naming variables.
Any statements and other code within the function should be indented.
Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

Example:

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
Output:

Hello, Sam Wilson

'''

def sum(a, b):
    return a + b

print("Sum of 2 numbers is:", sum(5, 10))