# ejercicio 1

import random

"""Crear un algoritmo donde se solicite dos matrices por consola. Tanto la cantidad de columnas
como de filas, deben ser ingresadas por teclado. Los elementos de las matrices deben ser
generados de forma aleatoria (0 al 5). Estas dos matrices se deben sumar. Luego se solicita
una tercera matriz. Al igual que las dos anteriores, se ingresan columnas y filas por consola, y
sus elementos son generados aleatoriamente (0 a 5). Esta última matriz se restará con la
matriz resultante entre la operación de suma.
"""
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
matriz_resultante=[[matriz1[i][j] + matriz2[i][j] for j in range(columnas1)] for i in range(filas1)]
print("la matriz resultante de la suma es: ", matriz_resultante)

#con la matriz resultante, le restamos una tercera matriz ingresada por el usuario
columnas3= int(input("ingrese numero de columnas de la Matriz 3: "))
filas3=int(input("ingrese numero de filas de la Matriz 3: "))

#generando aleatoriamnete los elementos de la matriz 3
matriz3 = [[random.randint(0,5) for j in range(columnas3)] for i in range(filas3)]
print("la matriz 3 ingresada por el usuario es: ",matriz3)

#restando la matriz resultante con la matriz 3
matriz_resta=[[matriz1[i][j] - matriz2[i][j] for j in range(columnas1)] for i in range(filas1)]
print("la matriz resultante de la resta es: ", matriz_resta)



print("---------------------------------------------------------")


#ejercicio 2

"""Crear una matriz la cual se debe solicitar por teclado la cantidad de filas y columnas que va a
contener. También ingresar por consola un escalar. Los elementos de la matriz deben ser
generados aleatoriamente (0 al 10). Por último, se debe multiplicar la matriz generada por el
escalar ingresado.
"""
#ingresar filas,columnas y escalar de la matriz 1
columnas2= int(input("ingrese numero de columnas de la Matriz 1: "))
filas2=int(input("ingrese numero de filas de la Matriz 1: "))
escalar=int(input("ingrese el numero escalar: "))

#generando aleatoriamente los elementos de la matriz
matriz1_5 = [[random.randint(0,10) for j in range(columnas1)] for i in range(filas1)]
print("la matriz resultante es : ", matriz1_5)

#multiplicando el escalar por la Matriz 1_5
matriz_multiplicacion=[[escalar * matriz1_5[i][j] for j in range(columnas2)] for i in range(filas2)]

print("el resultado de la multiplicacion de un escalar por una matriz es: ", matriz_multiplicacion)