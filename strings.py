t = """ I Love Varun Kacholia and we are together now. We both are kidish sometimes and mature as well !!!! """

### To find out the length of the string

print("Length of the given string", t,  "is: \t", len(t))

#### Strings as an Array

print(t[3: 8])

print(t[-101:])

#### Looping through a Strings

for i in t:
    print(i, end = "") # It will print each character at a time on a single line if we don't use end parameter.

#### String Methods

### Upper method is used to capitalize each letters in the string.

print("\n", t.upper())

### Lower method is used to lower each letters in the string.

print("\n", t.lower())

### Strip method removes any white spaces before and after the string!

print("\n", t.strip())

### Rstrip removes Trailing characters.

print(t.rstrip(" !"))

#### The replace() method replaces all occurences of a string with another string.

print(t.replace("kidish", "emotional"))

#### The split() method splits the given string at the specified instance and returns the separated strings as list items.

print(t.split(" !"))

#### The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

print(t.capitalize()) # if first character is already capitalized then it will toggle the case.

#### The center() method aligns the string to the center as per the parameters given by the user.

print(t.center(155))

print(t.center(155, "-"))

#### The count() method returns the number of times the given value has occurred within the given string.

print(t.count("e"))

#### The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

print(t.endswith("!!!"))

print(t.endswith(" !!!! "))

#### We can even also check for a value in-between the string by providing start and end index positions.

print(t. endswith("Varun", 5, 13))

# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

print(t.find("we"))

# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

print(t.find("Wel"))

# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

print(t.index("we"))

# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# print(t.index("Wel"))

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

print(t.isalnum())

print("HelloAlexa123".isalnum())

# The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

print(t.isalpha())

print("HelloAlexa".isalpha())

# The islower() method returns True if all the characters in the string are lower case, else it returns False.

print(t.islower())

print(t.lower().islower())

# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

print(t.isprintable())

print("***##&&^^^^". isprintable())

# The isspace() method returns True only and only if the string contains white spaces (using Spacebar, using Tab), else returns False.

print(t.isspace())
y = t[2] + "    "
print(y.isspace())

# The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False.

print(t.istitle())

# The isupper() method returns True if all the characters in the string are upper case, else it returns False.

print(t.upper().isupper())

# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.

print(t.startswith("I"))

print(t.startswith(" I"))

# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

print(t.endswith("!!!!"))

print(t.endswith("!!!! "))

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

print(t.swapcase())

# The title() method capitalizes each letter of the word within the string.

print(t.title())

print(t.title().istitle())

