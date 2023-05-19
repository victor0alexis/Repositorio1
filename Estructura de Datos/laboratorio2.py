#ejercicio 1

# Crear dos matrices donde la cantidad de filas y columnas deben ser generadas de
# forma aleatoria (de 2 a 5). Los elementos de estas matrices deben ingresarse por
# teclado. Luego se deben restar estas matrices, solamente utilizando elementos
# propios de Python (no se permite uso de librerías).

# La matriz resultado de la resta anterior se debe multiplicar por una nueva matriz,
# la que debe tener las dimensiones acordes para realizar la multiplicación entre
# ambas matrices. Esta matriz se debe ingresar por teclado tanto la cantidad de
# filas y columnas como sus elementos. Se permite el uso de la librería numpy.

#impotando random
import random
#impotando numpy
import numpy as np

# filas y columnas aleatorias de matriz 1
filas = random.randint(2, 5)
columnas = random.randint(2, 5)

# primera matriz
print("Ingrese los elementos de la matriz 1:")
matriz1 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz1.append(fila)
print("la matriz 1 se compone de: ", matriz1)

# segunda matriz
print("Ingrese los elementos de la matriz 2:")
matriz2 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz2.append(fila)
print("la matriz 2 se compone de: ", matriz2)

# Restar las matrices
matriz_resta = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = matriz1[i][j] - matriz2[i][j]
        fila.append(elemento)
    matriz_resta.append(fila)

print("la matriz resultante de la resta es :",matriz_resta)


#multiplicar matris resta con nueva matriz generada

print("---------------------------------------")
print("la matriz resta es: ",matriz_resta)

# nueva matriz para multiplicar
filas_nueva = int(input("Ingrese el número de filas de la nueva matriz: "))
columnas_nueva = int(input("Ingrese el número de columnas de la nueva matriz: "))
matriz_nueva = []
for i in range(filas_nueva):
    fila = []
    for j in range(columnas_nueva):
        elemento = int(input(f"Ingrese el elemento de la nueva matriz ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz_nueva.append(fila)

# Multiplicar la matriz resultado por la nueva matriz utilizando NumPy
resultado_multiplicacion = np.dot(matriz_resta, matriz_nueva)

# resultado de la multiplicación
print("el resultado de la multiplicacion es: ",resultado_multiplicacion)

# propiedad matrices transpuestas
traspuesta_resta = matriz_resta
traspuesta_nueva = matriz_nueva
producto_traspuestas = np.dot(traspuesta_nueva, traspuesta_resta)

# Imprimir el resultado de la propiedad de las matrices traspuestas
print("El resultado de la propiedad de las matrices traspuestas es:", producto_traspuestas)
