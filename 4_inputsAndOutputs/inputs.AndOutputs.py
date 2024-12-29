'''
# most of the time we code we intend that the user inputs something, in order to collect data
# 1) we need to know what type of data the input is going to be, if not, there's gonna be a conflict
# 2) input data will be attached to a variable, meaning that the value of the variable will be the user's input
# 3) when manipulating this data, we have to be careful cause the type of data of this input may vary over time
'''
# when the input is a string type, we don't need to be claryfying the type of data, an input will be STR by DEFAULT
name = input('Insert your name: ') # this bluit-in function will recognize a 'entrada por teclado'

# when talking about number we indeed have tu specify if it's a INT or a FLOAT
# note: the 'int()' goes outside the 'input()'
age = int(input('Insert your age: '))
print(name)
print(age)

# if we input another type different to which it is specificated, we get an error


# ---------------------- CLASS 31 - OUTPUTS ------------
name2 = input('What\'s your name:')
age2 = int(input('What\'s yor age:'))

print('What up', name2,'\b. So you\'r', age2, 'uh? ;)') # I thought about puting the \b as there is a unwanted space previous to the dot.

# format
print(f'Hi {name2}, so you say you are {age2} years old uh?') # we put the 'f' from format
print('Hi {}, so you say you are {} years old uh?'.format(name2, age2)) # instead of the f we call the .format() method with the variables we want

#the difference between a method and an attribute:
'''
Method: A function associated with an object that can perform actions on it.
    Example: .format() modifies the content of a string or creates a new formatted string.
Attribute: A property of an object that stores data.
    Example: Strings do not have many attributes, but objects like lists and classes often do.
'''
