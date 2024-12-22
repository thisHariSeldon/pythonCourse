# In python there is either INTEGERS or FLOATS, unlike other languages that might have many more

num1 = 40
num2 = 99.99

# if we use python built-in functions like float() or int() it returns a flot or int value WITHOUT affecting the origianl variable or value
print(float(num1))
print(type(num1)) # the type is still an integer

print(int(num2)) # it does not round it, just removes the decimal part
print(type(num2)) # the type is still a float 

print(type(float(num1))) # this indeed would be float

# %% ----------------------------------------------------------------
''' 
+ suma
- resta
*multiplicacion
/ division
** exponienciacion
// division entera : una division solo nos da la parte entera del cociente, sin decimales

ORDEN DE OPERACIONES
De izquierda a derecha
1) Los parentesis
2) Los exponentes
3) Multiplicacion y division
4) Suma y resta
'''

