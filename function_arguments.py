'''
Function Arguments and return statement
There are four types of arguments that we can provide in a function:

1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments

Default Arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Example:

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
Output:

Hello, Amy Jhon Whatson
Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Example:

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
Output:

Hello, Jade Peter Wesker
Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

Example 1: when number of arguments passed does not match to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
Output:
name("Peter", "Quill")\

TypeError: name() missing 1 required positional argument: 'lname'

Example 2: when number of arguments passed matches to the actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
Output:
Hello, Peter Ego Quill

Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Example:

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

Output:
Hello, James Buchanan Barnes

Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Example:

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

Output:
Hello, James Buchanan Barnes

return Statement
The return statement is used to return the value of the expression back to the calling function.

Example:

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
Output:

Hello, James Buchanan Barnes

'''

########################################### Default Arguments ###########################################

global hashtag_list

# function to print all the hashtags in a text
# def extract_hashtags(text1, text2, text3):

def extract_hashtags(*texts):
	
	text = texts[0] + texts[1] + texts[2]
	
	hashtag_list = []
	
	for word in text.split():
		# checking the first character of every word
		if word[0] == '#':

			# adding the word to the hashtag_list
			hashtag_list.append(word[1:])
			
	return hashtag_list
			

	


if __name__ == "__main__":
	
	text1 = " GeeksforGeeks is a wonderful #website #ComputerScience "
	text2 = " This day is beautiful ! #instagood #photooftheday #cute "
	
	# Keyword Arguments
	
	# extract_hashtags(text2 = "Varun K is Angry Man with mixed emotions #emotional #angryman #intelligent", text3 = "Varun K is childish at some places with professional ethics #professional #childish", text1 = "Whatever Varun is I Love him and especially his mood when he try to get angry #loveyouVarun #loveyourinnocentsmile")

    #Default Arguments
	
	# extract_hashtags(text1, text2, "Varun K is eating up my mind!!!! #mindeater #littlebitcrazy")
	
    # extract_hashtags(text1, text2, " Varun K is eating up my mind!!!! #mindeater #littlebitcrazy")
	
    # Arbitary Arguments
	
	hashtag_list = extract_hashtags(" Varun K is Angry Man with mixed emotions #emotional #angryman #intelligent ", " Varun K is childish at some places with professional ethics #professional #childish ", " Whatever Varun is I Love him and especially his mood when he try to get angry #loveyouVarun #loveyourinnocentsmile ")
	
    # printing the hashtag_list
	print("The hashtags in \""  + "\" are :")
	for hashtag in hashtag_list:
		print(hashtag)


	# extract_hashtags(text2)
	

