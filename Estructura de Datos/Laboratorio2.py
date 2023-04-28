
# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# se debe añadir uno por uno los elementos de ambas matrices. Luego se deben sumar
# estas matrices en una función, y en otra función restarlas. Solo utilizando las funciones
# de la biblioteca numpy
print("EJERCICIO 1")
"importando biblioteca"
import numpy as np

#pedir al usuario que ingrese las columnas y filas de la 1ra matriz 
columnas1= int(input("ingrese numero de columnas de la Matriz 1: "))
filas1=int(input("ingrese numero de filas de la Matriz 1: "))

# Creamos la primera matriz y le pedimos al usuario que ingrese sus elementos
print("Ingrese los elementos de la primera matriz:")
matriz1 = np.array([list(map(int, input().split())) for _ in range(filas1)])

# Creamos la segunda matriz y le pedimos al usuario que ingrese sus elementos
print("Ingrese los elementos de la segunda matriz:")
matriz2 = np.array([list(map(int, input().split())) for _ in range(filas1)])

# Sumamos las dos matrices y almacenamos el resultado en una tercera matriz
matriz_suma = matriz1 + matriz2
print("la matriz suma es :", matriz_suma)

# Restamos las dos matrices y almacenamos el resultado en una tercera matriz
matriz_resta = matriz1 - matriz2
print("la matriz resta es :", matriz_resta)









# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# los elementos de estas matrices deben ser aleatorios del 1 al 5, no se deben ingresar
# por consola. Luego se deben sumar en una función las matrices, y en otra función
# restarlas. En este caso no se puede utilizar numpy, solo estructuras propias de Python.

import random
print("EJERCICIO 2")

#pedir al usuario que ingrese las columnas y filas de la 1ra matriz 
columnas1= int(input("ingrese numero de columnas de la Matriz 1: "))
filas1=int(input("ingrese numero de filas de la Matriz 1: "))


print("en la matriz 1 hay",columnas1, "columnas, y", filas1, "filas.") 

#Generar aleatoriamente los elementos de las dos matrices.
matriz1 = [[random.randint(0,5) for j in range(columnas1)] for i in range(filas1)]
matriz2 = [[random.randint(0,5) for j in range(columnas1)] for i in range(filas1)]
print("la matriz 1 se compone de: ",matriz1)
print("la matriz 2 se compone de: ",matriz2)

#ya genrados los elementos de ambas matrizes, las sumamos y guardamos el resultado en una matriz resultante
matriz_suma=[[matriz1[i][j] + matriz2[i][j] for j in range(columnas1)] for i in range(filas1)]
print("la matriz resultante de la suma es: ", matriz_suma)

#ya genrados los elementos de ambas matrizes, los restamos  y guardamos el resultado en una matriz resultante
matriz_resta=[[matriz1[i][j] - matriz2[i][j] for j in range(columnas1)] for i in range(filas1)]
print("la matriz resultante de la suma es: ", matriz_resta)