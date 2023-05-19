// Crear tres listas:
// a. La primera lista debe tener los siguientes 5 elementos: [14,2,5,3,9]
// b. La segunda se debe ingresar por teclado (Debe tener 5 elementos
// enteros)
// c. La tercera lista igual debe contener 5 elementos, pero deben ser
// generados de forma aleatoria. (Solo números aleatorios negativos del
// -15 al -25)
// d. Restar la primera y segunda lista. La lista obtenida se suma con la
// tercera lista. Imprimir el resultado obtenido.
// e. Insertar en la primera y segunda posición de la lista que se obtuvo de la suma, los
// elementos 17 y 24.
// f. Por último ordenar de forma descendente la lista.


import 'dart:io';
import 'dart:math';

void main() {
  // a. Crear la primera lista con los siguientes elementos
  List<int> lista1 = [14, 2, 5, 3, 9];

  // b. La segunda se debe ingresar por teclado (Debe tener 5 elementos enteros)
  List<int> lista2 = [];
  print('Ingrese 5 elementos enteros para la segunda lista:');
  for (int i = 0; i < 5; i++) {
    int elemento = int.parse(stdin.readLineSync()!);
    lista2.add(elemento);
  }

  // c. La tercera lista igual debe contener 5 elementos, pero deben ser
// generados de forma aleatoria. (Solo números aleatorios negativos del
// -15 al -25)
  List<int> lista3 = [];
  Random random = Random();
  for (int i = 0; i < 5; i++) {
    int elemento = random.nextInt(11) - 15;
    lista3.add(elemento);
  }

  // d. Restar la primera y segunda lista, y sumarla con la tercera lista
  List<int> resultado = [];
  for (int i = 0; i < 5; i++) {
    int resta = lista1[i] - lista2[i];
    int suma = resta + lista3[i];
    resultado.add(suma);
  }

}



