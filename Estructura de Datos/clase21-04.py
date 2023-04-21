import random


# Crear un arreglo y ordenarlo de forma descendente

lista= [7, 2, 9, 1, 6, 3]

# Ordenar el arreglo con metodo sort()
# True para ordenarlo de forma descendente 
# False para ordenrlo de forma ascendente

lista.sort(reverse=True)

# Mostrar el arreglo ordenado
print("lista de forma descendente",lista)



#crear un arreglo de forma aleatoria
lista2= [24,25,15,76,43,64]

# la funcion random.shuffle ordena los valores de forma aleatoria
random.shuffle(lista2)

print("lista de forma aleatoria: ",lista2)


# Escribir un programa que pida al usuario una palabra y muestre por
# pantalla el número de veces que contiene cada vocal.

palabra= str(input("ingrese palabra :"))

vocales = "aeiou"

for vocal in vocales:
    contador = palabra.lower().count(vocal)
    print("La vocal", vocal, "aparece", contador, "veces en la palabra", palabra)


import array
# Crear un arreglo aleatorio de tamaño entre 10 a 30. Imprimir el arreglo
# creado y luego solicitar por consola la búsqueda de un elemento en
# específico del arreglo creado. Todo esto utilizando import array

import array
import random

# Creamos un arreglo aleatorio de tamaño entre 10 y 30
arreglo = array.array("i", [random.randint(0, 31) for _ in range(random.randint(10, 30))])

# Imprimimos el arreglo creado
print("Arreglo aleatorio:")
print(arreglo)

# Solicitamos por consola la búsqueda de un elemento en específico
busqueda = int(input("Ingresa un número a buscar en el arreglo: "))
if busqueda in arreglo:
    print("El número", busqueda, "se encuentra en el arreglo.")
else:
    print("El número", busqueda, "no se encuentra en el arreglo.")





