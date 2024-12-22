# Un lenguaje compilado es aquel que su codigo primero se traduce a lenguaje maquina y luego se ejecuta
# Un lenguaje interpretado necesita un tercer programa para ponerse en marcha. En este caso el propio Visual Code

print("Hi there my little muggots")

# ------------ VARIABLES ----------------
# Las variables son espacios reservados de almacenamiento, a los que se le asignan DATOS
# Las variables NO inician con numeros.
# No puede llevar caracteres especiales como ñ o @, ni guiones ni ser palabras separadas
# No pueden llevar el nombre de palabras resrvadas de lenguaje, por ejemplo "print"
# VARIABLE: Un espacio en memoria momentaneo con nombre y valor asignado
# syntax -- <name of the variable> = <value>


# ---------- DATOS --------
# Son la forma mínima de un programa, hay 3 principales (aunque no son los unicos)
# Integers (enteros): no tienen parte decimal
# Float (flotante): los que tienen decimales, como el pi, 3,1416
# String (cadena de texto): Conjunto de varios caracteres de texto

#%%
name = 'Hari Seldon'
age = 24
float = 3.14 # must be '.' and not ',' otherwise it is a separator and the class would be 'tuple'

print(type(float))  #what type of data is the variable?
print([type(name), type(age)]) # type just allows one parameter so we have to convert it into a list []

print('My name is', name, 'and I am', age, 'years young ;)') 

#%%
import keyword # esto es una libreria de python
#<kwlist> throws the list of all those words that can't be used as variables as they are python functions
print(keyword.kwlist)