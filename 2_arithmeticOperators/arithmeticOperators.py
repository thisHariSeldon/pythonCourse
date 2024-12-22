print(5 + 9)
print(98.7 - 15.33)
print(10 * 15)
print(75 / 9)
print(75 // 9) # we see that here we don't have the decimal part. This is a FLOOR division

# the MODULO (%) operator takes the REMAINDER de una division:
print(100 % 100) # this returns '0' as it is entera.
print(int(100 / 100)) # this returns '1'

print(2 ** 52) # exponential

# to put the result in scientific notation we can:
print(f"{2 ** 52:.5e}") # :.5e that "5" would be how many decimals we want before the "e" (which is 10 exponential)

# you CAN'T DO this
sciNot = 2 ** 52:.5e
print(f"{sciNot}")

# %% ----------------- CLASS 15th -------------
number1 = 10
number2 = 33.2

print(type(number1), type(number2))
print(number1 + number2)
print(number1 - number2)
print(number2 - number1)
print(number1 * number2)
print(number1 ** number2) #this is already in SCI NOTATION as the number is LAAARGE
print(number2 / number1)
print(number2 // number1)
print(type(number2 // number1)) # returns 'float' as one of the operator IS a FLOAT eventhough it's a floor division
print(number1 % number2) # MODULO 


sum = number1 + number2
print(sum)
exp = number1 ** number2
print(exp)
modulo = number1 % number2
print(modulo)

# %% ----------------- CLASS 16th: Operations HIERARCHY -------------

one = 100
two = 50
three = 25
four = 10

print((one + two) * (three - four)) # we are prioritazing the parenthesis here
print(type((one + two) * (three - four) / (one - four))) # in pyhton DIVISIONS are ALWAYS a FLOAT

print((one - two) / (four - four)) # four - four = 0 and division by zero is infinite, so this would be ERROR
