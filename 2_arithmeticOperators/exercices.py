# EXERCICE 1
sum = 3 + 2
mult = 2 * 5
div = sum / mult
operation1 = div ** 2

print(operation)
#or
operation2 = ((3 + 2) / (2 * 5)) ** 2
print(operation)
#we can also use pow(), it uses base, power, ie:
print(pow(5,2)) #this would be 5 to the 2nd power
operation3 = pow(div,2)
print(operation3)


#EXERCICE 2 (When the string or title of the exercice is too long to see it, we can prees Alt + z, that divides the paragraph into smaller lines)
'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística
les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa
que muestre el peso total de toda la venta.
'''

# peso de cada paquete??
pesoPayaso = 112
pesoMuneca = 75

pesoPaquete = (pesoPayaso * 23) + (pesoMuneca * 54)
pesoPaqueteKG = pesoPaquete / 1000
print('The total package weight is', pesoPaquete, 'grams, or', pesoPaqueteKG, 'kilos.')

# It would have been a better practice if cantidadPayasos was  avariable instead of putting the number raw just like that
# Actully the weight IS NOT VARIABLE, he variable is the QUANTITY, so it would had have to be inverted
