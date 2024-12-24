# ------------------ CLASS 21 - Strings -----------

# A string is a series of characters in between quotation marks, does not matter what the character is. 
# May be between "" or ''. The advantage of using '' instead of "" is that we can place quotes in between quotes:
 
string = 'He used to say his name was "Yaures" but that was just an achronomy'
print(string)

# escape CHARACTERS (string literal): they are meant to give strings a particular behaviour (\" x \")
stringEscape = "He used to say his name was \"Yaures\"."
print(stringEscape)

# raw strings (r prefix)
print(r"This is a raw string: \n will not create a new line.")
# \n this is a new line
print("This is NOT a raw string: \n it creates a new line underneath.")
# \t is a TAB
print("This is a tab \tas you can see")
# \b backspace (deletes previous character)
print('Hari \bSeldon')
# \f female icon (?)
print('Hari \f Seldon')
# \r retorno de carro (moves the cursor to the beginning of the current line, used in situations where you want to overwrite a line in the terminal)
print('Hari \r Seldon')
# \v varon icon (male)
print('Hari \v Seldon')


'''
\'	Single quote	'It\'s Python!'	It's Python!
\"	Double quote	"He said, \"Hello!\""	He said, "Hello!"
\\	Backslash	"This is a backslash: \\"	This is a backslash: \
\0	Null character	"Null\0Character"	NullCharacter
\uXXXX	Unicode character (16-bit)	"\u2764"	❤ (heart)
\UXXXXXXXX	Unicode character (32-bit)	"\U0001F600"	😀 (grinning face)
\N{name}	Named Unicode character	"\N{GREEK SMALL LETTER ALPHA}"	α
\xXX	Hexadecimal character (8-bit)	"\x48\x65\x6C\x6C\x6F"	Hello
'''

# ------------------ CLASS 22 - Strings and Arithmetics -----------
greetings = 'Hello human '
greetQuestion = 'How are you today?'
number = 17

#This is how we CONCATENATE (no longer a sum), there is no space in between
print(greetings + greetQuestion)
print(greetings + '\n' + greetQuestion)
print(greetings, greetQuestion) # yu can concatenate using ',' and using '+'

# We can multiply strings, but cannot divide them or substract them JUS ADD NAD MULTIPLY
print(greetings * 5)

# str() is a native function that transforms variables into strings
print(type(str(number)))

# ------------------ CLASS 23 - Substrings or STRING SLICING -----------
'''
[start:stop:step]
'''

substring = 'This is an example of substring (String Slicing)'

print(len(substring)) # len() counts also the spaces ' '.
print(substring[0]) # the character count starts from 0, so this returns character 'T'.
print(substring[47]) # len() = 48 but as it stars from 0, the last one would be character 47.
print(substring[0:48]) # when we say 'x:y' means rom x to y BUT y IS NOT INCLUDED (thats why we need to say 48 and not just 47)
print(substring[0:31])
print(substring[:]) # not writing the parameter = 0 or the end

print(substring[-10]) # negative paramter means that the count starts from the end
print(substring[-10: -16])  # this DON'T work cause the STEP is implicitly POSITIVE
print(substring[-10: -16: -1]) # this DOES WORK
print(substring[-16: -10: 1]) # this WORKS TOO
print(substring[: : -1]) # the string completely reversed
print(substring[-1]) # It starts from -1 when counting backwards as there is no -0!!

# ------------------ CLASS 24 - String METHODS -----------

'''
A string method BUILT-IN function that you can call on a string to perform specific operations or manipulations. These methods are designed to make common tasks involving strings easier, such as formatting, searching, splitting, or transforming them.
Methods tied to objects use .method(), but there is many more methods like @classmethod, @staticmethod or special methods/dunder methods/magic methods 
like __init__() or __str__()
'''

# CHARACTER METHODS (not their real name)

goal = ' be the motherfucking best one in this shit, and flex that MONEY'

# .lower() - every character to lowercase
print(goal.lower()) 
# .upper - every character to uppercase
print(goal.upper()) 
# .capitalize - first letter in uppercase
print(goal.capitalize())
# .title - each begging character is capitalized
print(goal.title())
# .swapcase - lowers to uppers and viceversa
print(goal.swapcase())
# .strip - removes any space that might be in the beggining or end of the string
print(goal.strip())
# .replace - replaces one word for another. The FIRST ARGUMENT must be the original string and the SECOND the replacement
print(goal.replace("motherfucking", "ultimate"))
# .count("o") - counts how many of that string there are
print(goal.count("o"))