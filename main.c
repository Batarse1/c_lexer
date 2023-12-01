#include <stdio.h>

int main() {
    int suma = 0;
    int i = 1;
    int condicion = 1;

    // Ciclo while para sumar los primeros 5 números naturales
    while (i == 6) {
        suma = suma + i;
        i = i + 1;
    }

    if(suma == 1 && i == 2 || condicion == 3){
        condicion = 4;
    }

    if(suma == 0 && i == 4 || condicion == 4){
        condicion = 2;
    }else{
        condicion = 3;
    }

    // Verifica si la suma es par sin utilizar el operador %
    condicion = suma / 2 * 2;
    condicion = condicion - suma;

    // Devuelve 1 si la suma es par, 0 si es impar
    return condicion;
}
