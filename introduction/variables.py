# VARIABLE: Un espacio en memoria momentaneo con nombre y valor asignado
# syntax -- <name of the variable> = <value>

name = 'Hari Seldon'
age = 24
float = 3.14 # must be '.' and not ',' otherwise it is a separator and the class would be 'tuple'

print(type(float))  #what type of data is the variable?
print([type(name), type(age)]) # type just allows one parameter so we have to convert it into a list []
print('My name is', name)
