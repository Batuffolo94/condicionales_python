# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from cgitb import text


texto_1 = str(input('Ingrese la primera palabra:\n').lower())

texto_2 = str(input('Ingrese la segunda palabra:\n').lower())

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2: 
    print (f"{texto_1} es mayor alfabeticamente a {texto_2}.")
elif texto_2 > texto_1:
    print (f"{texto_2} es mayor alfabeticamente a {texto_1}.")
else:
    print ("se ingreso la misma palabra ")

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(f"{texto_1} tiene mayor cantidad de letras a {texto_2}.")
elif len(texto_2) > len(texto_1):
    print(f"{texto_2} tiene mayor cantidad de letras a {texto_1}.")
else:
    print(f"{texto_1} y {texto_2} tienen la misma cantiad de letras")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

#variables que representan la primera letra de cada palabra
primera_letra_texto_1 = texto_1 [0]
primera_letra_texto_2 = texto_2 [0]

if primera_letra_texto_1 > primera_letra_texto_2: 
    print(f"la primera letra de {texto_1} es mayor que la primera letra del {texto_2}.")

elif primera_letra_texto_2 > primera_letra_texto_1:
    print(f"la primera letra de {texto_2} es mayor que la primera letra del {texto_1}.")

else: 
    print (f"la primera letra de {texto_1} es igual que la primera letra del {texto_2}.")



copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print (f"se verifica que {copia_texto_1} es igual a {texto_1}.")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_1:
    print (f"se verifica que {copia_texto_1} es distinto a {texto_1}.")