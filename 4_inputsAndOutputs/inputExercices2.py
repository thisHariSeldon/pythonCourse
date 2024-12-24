# ----------------EXERCISE 1
'''
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''
lowVocal = input('Please insert your favourite vocal in lower case: ')
upperLetter = input('Please insert your favourite letter in upper case: ')

print(lowVocal.upper(), upperLetter.lower())

# ----------------EXERCISE 2
'''
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
'''

name = input('Tell me ur name: ')
age = int(input('Tell me ur age: '))
gender = input('Tell me ur gender: ')

print(f'Te llamas: {name}\nTu edad es: {age}\nEres: {gender}')
