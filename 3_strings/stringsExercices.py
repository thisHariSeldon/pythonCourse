'''
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

'''
friendzone = 'Te quiero solo como amigo'

fisrt2 = print(friendzone[0:2]) # remember the last given character is not counted
last3 = print(friendzone[-3:]) # from -3 to the end (3 last)
each2 = print(friendzone[::2]) # each 2 steps
inverse = print(friendzone[-1::-1]) # from the end to the begining with a -1 step, it could also be 'friendzone[::-1]'
print(type(inverse)) # this is None because we are assingning 'inverse' to a PRINT value, and not to the value irself

inverse = friendzone[-1::-1] # Now this can be concatenated ad they are two STR and not a None value
bothInvAndNormal = print(friendzone + inverse)

# Note: print() displays a value but returns None !!!! NEVER assing a print to a variable:
first2 = friendzone[0:3]  
last3 = friendzone[-3:]    
each2 = friendzone[::2]   
inverse = friendzone[-1::-1]  