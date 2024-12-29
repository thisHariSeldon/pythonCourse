# it's a more advanced kind of data, and uses a special logic
# it can ONLY have to values: TRUE (1) FALSE (0)

booleanT = True  # note that this value is "reserved" in python, and it indicates that it is a boolean
booleanF = False
print(type(booleanT))

# they must be writen just like that, capitalized

'''
Truthy Values:
Non-empty strings: 'r', 'hello'
Non-zero numbers: 1, -1, 3.14
Non-empty collections: [1, 2, 3], { 'key': 'value' }, (1,)
Other objects (e.g., instances of a class)

Falsy Values:
Empty strings: ''
Numbers equal to zero: 0, 0.0
Empty collections: [], {}, ()
None
False
'''

# -------------------- RELATIONAL (comparison) OPERATORS ---------------------
# They are used to compare two values and return a Boolean value (True or False)

'''
==	Equal to	
!=	Not equal to	
>	Greater than	
<	Less than	
>=	Greater than or equal to	
<=	Less than or equal to	
'''
# if we mix them with conditionals, then the relational operators happen to be CONDITIONS

number1 = 500
number2 = 500
string1 = 'K pasa perro'
string2 = 'Whatup dawg'

print(number1 > number2) # False
print(number1 < number2) # False
print(number1 >= number2) # True
print(number1 <= number2) # True
print(number1 == number2) # True
print(number1 != number2) # False

print(string1 == string2) # False
print(string1 != string2) # True

print(string1 > string2)
print(string1 < string2)

print(string1.count())

# -------------------- LOGICAL OPERATORS ---------------------
# They are used to combine MULTIPLE conditions (Boolean expressions) and return a Boolean value (True or False) based on their logic. 
# They are often used in conjunction with relational operators for more complex decision-making.
'''
and	Returns True if both conditions are True.
or	Returns True if at least one condition is True.	
not	Reverses the Boolean value. - not (5 > 3) False
'''

#METHODS
# .startswith('x') Si empieza por ese charact
# .endswith('x')   Si finaliza por ese charactz
# .isupper()
# .islower() 