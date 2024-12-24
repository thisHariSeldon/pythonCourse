# EXERCISE 1
'''
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''
# FORMULA: x = ((-b +- math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
# as we see in the formula there's a +- sign. Thta is why there is two x (x1 and x2) depending on if ur adding or substracting

# we just use float as a float covers also integers (e.g 25)
a = float(input('Insert value of a: '))
b = float(input('Insert vale of b: '))
c = float(input('Insert vale of c: '))
x1 = 0
x2 = 0

print(a, b, c)

# gotta ask for math libary (a bunch of prefabricated code with its own functions)
import math 
# print(sqrt(100))  this brings up an erros cuase we gotta specify the FULL name (math.sqrt)
print(math.sqrt(100)) # if we just wanna say sqrt() we have to 'from math import sqrt'

# the square root of a negative number is an IMAGINARY number, thats why we need to use "if" in this equation
# no se por que da invalid syntax con el else????? indentacion???
if ((b ** 2) - (4 * a * c)) < 0:
    print('Cannot square root a negative number')
else:
    x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
print('The solution is', x1, 'and', x2)

# EXERCISE 2
'''
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
'''
P1 = float(input("First practice grade: "))
P2 = float(input("Second practice grade: "))
P3 = float(input("Third practice grade: "))

EP = float(input("Partial exam grade: "))
FE = float(input("Final exam grade: "))

PP = (P1 + P2 + P3) / 3 # promedio practicas
print(PP)

PROM = round((PP + 2*EP + 3*FE) / 6, 2)
print('Your total score for this matter is:\n ', PROM )